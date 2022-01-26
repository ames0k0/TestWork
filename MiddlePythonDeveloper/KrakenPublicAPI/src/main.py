#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# vim: ts=2, st

import os
import json
import socket
import sqlite3
import datetime
from typing import NewType, Generator, Optional, Union, Tuple, List, Dict
from collections import defaultdict
from urllib.parse import urlencode
from urllib.request import urlopen

from config import Static, DataBase, Data, Server


GEN_TRADES_TYPE = NewType(
  'Generated trades Type',
  Generator[Dict[str, Union[int, float]], None, None]
)
API_DATA_TYPE = NewType(
  'API Data Type', Dict[str, Union[str, int, float]]
)

class KrakenParser:
  URI = "https://api.kraken.com/0/public/Trades"

  @staticmethod
  def ts2dt(ts: float) -> datetime.datetime:
    return datetime.datetime.fromtimestamp(ts)

  @staticmethod
  def dt2ts(dt: datetime) -> float:
    return datetime.datetime.timestamp(dt)

  @staticmethod
  def days2td(days: int) -> datetime.timedelta:
    return datetime.timedelta(days)

  def _get(self, pair: Tuple[str], data_offset: float) -> Union[NotImplementedError, GEN_TRADES_TYPE]:
    hour = -1
    trades = urlopen(
      self.URI,
      urlencode({'pair': ''.join(pair), 'since': data_offset}).encode()
    )
    trades = json.load(trades)
    if trades['error']:
      raise NotImplementedError(trades['error'])

    trades['result'].pop('last')
    pair_key = list(trades['result'].keys())[0]
    hourly_trades = defaultdict(int)

    for trade in trades['result'][pair_key]:
      if (pair[0].startswith('X')):
        # ['0.80000000', '2429.23000', 1643128826.1641, 's', 'm', ''],
        (param, price, ts, action, *_) = trade
      else:
        # ['2429.23000', '0.80000000', 1643128826.1641, 's', 'm', ''],
        (price, param, ts, action, *_) = trade

      param = float(param)

      price_hour = self.ts2dt(ts).hour
      if (hour == -1):
        hour = price_hour
      elif (hour != price_hour):
        hour = price_hour
        yield hourly_trades
        hourly_trades.clear()

      if (not hourly_trades):
        hourly_trades['price'] = price
        hourly_trades['price_timestamp'] = ts
        hourly_trades['high'] = param
        hourly_trades['low'] = param
      else:
        if (param > hourly_trades['high']):
          hourly_trades['high'] = param
        elif (param < hourly_trades['low']):
          hourly_trades['low'] = param

      hourly_trades[action] += 1

    if (hourly_trades):
      yield hourly_trades

  def get_trades(self, data_offset: float) -> Tuple[Tuple[str], GEN_TRADES_TYPE]:
    """Returns pairs with hourly trades
    """
    for pair in Data.PAIRS:
      for data in self._get(pair, data_offset):
        yield (pair, data)


class KrakenDB:
  DB_PATH = os.path.join(Static.DIR, DataBase.FILENAME)

  def __init__(self):
    if not os.path.exists(self.DB_PATH):
      os.makedirs(Static.DIR, exist_ok=True)
      self.create_db()

  def create_db(self) -> None:
    with sqlite3.connect(self.DB_PATH) as conn:
      curr = conn.cursor()
      # curl "https://api.kraken.com/0/public/Trades?pair=XBTUSD"
      curr.execute(
        """
        CREATE TABLE IF NOT EXISTS %s (
          id INTEGER PRIMARY KEY,
          pair_left VARCHAR(5),
          pair_right VARCHAR(5),
          timestamp REAL,
          price VARCHAR(20),
          open INTEGER,
          close INTEGER,
          high REAL,
          low REAL
        )
        """ % (DataBase.NAME,)
      )
      conn.commit()

  @staticmethod
  def get_last_trade_ts(curr) -> Optional[Tuple[float]]:
    curr.execute(
      "SELECT timestamp FROM %s ORDER BY id DESC LIMIT 1" % (DataBase.NAME,)
    )
    return curr.fetchone()

  def get_data_offset(self, curr) -> float:
    """Calculates the data offset to get the data from
    """
    last_trade_ts = self.get_last_trade_ts(curr)
    current_datetime = datetime.datetime.now()

    data_offset = KrakenParser.dt2ts(
      current_datetime - KrakenParser.days2td(Data.OFFSET_DAYS)
    )
    if last_trade_ts is None:
      return data_offset

    last_data_datetime = KrakenParser.ts2dt(last_trade_ts[0])
    datetime_difference = (current_datetime - last_data_datetime)

    if (datetime_difference.days >= Data.OFFSET_DAYS):
      return data_offset

    # -N days
    data_offset = (
      current_datetime - KrakenParser.days2td(datetime_difference.days)
    )

    # +1 hour
    return KrakenParser.dt2ts(
      data_offset + datetime.timedelta(hours=1)
    )

  def update_db(self) -> None:
    """Update trades data from 30 days back with delay 1 hour
    """
    with sqlite3.connect(self.DB_PATH) as conn:
      curr = conn.cursor()
      data_offset = self.get_data_offset(curr)
      for (pair, data) in KrakenParser().get_trades(data_offset):
        curr.execute(
          """
          INSERT INTO %s (
            pair_left, pair_right, timestamp, price, open, close, high, low
          ) VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?
          )
          """ % (DataBase.NAME,),
          (
            *pair,
            data['price_timestamp'],
            data['price'], data['s'], data['b'], data['high'], data['low'],
          )
        )
      conn.commit()


class KrakenAPI:
  """Single API endpoint to get a data for pairs
  """
  def _get_by_filter(self, curr, pair: str, filter_param: str, new_ts: float, next_ts: float) -> Optional[API_DATA_TYPE]:
      curr.execute(
        """
        SELECT timestamp, close, open, price, high, low, max(%s) FROM %s
        WHERE (timestamp >= ? AND timestamp  < ?)
          AND (pair_left =  ? AND pair_right = ?)
        """ % (filter_param, DataBase.NAME),
        (new_ts, next_ts, *pair)
      )
      has_data = curr.fetchone()

      if has_data[0] is None:
        return has_data[0]

      trade_timestamp, closed_trades, opened_trades, trade_price, \
        p_high, p_low, _ = has_data

      return {
        'Type': 'min' if (filter_param == 'low') else 'max',
        'time': KrakenParser.ts2dt(trade_timestamp).strftime(Data.DATETIME_VIEW_FORMAT),
        'close': closed_trades,
        'open': opened_trades,
        'high': p_high,
        'low': p_low,
        'volume': float(trade_price)
      }

  def get(self, pair: str) -> List[API_DATA_TYPE]:
    # [{
    #   Type: “min”/”max”
    #   time: [DateTime],
    #   close: [number],    - 'b'
    #   open: [number],     - 's'
    #   high: [number],     - 1.80000000
    #   low: [number],      - 0.08000000
    #   volume: [number]    - price
    # }]
    data = []

    with sqlite3.connect(KrakenDB.DB_PATH) as conn:
      curr = conn.cursor()
      last_trade_ts = KrakenDB.get_last_trade_ts(curr)
      # NOTE: no checking for a None result, cuz parser runs first
      last_trade_dt = KrakenParser.ts2dt(last_trade_ts[0])

      new_date = datetime.datetime(
        last_trade_dt.year, last_trade_dt.month, last_trade_dt.day
      )
      new_ts = KrakenParser.dt2ts(new_date)

      next_date = (new_date + KrakenParser.days2td(1))
      next_ts = KrakenParser.dt2ts(next_date)

      high_trade = self._get_by_filter(curr, pair, 'high', new_ts, next_ts)
      if (high_trade is not None):
        data.append(high_trade)

      low_trade = self._get_by_filter(curr, pair, 'low', new_ts, next_ts)
      if (low_trade is not None):
        data.append(low_trade)

      if not data:
        return None

      return data

  def encode_message(self, message):
    # SEE: https://stackoverflow.com/questions/39817641/how-to-send-a-json-object-using-tcp-socket-in-python
    return bytes(json.dumps(message), encoding="utf-8")

  def run(self):
    # SEE: https://docs.python.org/3/howto/sockets.html
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
      server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      server_socket.bind((Server.HOST, Server.PORT))
      server_socket.listen(Server.MAX_CLIENTS)

      while True:
        (client_socket, address) = server_socket.accept()

        # SEE: https://realpython.com/python-sockets/
        with client_socket:
            data = client_socket.recv(Server.RECEIVE_BYTES)
            # GET /BTC-USD HTTP/1.1
            if (not data):
              client_socket.close()
              continue

            request = data.decode().split('\r\n')[0]
            r_type, r_endpoint, *_ = request.split(' ')

            if r_type != 'GET':
              client_socket.send(
                self.encode_message({'error': 'Allowed only GET request'})
              )
              continue

            if (Data.PAIR_DELIMITER not in r_endpoint):
              client_socket.send(
                self.encode_message({
                  'error': 'Endpoint: /pair_left-pair_rigth',
                  'pairs': Data.PAIRS
                })
              )
              continue

            endpoint_pair = r_endpoint.split(Data.PAIR_DELIMITER)
            if len(endpoint_pair) != 2:
              client_socket.send(
                self.encode_message({'error': 'Endpoint: /BTC-USD'})
              )
              continue

            pair = tuple(map(lambda x: x.strip('/').upper(), endpoint_pair))
            if (pair not in Data.PAIRS):
              client_socket.send(
                self.encode_message({'error': f"Pairs: {Data.PAIRS}"})
              )
              continue

            trade_data = self.get(pair)
            if (trade_data is None):
              client_socket.send(
                self.encode_message({'error': f"No trades for: {pair}"})
              )
              continue

            client_socket.send(self.encode_message(trade_data))


if __name__ == '__main__':
  print('Running parser')
  kdb = KrakenDB()
  kdb.update_db()

  print('Running API')
  kapi = KrakenAPI()
  kapi.run()

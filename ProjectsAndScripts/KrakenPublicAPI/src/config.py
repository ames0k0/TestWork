#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Static:
  DIR = 'static'


class DataBase:
  NAME = 'kraken_trades'
  FILENAME = 'kraken.db'


class Data:
  OFFSET_DAYS = 30
  DELAY = 1
  PAIRS = (
    ('BTC', 'USD'), ('ETH', 'USD'), ('XRP', 'EUR'), ('XRP', 'USD'),
  )
  PAIR_DELIMITER = '-'
  # 20.07.2021 14:00
  DATETIME_VIEW_FORMAT = '%d.%m.%Y %H:%M'


class Server:
  HOST = 'localhost'
  PORT = 80
  MAX_CLIENTS = 1
  RECEIVE_BYTES = 1024

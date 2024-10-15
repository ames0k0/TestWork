# yobit.net
YoBit is a centralized cryptocurrency exchange established in 2015 and registered in Russia

### Ticker: BTC to USD (`btc_usd`)
```python
import requests

def get_btc():
    url = 'https://yobit.net/api/2/btc_usd/ticker'
    response = requests.get(url).json()
    price = response['ticker']['last']
    return str(price) + 'usd'
```

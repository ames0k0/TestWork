from requests import get
from bs4 import BeautifulSoup as bs
from wget import download

url = 'https://www.nhk.or.jp/lesson/russian/download/'
r = get(url).text
soup = bs(r, 'lxml')

for i in soup.find_all('a'):
    con = i.get('href')
    if con.endswith('.mp3'):
        download('https://www.nhk.or.jp'+con)

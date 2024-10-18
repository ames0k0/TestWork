# OracleStat
```
# md5sum
502a33ded3ad5b0b64d68b06d183e1ca  data/TestTask.txt
```

### input
```bash
time poetry run python main.py "fefef
https://ya.ru
Not link

no"
```

### output
```
Строка "fefef" не является ссылкой.
Строка "Not link" не является ссылкой.
Строка "" не является ссылкой.
Строка "no" не является ссылкой.
{
  "https://ya.ru": {
    "GET": 200,
    "HEAD": 200,
    "OPTIONS": 302,
    "PUT": 302,
    "DELETE": 302,
    "POST": 200,
    "PATCH": 200,
    "CONNECT": 200
  }
}

real    0m1,677s
user    0m0,672s
sys     0m0,075s
```

### Tests
```bash
poetry run coverage report -m
```
```
Name       Stmts   Miss  Cover   Missing
----------------------------------------
main.py       50     21    58%   32-33, 44, 51-52, 57-67, 71-81
tests.py       8      0   100%
----------------------------------------
TOTAL         58     21    64%
```

### TimeSpent
```
Start
  Ср 25 сен 2024 16:54:11 MSK
  - 1h
Start
  Чт 26 сен 2024 08:01:24 MSK
  - 5h
```

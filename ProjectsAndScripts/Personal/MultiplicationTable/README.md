# Multiplication Table
<details>
<summary>Зависимости проекта</summary>
<pre>
poetry -V                     # Poetry (version 1.8.3)
poetry run python -V          # Python 3.11.6
</pre>
</details>

```bash
poetry run python main.py
```
```
usage: main.py [-h] [-mt MT] [-nmt NMT]

options:
  -h, --help  show this help message and exit
  -mt MT      Multiplication Table (ex.): -mt 10
  -nmt NMT    Negative Multiplication Table (ex.): -nmt=-10x1


+-------+------+--------+-------------------------------------------+-----------------+
| First | Mark | Second |                     NL                    |     Example     |
+-------+------+--------+-------------------------------------------+-----------------+
|   +   |  x   |   +    |       two positives make a positive       |    3 x 2 = 6    |
|   -   |  x   |   -    |       two negatives make a positive       | (-3) x (-2) = 6 |
|   -   |  x   |   +    | a negative and a positive make a negative |  (-3) x 2 = -6  |
|   +   |  x   |   -    | a positive and a negative make a negative |  3 x (-2) = -6  |
+-------+------+--------+-------------------------------------------+-----------------+
```
```bash
poetry run python main.py -mt 10
```
```
+----+----+----+----+----+----+----+----+----+-----+
| 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  |  10 |
+----+----+----+----+----+----+----+----+----+-----+
| 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  |  10 |
| 2  | 4  | 6  | 8  | 10 | 12 | 14 | 16 | 18 |  20 |
| 3  | 6  | 9  | 12 | 15 | 18 | 21 | 24 | 27 |  30 |
| 4  | 8  | 12 | 16 | 20 | 24 | 28 | 32 | 36 |  40 |
| 5  | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 |  50 |
| 6  | 12 | 18 | 24 | 30 | 36 | 42 | 48 | 54 |  60 |
| 7  | 14 | 21 | 28 | 35 | 42 | 49 | 56 | 63 |  70 |
| 8  | 16 | 24 | 32 | 40 | 48 | 56 | 64 | 72 |  80 |
| 9  | 18 | 27 | 36 | 45 | 54 | 63 | 72 | 81 |  90 |
| 10 | 20 | 30 | 40 | 50 | 60 | 70 | 80 | 90 | 100 |
+----+----+----+----+----+----+----+----+----+-----+
```

```bash
poetry run python main.py -nmt=-10x1
```
```
+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
|  X  | -10 |  -9 |  -8 |  -7 |  -6 |  -5 |  -4 |  -3 |  -2 |  -1 |  0  |  1  |
+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
| -10 | 100 |  90 |  80 |  70 |  60 |  50 |  40 |  30 |  20 |  10 |   0 | -10 |
|  -9 |  90 |  81 |  72 |  63 |  54 |  45 |  36 |  27 |  18 |   9 |   0 |  -9 |
|  -8 |  80 |  72 |  64 |  56 |  48 |  40 |  32 |  24 |  16 |   8 |   0 |  -8 |
|  -7 |  70 |  63 |  56 |  49 |  42 |  35 |  28 |  21 |  14 |   7 |   0 |  -7 |
|  -6 |  60 |  54 |  48 |  42 |  36 |  30 |  24 |  18 |  12 |   6 |   0 |  -6 |
|  -5 |  50 |  45 |  40 |  35 |  30 |  25 |  20 |  15 |  10 |   5 |   0 |  -5 |
|  -4 |  40 |  36 |  32 |  28 |  24 |  20 |  16 |  12 |   8 |   4 |   0 |  -4 |
|  -3 |  30 |  27 |  24 |  21 |  18 |  15 |  12 |   9 |   6 |   3 |   0 |  -3 |
|  -2 |  20 |  18 |  16 |  14 |  12 |  10 |   8 |   6 |   4 |   2 |   0 |  -2 |
|  -1 |  10 |   9 |   8 |   7 |   6 |   5 |   4 |   3 |   2 |   1 |   0 |  -1 |
|   0 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
|   1 | -10 |  -9 |  -8 |  -7 |  -6 |  -5 |  -4 |  -3 |  -2 |  -1 |   0 |   1 |
+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
```
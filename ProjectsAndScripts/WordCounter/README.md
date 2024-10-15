# Word Counter: Python Implementation
### Context
```
# 1. -l считает количество строк
$ cat /etc/passwd| wc  -l
46
# 2. -w считает количество слов
$ cat /etc/passwd| wc -w
62
# 3. -c считает количество байт
$ cat /etc/passwd| wc -c
2381
# 4. запуск без аргументов
$ cat /etc/passwd| wc
46      62    2381
```
### Implementation
```
python3 wc.py

$ cat tfile.txt | ./wc.py <option>
$ ./wc.py <file> <option>

-l считает количество строк
-w считает количество слов
-c считает количество байт
```
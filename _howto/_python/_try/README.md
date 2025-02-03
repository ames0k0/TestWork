try
```python
try:
	1/0
except ZeroDivisionError:
	pass
```

contextlib.suppress
```python
import contextlib
with contextlib.suppress(ZeroDivisionError):
	1/0
```

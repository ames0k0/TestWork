# Morse Code
```python
class Dot: pass
class Dash: pass
class Delimiter: pass
class Character: pass
class Characters: pass

# Character from Dots and Dashes
# Delimiter as a Code stop \n|\0

# TODO
# __mul__
# __add__
# __eq__
# __contains__

# Generate a Character and then use it to check
# - Save and Load Characters ?!
```

```python
#   A                        E
s = dot + dash + delimiter + dot + delimiter + delimiter
#   E                 T
s + dot + delimiter + dash + delimiter + delimiter
```

```
! <__main__.Word object at 0x7b5f337abbb0>
	> <__main__.Character object at 0x7b5f337abfd0>
		> <__main__.Dot object at 0x7b5f337ae740>
		> <__main__.Dash object at 0x7b5f337ae780>
	> <__main__.Character object at 0x7b5f337abb80>
		> <__main__.Dot object at 0x7b5f337ae740>
! <__main__.Word object at 0x7b5f337abaf0>
	> <__main__.Character object at 0x7b5f337abb50>
		> <__main__.Dot object at 0x7b5f337ae740>
	> <__main__.Character object at 0x7b5f337abac0>
		> <__main__.Dash object at 0x7b5f337ae780>
```

## Context
![aa](./docs/a.png)
![bb](./docs/b.png)
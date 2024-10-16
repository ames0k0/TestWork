# Morse Code
```python
class Dot: pass
class Dash: pass
class Delimiter: pass
class Character: pass
class Word: pass
class Sentence: pass

dot = Dot()
dash = Dash()
delimiter = Delimiter()

#   A                        E
s = dot + dash + delimiter + dot + delimiter + delimiter
#   E                 T
s + dot + delimiter + dash + delimiter + delimiter

for word in s.sentence:
    print(word)
    for char in word.characters:
        print('\t', char)
        for sym in char.symbols:
            print('\t\t', sym)
```

```
<__main__.Word object at 0x7570bc9ad1e0>
	 <__main__.Character object at 0x7570bc9ad630>
		 <__main__.Dot object at 0x7570bc9d4b90>
		 <__main__.Dash object at 0x7570bc80f570>
	 <__main__.Character object at 0x7570bc9acf70>
		 <__main__.Dot object at 0x7570bc9d4b90>
<__main__.Word object at 0x7570bc9ac9d0>
	 <__main__.Character object at 0x7570bc9acbb0>
		 <__main__.Dot object at 0x7570bc9d4b90>
	 <__main__.Character object at 0x7570bc9ac910>
		 <__main__.Dash object at 0x7570bc80f570>
```

## Context
![aa](./docs/a.png)
![bb](./docs/b.png)
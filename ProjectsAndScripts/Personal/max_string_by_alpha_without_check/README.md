# Max String without check
```
|a|aa
|a|ba
 +---> 0 -> reposition ?? (Noi)

a|a|b
a|b|a
  +--> 1 -> reposition
  tindex -> to_position[1] -> 1 -> not_changed

aa|b|
ab|a|
   +--> 1 -> reposition
   tindex -> to_position[0] -> 1 -> [a, b] -> do_reposition (??)


a = 'aba'
b = 'aaaa'
    by alpha <a> the max one, but by whole length result will be <b>

    to change it, ^do_reposition may help :: ^do_reposition -> found the greather one
```
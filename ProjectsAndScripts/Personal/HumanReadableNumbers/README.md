# Human Readable Numbers
```python
from __file__ import RegisterNumber
rn = RegisterNumber()

# 1065034002018 | 1 trillion 65 billion 34 million 2 thousand 18    | tr65bi34mi2th18
# 1065034002018 | 1 trillion 65 billion 34 million 2 thousand ten 8 | tr65bi34mi2thte8

rn.register('SECRET_KEY', 'tr65bi34mi2th18')    # REGISTER NUMBER TO KEY: SECRET_KEY
rn.use('SECRET_KEY')                            # RETURNS: 1065034002018
```

```bash
python3 main.py
# >>> tr65bi34mi2th18
# <<< 1065034002018
```
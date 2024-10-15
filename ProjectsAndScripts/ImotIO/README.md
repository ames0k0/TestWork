# [ImotIO](https://imot.io/)
STT-Engine result fixer
```python
TEST_RES = [
    {"word": "foo", "start": 3.1, "end": 3.2},
    {"word": "bar", "start": 3.3, "end": 3.5},
    {"word": "a", "start": 3.7, "end": 3.9},
]
TEST_RULES = {'a': 'baz'}
TEST_FIXED = [
    {"word": "foo", "start": 3.1, "end": 3.2},
    {"word": "bar", "start": 3.3, "end": 3.5},
    {"word": "baz", "start": 3.7, "end": 3.9},
]
assert fix_function(TEST_RES, TEST_RULES) == TEST_FIXED, \
    '"single word" index at the end'
```
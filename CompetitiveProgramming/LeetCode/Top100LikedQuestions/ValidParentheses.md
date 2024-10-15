### Python
```python
class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    pairs = {
      '(': ')',
      '{': '}',
      '[': ']'
    }
    u_pairs = {v: k for k, v in pairs.items()}
    for char in s:
      if (pairs.get(char) is not None):
        stack.append(char)
        continue
      if not (stack):
        return False
      end = u_pairs.get(char)
      if (end != stack[-1]):
        return False
      stack.pop(-1)
    return True if (not stack) else False
```

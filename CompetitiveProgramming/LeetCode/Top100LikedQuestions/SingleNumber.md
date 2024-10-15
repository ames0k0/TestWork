### Python
```python
class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    D = {}
    for n in nums:
      if (D.get(n) is None):
        D[n] = 1
        continue
      D[n] += 1
    for k, v in D.items():
      if (v == 1):
        return k
```

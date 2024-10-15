### Python
```
class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    M = {}
    for n in nums:
      if (M.get(n) is None):
        M[n] = 0
      M[n] += 1
    mk = None
    mv = None
    for k, v in M.items():
      if (mk is None):
        mk = k
        mv = v
        continue
      if (v > mv):
        mk = k
        mv = v
    return mk
```

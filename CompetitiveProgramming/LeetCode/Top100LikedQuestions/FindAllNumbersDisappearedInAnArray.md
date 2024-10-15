### Python
```python
from typing import List

class Solution:
  def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    missing = []
    next_ = None
    nums.sort()
    for n in nums:
      if (next_ is None):
        if (n != 1):
          missing.extend(range(1, n))
        next_ = n
        continue
      while (next_ != n):
        next_ += 1
        if (next_ == n):
          break
        missing.append(next_)
    if (nums[-1] != len(nums)):
      missing.extend(range(nums[-1]+1, len(nums)+1))
    return missing

if __name__ == '__main__':
  s = Solution()
  for a, r in (
    ([1, 6, 15, 11], [2, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14]),
    ([1,1], [2]),
    ([1,1,4], [2, 3]),
    ([2,2], [1]),
    ([1,2], []),
    ([1,1,2,2], [3, 4])
  ):
    assert s.findDisappearedNumbers(a) == r, r
```

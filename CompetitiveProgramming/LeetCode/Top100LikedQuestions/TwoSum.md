### Python3
```python
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    for idx, i in enumerate(nums):
      k = target - i
      for jdx, j in enumerate(nums):
        if (idx == jdx):
          continue
        if j == k:
          return idx, jdx
```

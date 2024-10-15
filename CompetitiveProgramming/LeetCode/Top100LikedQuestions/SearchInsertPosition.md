### Python
```python
class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    for nidx, n in enumerate(nums):
      if n >= target:
        return (nidx)
    return len(nums)
```

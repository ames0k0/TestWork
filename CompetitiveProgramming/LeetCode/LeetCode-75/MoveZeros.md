### Python
```python
class Solution(object):
  def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    zero_idx = None
    for idx, value in enumerate(nums):
      if (value == 0):
        if zero_idx is None:
          zero_idx = idx
        continue
      if zero_idx is None:
        continue
      nums[idx], nums[zero_idx] = nums[zero_idx], nums[idx]
      zero_idx += 1
```

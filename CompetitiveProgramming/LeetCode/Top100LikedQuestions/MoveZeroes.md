### Python
```python
class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    for nidx, n in enumerate(reversed(nums[:])):
      nidx += 1
      if (n == 0):
        nums.append(nums.pop(-nidx))
    return nums
```

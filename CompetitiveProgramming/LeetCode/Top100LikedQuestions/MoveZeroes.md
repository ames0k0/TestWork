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

### Golang
```go
func moveZeroes(nums []int) {
	var zidx int
	var zero_idx_is_set bool
	for nidx, num := range nums {
		if num == 0 && !zero_idx_is_set {
			zidx = nidx
			zero_idx_is_set = true
			continue
		}
		if num != 0 && zero_idx_is_set {
			nums[zidx], nums[nidx] = nums[nidx], nums[zidx]
			zidx += 1
		}
	}
}
```

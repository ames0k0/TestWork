#### Version: 1 (TLE)

Python
```python
class Solution:
  def countOdds(self, low: int, high: int) -> int:
    odd_count = 0
    for n in range(low, high+1):
      if (n % 2 != 0):
        odd_count += 1
    return odd_count
```

C++
```cpp
class Solution {
public:
  int countOdds(int low, int high) {
    int oddCount = 0;
    for (; low <= high; low++) {
      if (low % 2 != 0) {
        oddCount++;
      }
    }
    return oddCount;
  }
};
```

#### Version: 2

Python
```python
class Solution:
  def countOdds(self, low: int, high: int) -> int:
    odd_count = 0
    if (low % 2 != 0):
      odd_count += 1
      low += 1
    if (high % 2 != 0):
      odd_count += 1
      high -= 1
    mid = (high - low)
    mid //= 2
    return (mid + odd_count)
```

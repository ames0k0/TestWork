Python
```python
from functools import reduce

class Solution:
  def subtractProductAndSum(self, n: int) -> int:
    n = [int(i) for i in str(n)]
    return (
      reduce(lambda x, y: x * y, n)
      -
      reduce(lambda x, y: x + y, n)
    )
```

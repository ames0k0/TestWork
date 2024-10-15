##### Version: 1 (WA)

Pyhton
```python
from collections import deque

class Solution:
  def average(self, salary: List[int]) -> float:
    dq = deque(sorted(salary))
    while len(dq) > 2:
      dq.pop()
      dq.popleft()
    return sum(dq) / len(dq)
```


##### Version 2

Python
```python
class Solution:
  def average(self, salary: List[int]) -> float:
    salary = sorted(salary)
    avg = sum(salary)
    avg -= salary[0]
    avg -= salary[-1]
    avg /= (len(salary) - 2)
    return avg
```

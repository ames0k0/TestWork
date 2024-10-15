# Find Max Zeros
Given: [7, 15, 6, 20, 5, 10]<br/>
Multiplication of the combinations of 3: [630, ..., 1000]<br/>
Has max zeros length: 3

```python
def find_max_zeros(A):
    nem = [f"{reduce(lambda x, y: x*y, comb)}" for comb in combinations(A, 3)]
    return len(max(findall(r'0+', "".join(nem))))
```

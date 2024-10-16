# Filter Duplicates by Timestamp
```python
# Input
operations = [
    {"id": 1, "timestamp": 2, "amount": 1},
    {"id": 2, "timestamp": 4, "amount": 8},
    {"id": 1, "timestamp": 3, "amount": 2}
]

# process
filter(operations)

# Output
operations = [
    {"id": 1, "timestamp": 3, "amount": 2},
    {"id": 2, "timestamp": 4, "amount": 8}
]
```
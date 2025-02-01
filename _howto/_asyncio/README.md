asyncio.gather - [EXAMPLE](./_gather.py)
```python
await asyncio.gather(
	*[
		asyncio.create_task(task(task_id=idx, ttl=ttl))
		for idx, ttl in enumerate([3, 2, 1, 1, 2])
	]
)
```

asyncio.TaskGrop - [EXAMPLE](./_task_group.py)
```python
async with asyncio.TaskGroup() as group:
	for idx, ttl in enumerate([3, 2, 1, 1, 2]):
		group.create_task(task(task_id=idx, ttl=ttl))
```

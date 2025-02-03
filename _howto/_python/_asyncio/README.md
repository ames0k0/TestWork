asyncio.gather - [EXAMPLE](./_gather.py)
```python
tasks = []
for idx, ttl in enumerate([3, 2, 1, 1, 2]):
	tasks.append(
		asyncio.create_task(task(task_id=idx, ttl=ttl))
	)
await asyncio.gather(*tasks)
```

asyncio.TaskGrop - [EXAMPLE](./_task_group.py)
```python
async with asyncio.TaskGroup() as group:
	for idx, ttl in enumerate([3, 2, 1, 1, 2]):
		group.create_task(task(task_id=idx, ttl=ttl))
```

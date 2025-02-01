"""
[0] Started
[1] Started
[2] Started
[3] Started
[4] Started
[2] Ended
[3] Ended
[1] Ended
[4] Ended
[0] Ended
>>>> 3.0014827251434326
"""
import time
import asyncio

async def task(*, task_id: int, ttl: int) -> None:
	print(f'[{task_id}] Started')
	await asyncio.sleep(ttl)
	print(f'[{task_id}] Ended')

async def main():
	start = time.time()
	await asyncio.gather(
		*[
			asyncio.create_task(task(task_id=idx, ttl=ttl))
			for idx, ttl in enumerate([3, 2, 1, 1, 2])
		]
	)
	end = time.time()
	print('>>>>', end - start)

if __name__ == '__main__':
	asyncio.run(main())

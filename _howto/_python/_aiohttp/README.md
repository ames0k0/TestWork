json_response - [EXAMPLE](./jsn.py)
```python
def empty(argv):
	app = web.Application()
	app.router.add_get("/", lambda x: web.json_response({}))
	return app
```

```bash
python -m aiohttp.web -H localhost -P 8080 jsn:empty
```

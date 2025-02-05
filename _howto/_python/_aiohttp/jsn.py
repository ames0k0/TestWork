from aiohttp import web

def empty(argv):
  app = web.Application()
  app.router.add_get("/", lambda x: web.json_response({}))
  return app

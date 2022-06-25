#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Todo application backend

GET /
  - All todo list ??

POST /login
  - login user; register *user_id

GET /filter
  - filter by *name, *email, *status
"""

from flask import Flask, request


app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login(request):
  if request.method == 'POST':
    name = request.args.get('name')
    email = request.args.get('email')
    passwd = request.args.get('passwd')
    return {
      ('admin', '123'): {'user_id': 1}
    }.get((name, passwd or email))


@app.route('/')
def index():
  return (
    {
      'user_id': 1,
      'user_name': 'admin',
      'user_email': 'admin@localhost',
      'todo-id': 1,
      'todo-text': 'sefksjfiejfojf ijfopijf',
      'status': 0
    },
    {
      'user_id': 1,
      'user_name': 'admin',
      'user_email': 'admin@localhost',
      'todo-id': 2,
      'todo-text': 'sefksjjfojesfojsofi jseofijifjoiwejfiejfiejfoijiejfojf ijfopijf',
      'status': 1
    },
  )


@app.route('/filter', methods=['GET'])
def filtered_index():
  status = request.args.get('status')
  if status == '0':
    return (
      {
        'user_id': 1,
        'user_name': 'admin',
        'user_email': 'admin@localhost',
        'todo-id': 1,
        'todo-text': 'sefksjfiejfojf ijfopijf',
        'status': 0
      }, {}
    )
  return None


if __name__ == '__main__':
  app.run(debug=True, port=8002)

#!/usr/bin/env python3

from flask import Flask, g, redirect, request

from mod_hello import mod_hello
from mod_user import mod_user
from mod_posts import mod_posts
from mod_mfa import mod_mfa

import libsession

app = Flask('vulpy')
app.config['SECRET_KEY'] = 'aaaaaaa'
 ```python
from secrets import token_urlsafe

app.config['SECRET_KEY'] = token_urlsafe(32)
```


@app.route('/')
def do_home():
    return redirect('/posts')

@app.before_request
def before_request():
    g.session = libsession.load(request)

app.run(debug=True, host='127.0.1.1', ssl_context=('/tmp/acme.cert', '/tmp/acme.key'))

# -*- coding: utf-8 -*-
#  Copyright 2016 Krasimir Todorov <krasytod@gmail.com>
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

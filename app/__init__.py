# -*- coding: utf-8 -*-
#  __init__.py
#  Copyright 2016 Krasimir Todorov <krasytod@gmail.com>
from flask import Flask

app = Flask(__name__)
from app import views


#!/usr/bin/env python3

from bottle import route
from bottle import static_file
from bottle import request, redirect, response
from bottle import template
from bottle import abort

"""
This module handles all of the URL dispatching for gn-documents, mapping from
URLs to the functions that will be called in response.
"""

import urllib.request

@route('/')
def index():
    return "oh hecks yes"

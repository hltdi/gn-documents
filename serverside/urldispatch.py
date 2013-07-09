#!/usr/bin/env python3

from bottle import abort
from bottle import error
from bottle import request, redirect, response
from bottle import route
from bottle import static_file
from bottle import template

"""
This module handles all of the URL dispatching for gn-documents, mapping from
URLs to the functions that will be called in response.
"""

import urllib.request

@route('/')
def index():
    redirect("/inicio")

@error(404)
def error404(error):
    return 'Nothing here, sorry'

@route('/catalogo')
def catalogo():
    return static_file('catalogo.html', root='static')

@route('/inicio')
def inicio():
    return static_file('inicio.html', root='static')

@route('/subir')
def subir():
    return static_file('subir.html', root='static')

@route('/style/<fn>')
def style(fn):
    return static_file(fn, root='static/style')

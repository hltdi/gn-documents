#!/usr/bin/env python3

from bottle import abort
from bottle import error
from bottle import request, redirect, response
from bottle import route
from bottle import static_file
from bottle import template

import search

"""
This module handles all of the URL dispatching for gn-documents, mapping from
URLs to the functions that will be called in response.
"""

import urllib.request

@route('/')
def index():
    return static_file('index.html', root='static')

@route('/buscar/<q>')
def buscar(q):
    return search.search(q)

@error(404)
def error404(error):
    return 'Nothing here, sorry'

@route('/catalogo')
def catalogo():
    return static_file('catalogo.html', root='static')

@route('/inicio')
def inicio():
    return static_file('inicio.html', root='static')

@route('/subir', method='GET')
def subir():
    return static_file('subir.html', root='static')

@route('/upload', method='POST')
def do_login():
    spanishDoc = request.files.get('uploadSpanish')
    guaraniDoc = request.files.get('uploadGuarani')
    
    guaraniDoc.save('uploadedDocs') # appends guaraniDoc.filename automatically
    spanishDoc.save('uploadedDocs') # appends spanishDoc.filename automatically	
    return 'OK'

@route('/css/<fn>')
def style(fn):
    return static_file(fn, root='css')

@route('/js/<fn>')
def js(fn):
    return static_file(fn, root='js')

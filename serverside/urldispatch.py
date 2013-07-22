#!/usr/bin/env python3

from bottle import error
from bottle import request
from bottle import route
from bottle import static_file
from bottle import template

import search

"""
This module handles all of the URL dispatching for gn-documents, mapping from
URLs to the functions that will be called in response.
"""

@route('/')
def index_test():
    return static_file('index.html', root='static')

@route('/index')
def index():
    return template('index')

@route('/catalog')
def catalog():
    return template('catalog')

@route('/upload', method='GET')
def upload_page():
    return template('upload')

@route('/upload', method='POST')
def upload_files():
    spanishDoc = request.files.get('uploadSpanish')
    guaraniDoc = request.files.get('uploadGuarani')
    
    guaraniDoc.save('uploadedDocs') # appends guaraniDoc.filename automatically
    spanishDoc.save('uploadedDocs') # appends spanishDoc.filename automatically	
    return 'OK'

@route('/docs/<fn>')
def docs(fn):
    return static_file(fn, root='docs')

@route('/css/<fn>')
def style(fn):
    return static_file(fn, root='css')

@route('/js/<fn>')
def js(fn):
    return static_file(fn, root='js')

@error(404)
def error404(error):
    return 'Nothing here, sorry'

@route('/buscar/<q>')
def buscar(q):
    return search.search(q)

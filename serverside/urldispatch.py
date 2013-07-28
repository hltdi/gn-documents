#!/usr/bin/env python3

from bottle import error
from bottle import request
from bottle import route
from bottle import static_file

import search

"""
This module handles all of the URL dispatching for gn-documents, mapping from
URLs to the functions that will be called in response.
"""

@route('/')
def index_test():
    return static_file('index.html', root='static')

@route('/index', method='GET')
def index():
    return static_file('index.html', root='app')

@route('/partials/<fn>', method='GET')
def partials(fn):
    return static_file(fn, root='app/partials')

@route('/css/<fn>')
def css(fn):
    return static_file(fn, root='app/css')

@route('/js/<fn>')
def js(fn):
    return static_file(fn, root='app/js')

@route('/img/<fn>')
def img(fn):
    return static_file(fn, root='app/img')

@route('/lib/<fn>')
def lib(fn):
    return static_file(fn, root='app/lib')

@error(404)
def error404(error):
    return ('Nothing here, sorry: ' + str(error))

@route('/upload', method='POST')
def upload_files():
    spanishDoc = request.files.get('uploadSpanish')
    guaraniDoc = request.files.get('uploadGuarani')
    
    guaraniDoc.save('uploadedDocs', overwrite=True) # appends guaraniDoc.filename automatically
    spanishDoc.save('uploadedDocs', overwrite=True) # appends spanishDoc.filename automatically	
    return {'success':True, 'message': 'Documentos subidos exitosamente'}

@route('/docs/<fn>')
def docs(fn):
    return static_file(fn, root='docs')

@route('/buscar/<q>')
def buscar(q):
    return search.search(q)

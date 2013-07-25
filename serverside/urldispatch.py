#!/usr/bin/env python3

from bottle import error
from bottle import request
from bottle import route
from bottle import static_file
from bottle import template
from bottle import redirect

import search

"""
This module handles all of the URL dispatching for gn-documents, mapping from
URLs to the functions that will be called in response.
"""

APPNAME = "/tahekami"

@route('/')
def top():
    redirect(APPNAME)

@route(APPNAME)
@route(APPNAME + '/')
def index_test():
    return static_file('index.html', root='static')

@route(APPNAME + '/index')
def index():
    return template('index')

@route(APPNAME + '/catalog')
def catalog():
    return template('catalog')

@route(APPNAME + '/upload', method='GET')
def upload_page():
    return template('upload')

@route(APPNAME + '/upload', method='POST')
def upload_files():
    spanishDoc = request.files.get('uploadSpanish')
    guaraniDoc = request.files.get('uploadGuarani')
    
    guaraniDoc.save('uploadedDocs', overwrite=True) # appends guaraniDoc.filename automatically
    spanishDoc.save('uploadedDocs', overwrite=True) # appends spanishDoc.filename automatically	
    return {'success':True, 'message': 'Documentos subidos exitosamente'}

@route(APPNAME + '/docs/<fn>')
def docs(fn):
    return static_file(fn, root='docs')

@route(APPNAME + '/css/<fn>')
def style(fn):
    return static_file(fn, root='css')

@route('/favicon.ico')
def favicon():
    return static_file('favicon.ico', root='css')

@route(APPNAME + '/js/<fn>')
def js(fn):
    return static_file(fn, root='js')

@error(404)
def error404(error):
    return 'Nothing here, sorry'

@route(APPNAME + '/buscar/<q>')
def buscar(q):
    return search.search(q)

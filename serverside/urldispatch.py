#!/usr/bin/env python3

from bottle import error
from bottle import request
from bottle import route
from bottle import static_file

import search
import os

"""
This module handles all of the URL dispatching for gn-documents, mapping from
URLs to the functions that will be called in response.
"""

UPLOADED_DOCS_DIR = 'uploadedDocs';

@route('/')
def index_test():
    return static_file('index.html', root='app')

@route('/partials/<fn>')
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
    if(guaraniDoc is not None):
        guaraniDoc.save(UPLOADED_DOCS_DIR, overwrite=True) # appends guaraniDoc.filename automatically
    if(spanishDoc is not None):
        spanishDoc.save(UPLOADED_DOCS_DIR, overwrite=True) # appends spanishDoc.filename automatically	
    return {'success':True, 'message': 'Documentos subidos exitosamente'}

@route('/uploaded/totalfiles')
def count_uploaded_files():
    #ignore .gitignore file
    total = len([name for name in os.listdir(UPLOADED_DOCS_DIR) if os.path.isfile(UPLOADED_DOCS_DIR + '/' + name)]) - 1 
    return {'total': total}

@route('/docs/<fn>')
def docs(fn):
    return static_file(fn, root='docs')

@route('/buscar/<q>')
def buscar(q):
    return search.search(q)

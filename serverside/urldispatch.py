#!/usr/bin/env python3

from bottle import error
from bottle import request
from bottle import response
from bottle import route
from bottle import static_file

import search
import os
import json

"""
This module handles all of the URL dispatching for gn-documents, mapping from
URLs to the functions that will be called in response.
"""

UPLOADED_DOCS_DIR = 'uploadedDocs';

@route('/')
def index():
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
    parameters = {"title" : request.forms.get('title'), "language": request.forms.get('language'),
                  "tags" : request.forms.get('tags'), "author" : request.forms.get('author'),
                  "institute" : request.forms.get('institute'), "downloadable" : request.forms.get('downloadable')}
    files = []
    files.append(request.files.get('uploadSpanish'))
    files.append(request.files.get('uploadGuarani'))
    for file in files:
        if(file is not None):
            file.save(UPLOADED_DOCS_DIR, overwrite=True) # appends file.filename automatically
            f = open(UPLOADED_DOCS_DIR + '/' + file.filename + '.json', 'w')
            f.write(json.dumps(parameters))
            f.close()
    return {'success':True, 'message': 'Documentos subidos exitosamente'}

@route('/uploaded/totalfiles')
def count_uploaded_files():
    #ignore .gitignore file
    total = len([name for name in os.listdir(UPLOADED_DOCS_DIR) if os.path.isfile(UPLOADED_DOCS_DIR + '/' + name)]) - 1 
    return {'total': total}

@route('/uploaded/alltags')
def alltags():
    ## XXX(alexr): do we need to set these?
    response.set_header('Cache-Control', 'No-Cache')
    response.set_header("Content-Type", "application/json")
    return static_file('alltags.json', root='indexdir')

@route('/docs/<fn>')
def docs(fn):
    return static_file(fn, root='docs')

@route('/buscar/<q>')
def buscar(q):
    response.set_header('Cache-Control', 'No-Cache')
    return search.search(q)

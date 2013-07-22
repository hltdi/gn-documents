#!/bin/bash

export PYTHONPATH=$PYTHONPATH:searchengine:lib/whoosh.par
python3 searchengine/add_documents.py $*

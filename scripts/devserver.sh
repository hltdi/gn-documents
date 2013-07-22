#!/bin/bash

export PYTHONPATH=$PYTHONPATH:serverside:searchengine:lib/whoosh.par
python3 scripts/devserver.py

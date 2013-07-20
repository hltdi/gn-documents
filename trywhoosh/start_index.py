#!/usr/bin/env python3

import os
import whoosh.index
from whoosh.fields import *

INDEXDIR = "indexdir"

THESCHEMA = Schema(title=TEXT(stored=True),
                   path=ID(stored=True),
                   tags=KEYWORD(stored=True,lowercase=True,commas=True),
                   content=TEXT)

def store_index():
    if not os.path.exists(INDEXDIR):
        os.mkdir(INDEXDIR, 0o700)
    ix = whoosh.index.create_in(INDEXDIR, THESCHEMA)
    writer = ix.writer()
    writer.commit()

def check_for_index():
    if os.path.exists(INDEXDIR):
        ix = whoosh.index.open_dir(INDEXDIR)
        if not ix: return False
        if ix and (ix.schema != THESCHEMA):
            print("warning!! there is an index, but with an outdated schema.")
        return True
    return False

def main():
    found_index = False
    try:
        found_index = check_for_index()
    except:
        pass

    if not found_index:
        store_index()
    else:
        print("Index already there, no worries.")

if __name__ == "__main__": main()

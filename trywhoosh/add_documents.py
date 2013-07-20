#!/usr/bin/env python3

import os
import sys

import whoosh.index
from whoosh.fields import *

from start_index import THESCHEMA 
from start_index import INDEXDIR 

def add_document(fn, writer):
    fn = os.path.abspath(fn)
    pathto, endfn = os.path.split(fn)
    text = ""
    with open(fn) as infile:
        text = infile.read()
    writer.add_document(title=endfn,
                        path=endfn,
                        tags="foo,bar",
                        content=text)

def main():
    fns = sys.argv[1:]
    print("fns:", fns)
    ix = whoosh.index.open_dir(INDEXDIR)
    writer = ix.writer()
    for fn in fns:
        add_document(fn, writer)
    writer.commit()

if __name__ == "__main__": main()

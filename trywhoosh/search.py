#!/usr/bin/env python3

import os
import whoosh.index
from whoosh.qparser import QueryParser

from start_index import INDEXDIR 

def search(searcher, ix, q):
        query = QueryParser("content", ix.schema).parse(q)
        results = searcher.search(query)
        print(results)
        for result in results:
            print(result)

def main():
    ix = whoosh.index.open_dir(INDEXDIR)
    with ix.searcher() as searcher:
        while True:
            try:
                q = input("? ")
                if not q: continue
                search(searcher, ix, q)
            except: break
    print()

if __name__ == "__main__": main()

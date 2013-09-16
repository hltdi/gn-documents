import json

import whoosh.index
from whoosh.qparser import QueryParser
from start_index import INDEXDIR 

def search(q):
    out = []
    ix = whoosh.index.open_dir(INDEXDIR)
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(q)
        results = searcher.search(query)
        for result in results:
            msg = {}
            msg['title'] = result['title']
            msg['snippet'] = result.highlights("content")
            msg['url'] = "docs/" + result['path']
            out.append(msg)
    return json.dumps(out)

def search_by_tag(q):
    out = []
    ix = whoosh.index.open_dir(INDEXDIR)
    with ix.searcher() as searcher:
        query = QueryParser("tags", ix.schema).parse(q)
        results = searcher.search(query)
        for result in results:
            msg = {}
            msg['title'] = result['title']
            msg['tags'] = result['tags'].split(',')
            msg['url'] = "docs/" + result['path']
            out.append(msg)
    return json.dumps(out)

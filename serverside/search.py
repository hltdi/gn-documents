import json

def search(query):
    out = {}
    out['message'] = 'there are no matching documents for ' + query
    return json.dumps(out)    

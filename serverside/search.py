import json

def search(query):
    out = []
    for i in range(5):
        msg = {}
        msg['title'] = 'title' + str(i)
        msg['snippet'] = 'snippet' + str(i)
        msg['url'] = 'url' + str(i)
        out.append(msg)
    return json.dumps(out)    

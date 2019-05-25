from flask import jsonify

def response(json = None, status = None):
    r = {}
    if json is not None:
        r['response'] = json
    if status is not None:
        r['status'] = status    
    return jsonify(r)

def response_text(text = '', status = None):
    r = {}
    if text is not '':
        r['response'] = text
    if status is not None:
        r['status'] = status    
    return jsonify(r)
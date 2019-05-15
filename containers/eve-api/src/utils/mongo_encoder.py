import datetime
from bson.objectid import ObjectId
from werkzeug import Response
import json
from bson import json_util

def jsonify(data):
    return Response(json.dumps(data, default=json_util.default), mimetype='application/json')
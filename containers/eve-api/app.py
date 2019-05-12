from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_hello_world():
    return jsonify({'message': 'Hello world'})

@app.route('/api/v1/messages', methods=['GET'])
def get_messages():
    return jsonify(['eve','app'],'teste')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
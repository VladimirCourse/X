import os, json

from bottle import route, run, request, Bottle, response

from controllers.chat_controller import ChatController

from helpers.database import Database

chat = ChatController()

def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        response.headers['Content-type'] = 'application/json'
        if request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors

@route('/message', method=['OPTIONS', 'POST'])
@enable_cors
def message():
    postdata = json.load(request.body)['message']
    res = chat.interact(postdata, 'abc')
    return res.dict()

@route('/topic', method=['GET', 'OPTIONS'])
@enable_cors
def topic():
    return Database().get_topic('abc').__dict__

run(host='localhost', port=5000, debug=True)

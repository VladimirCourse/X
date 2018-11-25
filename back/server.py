import os, json

from sys import argv

from bottle import route, run, request, Bottle, response, hook

from controllers.chat_controller import ChatController

from helpers.database import Database

chat = ChatController()

_allow_origin = '*'
_allow_methods = 'PUT, GET, POST, DELETE, OPTIONS'
_allow_headers = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token, X-HTTP-Method-Override'

def enable_corss():
    '''Add headers to enable CORS'''

    response.headers['Access-Control-Allow-Origin'] = _allow_origin
    response.headers['Access-Control-Allow-Methods'] = _allow_methods
    response.headers['Access-Control-Allow-Headers'] = _allow_headers


def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token, X-HTTP-Method-Override'

        response.headers['Content-Type'] = 'application/json'
        if request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors

@route('/message', method=['OPTIONS', 'POST'])
@enable_cors
def message():
    postdata = json.load(request.body)
    res = chat.interact(postdata['message'], 'abc', postdata['user'])
    enable_corss()
    return json.dumps(res.dict())
    
@route('/messages', method=['OPTIONS', 'GET'])
@enable_cors
def messages():
    messages = Database().get_messages('abc')
    res = []
    for msg in messages:
        res.append(msg.dict())
    enable_corss()
    return json.dumps(res)

@route('/topic', method=['GET', 'OPTIONS'])
@enable_cors
def topic():
    enable_corss()
    return json.dumps(Database().get_topic('abc').__dict__)

@route('/flight', method=['GET', 'OPTIONS'])
@enable_cors
def flight():
    res = Database().get_flight('abc')
    enable_corss()
    if res:
        return json.dumps(res.__dict__)

@route('/hotel', method=['GET', 'OPTIONS'])
@enable_cors
def hotel():
    res = Database().get_hotel('abc')
    enable_corss()
    if res:
        return json.dumps(res.__dict__)

@route('/places', method=['OPTIONS', 'GET'])
@enable_cors
def places():
    places = Database().get_places('abc')
    res = []
    for msg in places:
        res.append(msg.__dict__)
    enable_corss()
    return json.dumps(res)

@route('/food', method=['OPTIONS', 'GET'])
@enable_cors
def food():
    food = Database().get_food('abc')
    res = []
    for msg in food:
        res.append(msg.__dict__)
    return json.dumps(res)


run(server='wsgiref', host='0.0.0.0', port=argv[1])


#run(application=APP, host='localhost', port=5000, debug=True)

import os, json

from sys import argv

from bottle import route, run, request, Bottle, response

from controllers.chat_controller import ChatController

from helpers.database import Database

chat = ChatController()

APP = Bottle()

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

@APP.route('/message', method=['OPTIONS', 'POST'])
@enable_cors
def message():
    postdata = json.load(request.body)['message']
    res = chat.interact(postdata, 'abc')
    return json.dumps(res.dict())
    
@APP.route('/messages', method=['OPTIONS', 'GET'])
@enable_cors
def messages():
    messages = Database().get_messages('abc')
    res = []
    for msg in messages:
        res.append(msg.dict())
    return json.dumps(res)

@APP.route('/topic', method=['GET', 'OPTIONS'])
@enable_cors
def topic():
    return json.dumps(Database().get_topic('abc').__dict__)

@APP.route('/flight', method=['GET', 'OPTIONS'])
@enable_cors
def flight():
    res = Database().get_flight('abc')
    if res:
        return json.dumps(res.__dict__)

@APP.route('/hotel', method=['GET', 'OPTIONS'])
@enable_cors
def hotel():
    res = Database().get_hotel('abc')
    if res:
        return json.dumps(res.__dict__)

@APP.route('/places', method=['OPTIONS', 'GET'])
@enable_cors
def places():
    places = Database().get_places('abc')
    res = []
    for msg in places:
        res.append(msg.__dict__)
    return json.dumps(res)

@APP.route('/food', method=['OPTIONS', 'GET'])
@enable_cors
def food():
    food = Database().get_food('abc')
    res = []
    for msg in food:
        res.append(msg.__dict__)
    return json.dumps(res)

HOST = os.environ.get('SERVER_HOST', 'localhost')
try:    
    PORT = int(os.environ.get('SERVER_PORT', '5555'))
except ValueError:
    PORT = 5555

run(application=APP, server='wsgiref', host='0.0.0.0', port=argv[1])


#run(application=APP, host='localhost', port=5000, debug=True)

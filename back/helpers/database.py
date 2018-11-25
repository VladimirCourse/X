from models.topic import Topic
from models.flight import Flight

class Database:
    class __Database:
        def __init__(self):
            self.messages = {}
            self.topics = {}
            self.flights = {}
            self.hotels = {}
            self.places = {}
            self.food = {}

    instance = None
    
    def __init__(self):
        if not Database.instance:
            Database.instance = Database.__Database()

    def flush(self):
        self.instance.messages = {}
        self.instance.topics = {}
        self.instance.flights = {}
        self.instance.hotels = {}
        self.instance.places = {}
        self.instance.food = {}


    def get_messages(self, token):
        if token not in self.instance.messages:
            self.instance.messages[token] = []
        return self.instance.messages[token]

    def add_message(self, token, message):
        if token not in self.instance.messages:
            self.instance.messages[token] = []
        self.instance.messages[token].append(message)

    def get_topic(self, token):
        if token not in self.instance.topics:
            self.instance.topics[token] = Topic()
        return self.instance.topics[token]

    def set_topic(self, token, topic):
        self.instance.topics[token] = topic

    def get_flight(self, token):
        return self.instance.flights.get(token)

    def set_flight(self, token, flight):
        self.instance.flights[token] = flight
  
    def get_hotel(self, token):
        return self.instance.hotels.get(token)

    def set_hotel(self, token, hotel):
        self.instance.hotels[token] = hotel

    def get_places(self, token):
        if token not in self.instance.places:
            self.instance.places[token] = []
        return self.instance.places.get(token)

    def set_places(self, token, places):
        self.instance.places[token] = places

    def get_food(self, token):
        if token not in self.instance.food:
            self.instance.food[token] = []
        return self.instance.food.get(token)

    def set_food(self, token, food):
        self.instance.food[token] = food

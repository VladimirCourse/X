from helpers.luis import Luis
from helpers.data_provider import DataProvider
from helpers.database import Database
from helpers.iata import Iata

from models.answer import Answer

class ChatController:
    def __init__(self):
        self.data = DataProvider()
        self.luis = Luis()
        self.db = Database()

    def save_flight(self, token, flight, dest):
        topic = self.db.get_topic(token)
        topic.topic = 'flight_found'
        topic.origin = 'Moscow'
        topic.destination = dest
        self.db.set_topic(token, topic)
        self.db.set_flight(token, flight)

    def interact(self, msg, token):
        result = self.luis.message(msg)

        self.db.add_message(token, Answer('my_message', msg))

        try:
            if result.score >= 0.5:
                if result.intent == 'Travel.Flight':
                    if len(result.entities) == 0:
                        res = self.data.get_flights('Moscow')[0]
                        self.save_flight(token, res, Iata().get_city_name(res.destination))
                        return Answer('flights_from', data=res)
                    else:
                        res = self.data.get_flights('Moscow', dest=result.entities[0].entity)[0]
                        self.save_flight(token, res, result.entities[0].entity)
                        return Answer('flights_to', data=res)
                elif result.intent == 'Travel.Hotel':
                    topic = self.db.get_topic(token)
                    if topic.destination:
                        res = self.data.get_hotels(topic.destination)[0]
                        
                        topic = self.db.get_topic(token)
                        topic.topic = 'hotel_found'
                        self.db.set_topic(token, topic)
                        self.db.set_hotel(token, res)

                        return Answer('hotel', data=res)
                    else:
                        return Answer('no_topic')
                elif result.intent == 'Travel.Places':
                    topic = self.db.get_topic(token)
                    if topic.destination:
                        res = self.data.get_places(topic.destination)
                        
                        topic = self.db.get_topic(token)
                        topic.topic = 'places_found'
                        self.db.set_topic(token, topic)
                        #self.db.set_hotel(token, res)

                        return Answer('places', data=res)
                    else:
                        return Answer('no_topic')
                else:   
                    return Answer('not_understand')
            else:
                return Answer('not_understand')
        except Exception as e:
            print(e)
            return Answer('not_understand')
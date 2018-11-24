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

    def interact(self, msg, token):
        result = self.luis.message(msg)

        try:
            if result.score >= 0.5:
                if result.intent == 'Travel.Flight':
                    if len(result.entities) == 0:
                        res = self.data.get_flights('Moscow')[0]

                        topic = self.db.get_topic(token)
                        topic.topic = 'flight_found'
                        topic.origin = 'Moscow'
                        topic.destination = Iata().get_city_name(res.destination)
                        self.db.set_topic(token, topic)

                        return Answer('flights_from', data=res)
                    else:
                        res = self.data.get_flights('Moscow', dest=result.entities[0].entity)[0]

                        topic = self.db.get_topic(token)
                        topic.topic = 'flight_found'
                        topic.origin = 'Moscow'
                        topic.destination = result.entities[0].entity
                        self.db.set_topic(token, topic)

                        return Answer('flights_to', data=res)
                else:   
                    return Answer('not_understand')
            else:
                return Answer('not_understand')
        except Exception as e:
            print(e)
            return Answer('not_understand')
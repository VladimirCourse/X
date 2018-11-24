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
        self.poi = ['city center', 'theatre', 'supermarket', 'cinema', 'museum']

    def save_flight(self, token, flight, dest):
        topic = self.db.get_topic(token)
        topic.topic = 'flight_found'
        topic.origin = 'Moscow'
        topic.destination = dest
        self.db.set_topic(token, topic)
        self.db.set_flight(token, flight)

    def magic_sorted(self, coll):
        coll.sort(key=lambda p: p.price)
        return coll[len(coll) // 4]

    def poi_sorted(self, coll, poi):
        coll.sort(key=lambda p: p.price)
        if poi == 'city center':
            #higher price - closer to center lol
            return coll[len(coll) // 2]
        else:
            return coll[len(coll) // (self.poi.index(poi) + 2)] 
            

    def interact(self, msg, token):
        result = self.luis.message(msg)

        self.db.add_message(token, Answer('my_message', msg))

        try:
            if result.score >= 0.5:
                if result.intent == 'Travel.Flight':
                    if len(result.entities) == 0:
                        res = self.data.get_flights('Moscow')
                        res = self.magic_sorted(res)
                        self.save_flight(token, res, Iata().get_city_name(res.destination))
                        return Answer('flights_from', data=res)
                    else:
                        res = self.data.get_flights('Moscow', dest=result.entities[0].entity)
                        res = self.magic_sorted(res)
                        self.save_flight(token, res, result.entities[0].entity)
                        return Answer('flights_to', data=res)
                    
                    self.db.set_places(token, [])
                    self.db.set_hotel(token, None)
                    
                elif result.intent == 'Travel.Hotel':
                    topic = self.db.get_topic(token)
                    if topic.destination:
                        res = self.data.get_hotels(topic.destination)
                        if result.entities[0].entity in self.poi:
                            res = self.poi_sorted(res, result.entities[0].entity)
                        else:
                            res = self.magic_sorted(res)
                            
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
                        res = self.data.get_places(topic.destination)[:5]
                        
                        topic = self.db.get_topic(token)
                        topic.topic = 'places_found'
                        self.db.set_topic(token, topic)
                        self.db.set_places(token, res)

                        return Answer('places', data=res)
                    else:
                        return Answer('no_topic')
                elif result.intent == 'Travel.Price':
                    topic = self.db.get_topic(token)
                    if topic.topic == 'flight_found':
                        res = self.data.get_flights(topic.origin, dest=topic.destination)
                        res.sort(key=lambda p: p.price)
                        self.save_flight(token, res[0], Iata().get_city_name(res[0].destination))
                        return Answer('flights_to', data=res[0])
                    elif topic.topic == 'hotel_found':
                        res = self.data.get_hotels(topic.destination)
                        res.sort(key=lambda p: p.price)
                        self.db.set_hotel(token, res[0])
                        return Answer('hotel', data=res[0])
                    else:
                        return Answer('not_understand')
                elif result.intent == 'Travel.Food':
                    topic = self.db.get_topic(token)
                    if topic.destination:
                        res = self.data.get_food(topic.destination)[:1]
                        
                        topic = self.db.get_topic(token)
                        topic.topic = 'food_found'
                        self.db.set_topic(token, topic)
                        self.db.set_food(token, res)

                        return Answer('food', data=res)
                    else:
                        return Answer('no_topic')
                else:   
                    return Answer('not_understand')
            else:
                return Answer('not_understand')
        except Exception as e:
            print(e)
            return Answer('not_understand')
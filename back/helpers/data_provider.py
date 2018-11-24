import urllib.request
import json, random
import foursquare

from models.flight import Flight
from models.place import Place

from helpers.iata import Iata

class DataProvider:
    
    def __init__(self):
        self.client = foursquare.Foursquare(client_id='TW0KUEAIOA00ZSGKD2O2TVLIWQXWHJY1DPLI5ZFUGVPN1AKR', client_secret='2F2Z40MSGXJDKX0PIDLLU12UDZJ4A1TZWMYICHFUVYQWLD3E')


    def get_flights(self, origin, dest=None):
        code = Iata().get_city_code(origin)
        #url = 'https://api.sandbox.amadeus.com/v1.2/flights/inspiration-search?apikey=r2VHFajVkYBhFLBA3bP4iw25GkXPKuBK&origin={}'.format(code)
        
        if dest:
            destCode = Iata().get_city_code(dest)
            url = 'http://min-prices.aviasales.ru/calendar_preload?origin={}&destination={}&locale=en&currency=eur'.format(code, destCode)
            contents = urllib.request.urlopen(url).read()
            flights = json.loads(contents)['best_prices']
        else:
            url = 'http://map.aviasales.ru/prices.json?origin_iata={}&locale=en&period=2018-12-01:month&currency=eur'.format(code)
            contents = urllib.request.urlopen(url).read()
            flights = json.loads(contents)
        # res = []
        # for result in json.loads(contents)['results']:
        #     res.append(Flight(result))

        res = []
        for result in flights:
            result['origin'] = code
            res.append(Flight(result))

        return res

    def get_hotels(self, origin):
        results = self.client.venues.search(params={'near': origin, 'query': 'hotel', 'categoryId': '4bf58dd8d48988d1fa931735'})['venues']
        res = []
        for result in results:
            res.append(Place(result, 'hotel', random.randint(50, 100)))

        return res

    def get_food(self, origin):
        results = self.client.venues.search(params={'near': origin, 'query': 'hotel', 'categoryId': '4d4b7105d754a06374d81259'})['venues']
        res = []
        for result in results:
            res.append(Place(result, 'food'))

        return res

    def get_places(self, origin):
        results = self.client.venues.search(params={'near': origin, '': 'sight', 'categoryId': '4d4b7104d754a06370d81259'})['venues']
        res = []
        for result in results:
            res.append(Place(result, 'sight'))

        return res
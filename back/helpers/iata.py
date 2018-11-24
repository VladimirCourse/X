import urllib.request
import json
import ssl

class Iata:
    def get_city_code(self, query):
        url = 'https://iatacodes.org/api/v6/autocomplete?api_key=c29b7c79-28fd-43e9-8355-44b4ff008e45&query={}'.format(query)
        context = ssl._create_unverified_context()
        contents = urllib.request.urlopen(url, context=context).read()
        return json.loads(contents)['response']['cities'][0]['code']

    def get_city_name(self, query):
        url = 'https://iatacodes.org/api/v6/autocomplete?api_key=c29b7c79-28fd-43e9-8355-44b4ff008e45&query={}'.format(query)
        context = ssl._create_unverified_context()
        contents = urllib.request.urlopen(url, context=context).read()
        return json.loads(contents)['response']['cities'][0]['name']
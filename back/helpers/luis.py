import requests

from models.luis_result import LuisResult

class Luis:
    def __init__(self):
        pass

    def message(self, msg):
        headers = {
            'Ocp-Apim-Subscription-Key': 'a3b758516f9240b5aa5a04e4efd45080',
        }
        params = { 
            'q': msg
        }

        try:
           res = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/d982780f-8774-4883-99e2-e3b039f0b5c6', headers=headers, params=params)
           print(res.json())
           return LuisResult(res.json())
        except Exception as e:
            print(e)


    
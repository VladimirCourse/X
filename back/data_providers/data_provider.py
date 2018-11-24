import urllib.request

class DataProvider:

    def get_avia_prices(self, origin):
        url = 'http://map.aviasales.ru/prcies.json?origin_data={}&locale=en'.format(origin)
        contents = urllib.request.urlopen(url).read()
        print(contents)
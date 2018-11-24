class Flight:
    def __init__(self, data):
        self.destination = data.get('destination')
        self.origin = data.get('origin')
        self.depart_date = data.get('depart_date')
        #self.depart_date = data.get('departure_date')
        self.price = data.get('value')
        self.gate = data.get('gate')
        #self.price = data.get('price')
        #self.currency = data.get('currency')


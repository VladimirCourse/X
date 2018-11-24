class Place:
    def __init__(self, data, category):
        self.name = data.get('name')
        self.address = ','.join(data.get('location').get('formattedAddress'))
        self.lat = data.get('location').get('lat')
        self.lng = data.get('location').get('lng')
        self.category = category
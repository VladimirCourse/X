class Answer:
    def __init__(self, messageType, message=None,  data=None):
        self.messageType = messageType
        self.message = message
        self.data = data

    def dict(self):
        res = {
            'messageType': self.messageType,
            'message': self.message
        }

        if self.messageType == 'flights_from' or self.messageType == 'flights_to':
            res['data'] = self.data.__dict__
        elif self.messageType =='hotel':
            res['data'] = self.data.__dict__
        elif self.messageType == 'places':
            tmp = []
            for place in self.data:
                tmp.append(place.__dict__)
            res['data'] = tmp
        return res
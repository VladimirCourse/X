class Answer:
    def __init__(self, messageType, message=None, data=None, user=None, createdAt=None):
        self.messageType = messageType
        self.message = message
        self.data = data
        self.user = user
        self.createdAt = createdAt

    def dict(self):
        res = {
            'messageType': self.messageType,
            'message': self.message,
            'user': self.user,
            'createdAt': self.createdAt
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
        elif self.messageType == 'food':
            tmp = []
            for food in self.data:
                tmp.append(food.__dict__)
            res['data'] = tmp
        return res
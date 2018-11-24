from models.topic import Topic

class Database:
    class __Database:
        def __init__(self):
            self.messages = {}
            self.topics = {}
    
    instance = None
    
    def __init__(self):
        if not Database.instance:
            Database.instance = Database.__Database()

    def get_messages(self, token):
        if token not in self.instance.messages:
            self.instance.messages[token] = []
        return self.instance.messages[token]

    def add_message(self, token, message):
        if token not in self.instance.messages:
            self.instance.messages[token] = []
        self.instance.messages[token].append(message)

    def get_topic(self, token):
        if token not in self.instance.topics:
            self.instance.topics[token] = Topic()
        return self.instance.topics[token]

    def set_topic(self, token, topic):
        self.instance.topics[token] = topic

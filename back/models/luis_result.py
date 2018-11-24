class LuisEntity:
    def __init__(self, entity, entityType):
        self.entity = entity
        self.enttityType = entityType

class LuisResult:
    def __init__(self, data):
        self.intent = data.get('topScoringIntent').get('intent')
        self.score = data.get('topScoringIntent').get('score')
        self.entities = []

        for ent in data.get('entities'):
            self.entities.append(LuisEntity(ent.get('entity'), ent.get('type')))
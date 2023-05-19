class EntityHandler:
    entityArray = []
    def __init__(self):
        pass

    def addEntity(self,entity):
        self.entityArray.append(entity)
        pass

    def updateEntities(self):
        for entity in self.entityArray:
            entity.update()
            entity.draw()
        pass
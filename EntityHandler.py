class EntityHandler:
    entityArray = []
    def __init__(self,entityArray = []):

        self.entityArray = entityArray

    def addEntity(self,entity):
        self.entityArray.append(entity)
        pass

    def updateEntities(self,dt):
        for entity in self.entityArray:
            entity.update(dt)
            entity.updateSprite()

    def resetEntities(self,dt):
        for entity in self.entityArray:
            entity.resetEntity(dt)
        
            
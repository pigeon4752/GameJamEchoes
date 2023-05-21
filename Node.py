
class Node:
    def __init__(self, position,key, endPosition, count= 0, parentNode = None):
        self.coordinates = position
        if parentNode != None:
            self.count = parentNode.count
        else:
           self.count = count 
        self.key = key
        self.heuristic = self.generateHeuristic(position,endPosition, count)
        self.parentNode = parentNode
        
        #self.key = self.calculateKey(max)

    def generateHeuristic(self,startingPosition, endingPosition,count):
        return((startingPosition.x-endingPosition.x)**2+(startingPosition.y-endingPosition.y)**2+count)
    def calculateKey(self,max):
        return(self.coordinates.x*max+self.coordinates.y)


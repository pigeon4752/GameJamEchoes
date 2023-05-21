from Bot import Bot
from gun import Gun
import random
from Vector import Vector
from Node import Node
import numpy as np
import math
import threading
class Goblin(Bot):
    def __init__(self,screen,background,rendered = False):
        super().__init__(screen,background)
        gobbo = threading.Thread(target=self.run, args=())
        self.brain = Pathing(background.map)
        
        gobbo.start()

    def run(self):
        while self.health>0:
            #print(self.position.x)
            #self.changeXVelocity(random.randint(-10,10))
            #self.changeYVelocity(random.randint(-5,5))
            
            self.brain.calculatePath(self.coordinates)
        time.sleep(10000)

class Pathing:
    def __init__(self,grid):
        self.MAX = len(grid)**2
        self.grid = grid

    def calculatePath(self,startingPosition):
        
        
        grid = np.copy(self.grid)
        
        
        
        openSet,endPosition = self.getEndPosition(startingPosition,grid)
        count = 0
        closedSet = {}
        while openSet: 
            
            for node in openSet:
                currentNode = min(openSet, key=lambda node: node.heuristic)


                if currentNode.key == self.calculateKey(endPosition.x,endPosition.y):
                    print(1)
                else:
                    
                    openSet.remove(currentNode)
                    closedSet[currentNode.key] = currentNode
                    neighbours = self.generateNeighbours(currentNode.coordinates)
                    for neighbour in neighbours:
                        key = self.calculateKey(neighbour.x, neighbour.y)
                        if key in closedSet:
                            pass
                        elif key in openSet:
                            if currentNode.count<= openSet[key].count:
                                openSet[key].parentNode = currentNode
                        else:
                            neighbour = Node(neighbour,self.calculateKey(neighbour.x, neighbour.y),endPosition,parentNode= currentNode)
                            openSet.append(neighbour)
                            #closedSet[]

        #print("pi")


                
                #print(neighbours)


    def getEndPosition(self,startingPosition,grid):
        for x in range(0,len(self.grid)):
            for y in range(0,len(self.grid)):
                    if grid[x][y] == 2:
                        endingPosition = Vector(x,y)
                        openSet = [Node(startingPosition,self.calculateKey(startingPosition.x, startingPosition.y),endingPosition)]
                        return(openSet,endingPosition)
        return([],())

    def calculateKey(self,x,y):
        return(x*self.MAX+y)

        


    def generateNeighbours(self,coordinates):
        neighbours = []
        for x in [-1,1]:
            for y in [-1,1]:
                if self.grid[x+coordinates.x][y+coordinates.y] != 0:
                    neighbours.append(Vector(x+coordinates.x,y+coordinates.y))
        return neighbours

    
        
    #neighbors = generate_neighbors(current_node, grid)
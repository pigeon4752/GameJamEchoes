import pygame
import numpy as np
from Tile import tile
from PIL import Image
import math
import time
import random

class Background:
    
    def __init__(self,screen,SCREEN_WIDTH,SCREEN_HEIGHT):
        self.screen = screen
        self.tileArray = []
        self.fogSurfaces = []
        self.screenHeight = SCREEN_HEIGHT
        self.screenWidth = SCREEN_WIDTH
        self.hashMap = {}
        self.createNewBackground()
        

    
    def addLight(self, x, y, size, intensity):
        radius = size / 2
        center = (x + radius, y + radius)
        
        # Iterate over the array of tiles
        for tile in self.tileArray:
            # Get the center of the tile's rect
            tile_center = tile.rect.center
            
            # Calculate the distance between the tile's center and the circular area's center
            distance_x = abs(tile_center[0] - center[0])
            distance_y = abs(tile_center[1] - center[1])
            
            # Check if the tile is inside the circular area
            if distance_x <= radius + tile.rect.width / 2 and distance_y <= radius + tile.rect.height / 2:
                # Increase the alpha value by the specified intensity
                self.increaseTileBrightness(tile, intensity)
    
    
   
        
        
    


    def createNewBackground(self):
        #rectangle = pygame.Rect(100, self.screen.get_height() - 100, self.screen.get_width()-200, 100)
        #img = Image.open('file.bmp')
        self.map = np.array(Image.open('oldmap32.bmp'))
        
        self.dimension = int(math.sqrt(self.map.size))
        
        fogSurface = pygame.Surface((self.screenWidth, self.screenHeight), pygame.SRCALPHA)

        self.tileSize = self.screen.get_height()/self.dimension
        
        for x in range(int (self.map.size/self.dimension)):
            for y in range(int (self.map.size/self.dimension)):
                tileValue = self.map[x][y]

                
                if tileValue == 0:
                    tileRect = pygame.Rect(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize)
                     
                    randomNum = random.randint(0,100)
                    randomNum2 = random.randint(0,100)
                    if randomNum2<97:
                        if(randomNum<=60):
                            cobble = pygame.image.load("cobble.png")
                        elif(randomNum<=79):
                            cobble = pygame.image.load("cobble2.png")
                        elif(randomNum<=83):
                            cobble = pygame.image.load("cobble3.png")
                        elif(randomNum<=88):
                            cobble = pygame.image.load("cobble4.png")
                        else:
                            cobble = pygame.image.load("cobble5.png")
                        tileObject = tile(cobble,tileRect,255,x,y)
                        
                    else:
                        if (randomNum<= 50):
                            cobble = pygame.image.load("lava.png")
                            tileObject = tile(cobble,tileRect,255,x,y,damaging =True,damageRate=100)
                        else:
                            cobble = pygame.image.load("goblinPit.png")
                            tileObject = tile(cobble,tileRect,255,x,y,damaging =True,damageRate=10)


                    
                    #pygame.draw.rect(self.screen, (0, 0, 0), tileRect)
                    #self.screen.blit(cobble, tileRect.topleft)
                    self.tileArray.append(tileObject)
                    self.hashMap[tileObject.key] = tileObject
                    
        
        
       
    
    def updateMap(self):
        for tileObject in self.tileArray: 
            self.decreaseTileBrightness(tileObject,2)
            if tileObject.glows:
                self.addLight(tileObject.x, tileObject.y, 50, 50)
            tileObject.image.set_alpha(tileObject.shadow)
            if (tileObject.shadow!=0):
                self.screen.blit(tileObject.image, tileObject.rect.topleft)


    def lightAllTiles(self):
        for tileObject in self.tileArray:
            self.increaseTileBrightness(tileObject,20)
            self.increaseTileBrightness(tileObject,20)

    def modifyCoordinateMap(self,oldCoordinates,newCoordinates, representation):
        #print(self.map[int(oldCoordinates.x),int(oldCoordinates.y)])
        #if self.map[int(newCoordinates.x)][int(newCoordinates.y)] != 0: 
        if oldCoordinates.x != newCoordinates.x or oldCoordinates.y != newCoordinates.y:
            self.map[oldCoordinates.x-1,oldCoordinates.y-1] = 1
            self.map[newCoordinates.x-1,newCoordinates.y-1] = representation
       
        #print(self.map[int(oldCoordinates.x),int(oldCoordinates.y)])
    
    def getTile(self,x,y):
        return(self.hashMap[x,"_",y])

    def getTilesAround(self,position):
        arr = []
        
        #for row in self.map:
        #jjjjjjjjjjjjjjjjjjjj    print(row)
        #print(position.x,"X")
        #print(position.y,"Y")
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                
                if (-1<position.x+x<32) and (-1<position.y+y<32):
                    if self.map[position.x+x,position.y+y] == 0 :
                        arr.append(self.getTile(position.x+x,position.y+y))  

        
        return(arr)

                

    

    def printMap(self):
        print("\n")
        for row in self.map:
            print(row)


    def modifyCoordinateMap(self,oldCoordinates,newCoordinates, representation):
        #print(self.map[int(oldCoordinates.x),int(oldCoordinates.y)])
        #if self.map[int(newCoordinates.x)][int(newCoordinates.y)] != 0: 
        if oldCoordinates.x != newCoordinates.x or oldCoordinates.y != newCoordinates.y:

            self.map[oldCoordinates.x-1,oldCoordinates.y-1] = 1
            self.map[newCoordinates.x-1,newCoordinates.y-1] = representation
       
        #print(self.map[int(oldCoordinates.x),int(oldCoordinates.y)])
    
    def getTile(self,x,y):
        return(self.hashMap[x,"_",y])

    def getTilesAround(self,position):
        arr = []
        
        #for row in self.map:
        #jjjjjjjjjjjjjjjjjjjj    print(row)
        #print(position.x,"X")
        #print(position.y,"Y")
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                
                if (-1<position.x+x<32) and (-1<position.y+y<32):
                    if self.map[position.x+x,position.y+y] == 0 :
                        arr.append(self.getTile(position.x+x,position.y+y))  

        
        return(arr)

                

    

    def printMap(self):
        print("\n")
        for row in self.map:
            print(row)


    def decreaseBrightness(self):
        for tileObject in self.tileArray:
            self.decreaseTileBrightness(tileObject,1)
            

    def increaseTileBrightness(self,tile,amount):
        tile.shadow+=amount
        if tile.shadow>255:
            tile.shadow=255
    
    def decreaseTileBrightness(self,tile,amount):
        if not tile.glows:
            tile.shadow-=amount
            if tile.shadow<0:
                tile.shadow=0
            
    def revertBrightness(self):
        for tileObject in self.tileArray:
            self.decreaseTileBrightness(tileObject)
        # time.sleep(0.05)  # Delay of 0.05 seconds (adjust as needed)
            
    
    def addFog(self):
        for fog in self.fogSurfaces:
            self.screen.blit(fog,(0,0))
        pass

    def getTileArray(self):
        return(self.tileArray)

    
       

    def isGrounded(self):
        for rect in self.rectArray:
            print(rect[0].bottom)
            

    def checkGrounded(self, rectangle):
        pass

    def handlePlayerCollision(self,player,previousX,previousY):
        playerTop = player.position.y
        playerRight = player.position.x+player.playerRectangle.width
        playerBottom = player.position.y+player.playerRectangle.height
        playerLeft = player.position.x
        #tiles = self.getTilesAround(player.coordinates)
        tiles = self.getTileArray()
        for tile in tiles:
            rect=tile.rect
            if playerRight > rect.left and playerLeft < rect.right:
                if playerBottom > rect.top and playerTop < rect.bottom:
                    # Player is within the vertical bounds of the current platform
                    # Player is within the horizontal bounds of the current platform
                    if previousX + player.playerRectangle.width <= rect.left:
                            # Player was to the left of the platform in the previous frame
                            if playerRight >= rect.left and playerBottom>rect.top+(rect.height/4):  # Added check
                                player.position.x = rect.left - player.playerRectangle.width
                                player.velocity.x = 0
                    elif previousX >= rect.right:
                            # Player was to the right of the platform in the previous frame
                            if playerLeft <= rect.right and playerBottom>rect.top+(rect.height/4):  # Added check
                                player.position.x = rect.right
                                player.velocity.x = 0
                    elif previousY + player.playerRectangle.height <= rect.top:
                        # Player was above the platform in the previous frame
                        if tile.damaging:
                            player.takeDamage(tile.damageRate)
                        if playerBottom > rect.top:  # Added check
                            player.position.y = rect.top - player.playerRectangle.height
                            player.velocity.y = 0
                    elif previousY >= rect.bottom:
                        # Player was below the platform in the previous frame
                        if playerTop < rect.bottom+2:  # Added check
                            player.position.y = rect.bottom+2
                            player.velocity.y = -0.01
                    
                    else:
                         player.position.y = rect.top-player.playerRectangle.height
                         player.velocity.y = 0

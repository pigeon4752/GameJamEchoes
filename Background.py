import pygame
import numpy as np
from Tile import tile
from PIL import Image
import math
import time

class Background:
    
    def __init__(self,screen,SCREEN_WIDTH,SCREEN_HEIGHT):
        self.screen = screen
        self.tileArray = []
        self.polyArray = []
        self.fogSurfaces = []
        self.screenHeight = SCREEN_HEIGHT
        self.screenWidth = SCREEN_WIDTH
        self.hashMap = {}
        #fogSurface = pygame.Surface((self.screenWidth, self.screenHeight), pygame.SRCALPHA)
        #fogSurface.fill((0, 0, 0, 100))
        
        
        #self.fogSurfaces.append(fogSurface)
        self.createNewBackground()
        
    
    def addLight(self,x,y,size):
        radius = size / 2
        center = (x + radius, y + radius)
        
        # Iterate over the array of tiles
        for tile in self.tileArray:
            # Get the center of the tile's rect
            tile_center = tile.rect.center
            
            # Calculate the distance between the tile's center and the circular area's center
            distance = math.sqrt((tile_center[0] - center[0]) ** 2 + (tile_center[1] - center[1]) ** 2)
            
            # Check if the tile is inside the circular area
            if distance <= radius:
                # Increase the alpha value by 100
                tile.shadow -= 100
        pass
   
        
        
    


    def createNewBackground(self):
        #rectangle = pygame.Rect(100, self.screen.get_height() - 100, self.screen.get_width()-200, 100)
        
        #img = Image.open('file.bmp')
        self.map = np.array(Image.open('map.bmp'))
        dimension = int(math.sqrt(self.map.size))
        cobble = pygame.image.load("cobble.png")
        fogSurface = pygame.Surface((self.screenWidth, self.screenHeight), pygame.SRCALPHA)

        tileSize = self.screen.get_height()/dimension
        
        for x in range(int (self.map.size/dimension)):
            for y in range(int (self.map.size/dimension)):
                tileValue = self.map[x][y]
                
                if tileValue == 0:
                    tileRect = pygame.Rect(x * tileSize, y * tileSize, tileSize, tileSize)
                    tileObject = tile(cobble,tileRect,255,x,y)
                    #pygame.draw.rect(self.screen, (0, 0, 0), tileRect)
                    #self.screen.blit(cobble, tileRect.topleft)
                    self.tileArray.append(tileObject)
                    self.hashMap[tileObject.key] = tileObject
                    
        
        
       
    
    def updateMap(self):
        for tileObject in self.tileArray: 
            self.decreaseTileBrightness(tileObject)
            tileObject.image.set_alpha(tileObject.shadow)
            if (tileObject.shadow!=0):
                self.screen.blit(tileObject.image, tileObject.rect.topleft)


    def lightAllTiles(self):
        for tileObject in self.tileArray:
            self.increaseTileBrightness(tileObject)
            self.increaseTileBrightness(tileObject)

    def decreaseBrightness(self):
        for tileObject in self.tileArray:
            self.decreaseTileBrightness(tileObject)
            

    def increaseTileBrightness(self,tile):
        tile.shadow+=20
        if tile.shadow>255:
            tile.shadow=255
    
    def decreaseTileBrightness(self,tile):
        tile.shadow-=20
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

        for tile in self.tileArray:
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

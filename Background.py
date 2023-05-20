import pygame
import numpy as np
from Tile import tile
from PIL import Image
import math

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
        fogSurface = pygame.Surface((self.screenWidth, self.screenHeight), pygame.SRCALPHA)
        for tileObject in self.tileArray: 
            #pygame.draw.rect(self.screen,"black",rect[1])
            
            if (tileObject.shadow!=255):
                self.screen.blit(tileObject.image, tileObject.rect.topleft)
                fogSurface.fill((0, 0, 0, tileObject.shadow))
                self.screen.blit(fogSurface,(tileObject.rect.topleft),tileObject.rect)

    def decreaseBrightness(self):
        for tileObject in self.tileArray:
            if tileObject.shadow>10:
                tileObject.shadow-=10
            else:
                tileObject.shadow = 0
            

            
    
    def addFog(self):
        for fog in self.fogSurfaces:
            self.screen.blit(fog,(0,0))
        pass
       

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

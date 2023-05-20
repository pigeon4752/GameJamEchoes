import pygame
import numpy as np
from PIL import Image
class Background:
    
    def __init__(self,screen,SCREEN_WIDTH,SCREEN_HEIGHT):
        self.screen = screen
        self.rectArray = []
        self.polyArray = []
        self.fogSurfaces = []
        self.screenHeight = SCREEN_HEIGHT
        self.screenWidth = SCREEN_WIDTH
        #fogSurface = pygame.Surface((self.screenWidth, self.screenHeight), pygame.SRCALPHA)
        #fogSurface.fill((0, 0, 0, 100))
        
        
        #self.fogSurfaces.append(fogSurface)
        self.createNewBackground()
        
        
        
        
    
    def createNewBackground(self):
        #rectangle = pygame.Rect(100, self.screen.get_height() - 100, self.screen.get_width()-200, 100)
        
        #img = Image.open('file.bmp')
        self.map = np.array(Image.open('map.bmp'))
        cobble = pygame.image.load("cobble.png")
        tileSize = self.screen.get_height()/32
        for y in range(int (self.map.size/32)):
            for x in range(int (self.map.size/32)):
                tileValue = self.map[y][x]
                tileRect = pygame.Rect(x * tileSize, y * tileSize, tileSize, tileSize)
                if tileValue == 0:
                    pygame.draw.rect(self.screen, (0, 0, 0), tileRect)
                    self.screen.blit(cobble, tileRect.topleft)
                    self.rectArray.append((cobble,tileRect,255))
                #elif tile_value == 1:
                    #pygame.draw.rect(self.screen, (255, 0, 0), tile_rect,255)
                    #self.rectArray.append(("white",tile_rect))
                    
        
        
       
    
    def updateMap(self):
        for rect in self.rectArray: 
            pygame.draw.rect(self.screen,"black",rect[1])
            self.screen.blit(rect[0], rect[1].topleft)
            
        #fog_rect = pygame.Rect(100, 100, 200, 200)
        #fog_surface.set_alpha(100, fog_rect)

   

    def addBigFog(self):
        fogSurface = pygame.Surface((self.screenWidth, self.screenHeight), pygame.SRCALPHA)
        fogSurface.fill((0, 0, 0, 255))
        self.screen.blit(fogSurface,(0,0))

    
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

        for rect in self.rectArray:
            if playerRight > rect[1].left and playerLeft < rect[1].right:
                # Player is within the horizontal bounds of the current platform
                if previousY + player.playerRectangle.height <= rect[1].top:
                    # Player was above the platform in the previous frame
                    if playerBottom > rect[1].top:  # Added check
                        player.position.y = rect[1].top - player.playerRectangle.height
                        player.velocity.y = 0
                elif previousY >= rect[1].top + rect[1].height:
                    # Player was below the platform in the previous frame
                    if playerTop < rect[1].bottom:  # Added check
                        player.position.y = rect[1].top + rect[1].height
                        player.velocity.y = 0

            if playerBottom > rect[1].top and playerTop < rect[1].bottom:
                # Player is within the vertical bounds of the current platform
                if previousX + player.playerRectangle.width <= rect[1].left:
                    # Player was to the left of the platform in the previous frame
                    if playerRight > rect[1].left:  # Added check
                        player.position.x = rect[1].left - player.playerRectangle.width
                        player.velocity.x = 0
                elif previousX >= rect[1].right:
                    # Player was to the right of the platform in the previous frame
                    if playerLeft < rect[1].right:  # Added check
                        player.position.x = rect[1].right
                        player.velocity.x = 0

                    


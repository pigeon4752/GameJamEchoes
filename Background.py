import pygame
import numpy as np
from PIL import Image
class Background:
    
    def __init__(self,screen):
        self.screen = screen
        self.rectArray = []
        self.polyArray = []
        self.createNewBackground()
        
    
    def createNewBackground(self):
        rectangle = pygame.Rect(0, self.screen.get_height() - 100, self.screen.get_width(), 100)
        
        #img = Image.open('file.bmp')
        img = np.array(Image.open('untitle.bmp'))
        print(img)
        
        self.rectArray.append(("blue",rectangle))
       
    
    def updatePosition(self):
        for y in range(map_height):
            for x in range(map_width):
                tile_value = map_data[y][x]
                tile_rect = pygame.Rect(x * tile_width, y * tile_height, tile_width, tile_height)

                if tile_value == 0:
                    pygame.draw.rect(screen, (0, 0, 0), tile_rect)  # Draw an empty tile
                elif tile_value == 1:
                    pygame.draw.rect(screen, (255, 0, 0), tile_rect)  # Draw a wall tile
        for rect in self.rectArray:
            pygame.draw.rect(self.screen,rect[0],rect[1])
       

    def isGrounded(self):
        for rect in self.rectArray:
            print(rect[0].bottom)

    def checkGrounded(self, rectangle):
        pass
            


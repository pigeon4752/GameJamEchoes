import pygame
class Background:
    
    def __init__(self,screen):
        self.screen = screen
        self.rectArray = []
        self.createNewBackground()
        
    
    def createNewBackground(self):
        rectangle = pygame.Rect(0, self.screen.get_height() - 100, self.screen.get_width(), 100)
        
        self.rectArray.append(("blue",rectangle))
    
    def updatePosition(self):
        for rect in self.rectArray:
            pygame.draw.rect(self.screen,rect[0],rect[1])

    def isGrounded(self):
        for rect in self.rectArray:
            print(rect[0].bottom)

    def checkGrounded(self, rectangle):
        pass
            


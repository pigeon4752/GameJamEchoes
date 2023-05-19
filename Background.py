import pygame
class Background:
    rectArray  = []
    def __init__(self,screen):
        self.screen = screen
        self.createNewBackground()
    
    def createNewBackground(self):
        pygame.draw.line(self.screen,"blue",pygame.Vector2(0,self.screen.get_height()) ,pygame.Vector2(self.screen.get_width(), self.screen.get_height()),100)
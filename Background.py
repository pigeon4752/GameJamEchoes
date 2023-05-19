import pygame
import random as Random
class Background:
    
    def __init__(self,screen):
        self.screen = screen
        self.rectArray = []
        self.createNewBackground()
        
    
    def createNewBackground(self):
        rectCount = 10
        colourDict = {0:"blue",1:"red",2:"green"}
        bottomWidth = 10
        rectangle = pygame.Rect(0, self.screen.get_height() - bottomWidth, self.screen.get_width(), bottomWidth)
        
        while (rectCount>0):
            ledgeLeft = 0
            
            rectangle = pygame.Rect(Random.randint(0,self.screen.get_width()-Random.randint(0,self.screen.get_height()/2)), Random.randint(0,self.screen.get_height() - bottomWidth), self.screen.get_width(), bottomWidth)
            self.rectArray.append((colourDict[Random.randint(0,2)],rectangle))
            
            rectCount-=1
            
        
        
        
    
    def updatePosition(self):
        for rect in self.rectArray:
            pygame.draw.rect(self.screen,rect[0],rect[1])

    def isGrounded(self,rectangle):
        for rect in self.rectArray:
            if rectangle.bottom <= rect[1].top and rectangle.left>rect[1].left and rectangle.right<rect[1].right:#
                print("Pi")
                return(true)


    
            


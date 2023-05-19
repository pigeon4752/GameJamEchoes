import pygame
import random as Random
class Background:
    
    def __init__(self,screen):
        self.screen = screen
        self.rectArray = []
        self.createNewBackground()
        
    
    def createNewBackground(self):
        rectCount = 0
        colourDict = {0:"blue",1:"red",2:"green"}
        bottomWidth = 50
        rectangle = pygame.Rect(0, self.screen.get_height() - bottomWidth, self.screen.get_width(), bottomWidth)
        self.rectArray.append((colourDict[Random.randint(0,2)],rectangle))
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
            
            print(rectangle.bottom)
            print(rect[1].top)
            if rectangle.colliderect(rect[1]) and rectangle.bottom >= rect[1].bottom: #and (rect[1].left<rectangle.centrex<=rect[1].right):#
               
                return True


    
            


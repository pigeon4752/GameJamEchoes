import pygame
import Background as background
class Sprite:
    
    

    def __init__(self,screen,background,width=10,size= 10,colour="red"):
        self.background = background
        self.screen = screen
        self.position = pygame.Vector2(0,0)
        self.velocity = pygame.Vector2(0,0)
        self.playerRectangle = pygame.Rect(self.position.x,self.position.y,width,size)


    def updatePosition(self):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

        self.playerRectangle.move(self.position.x,self.position.y)
    
    def incrementXVelocity(self,increment):
        self.velocity.x += increment

    def incrementYVelocity(self,increment):
        self.velocity.y += increment
    
    def isGrounded():
        return(self.background.checkGrounded(this))
        


        

        


import pygame
import Background as background

class Sprite:

    position = pygame.Vector2(0,0)
    velocity = pygame.Vector2(0,0)
    MAX_VELOCITY = 30
    

    def __init__(self,screen,background,width=25,size= 25,colour="red"):
        self.background = background
        self.screen = screen
        self.position = pygame.Vector2(0,0)
        self.velocity = pygame.Vector2(0,0)
        self.playerRectangle = pygame.Rect(self.position.x,self.position.y,width,size)
        self.colour = colour
        self.isGrounded()

    def updatePosition(self):
        if (0 > (self.position.x + self.velocity.x)):
            self.position.x = 0
            self.velocity.x = 0
        elif (self.position.x+self.playerRectangle.width + self.velocity.x) > 1000:
            self.position.x=1000-self.playerRectangle.width
            self.velocity.x=0         
        else:
            self.position.x+=self.velocity.x
        if (0 > (self.position.y + self.velocity.y)):
            self.position.y=0
            self.velocity.y=0
        elif (self.position.y+self.playerRectangle.height + self.velocity.y)>600:     
            self.position.y=600-self.playerRectangle.height
            self.velocity.y=0
        else:
            self.position.y+=self.velocity.y

    
    def changeXVelocity(self,increment):
            if self.velocity.x+increment>self.MAX_VELOCITY:
                self.velocity.x=self.MAX_VELOCITY
            else:
                self.velocity.x += increment

    def changeYVelocity(self,increment):
            if self.velocity.y+increment>self.MAX_VELOCITY:
                self.velocity.y=self.MAX_VELOCITY
            else:
                self.velocity.y += increment
    
    def isGrounded(self):
        return(self.background.checkGrounded(self.playerRectangle))
    
    def update(self):
        self.updatePosition()
        self.playerRectangle.topleft = (self.position.x,self.position.y)

    def draw(self):
        pygame.draw.rect(self.screen,self.colour,self.playerRectangle)
        pass
        


        

        


import pygame
import Background as background
from projectiles import Projectile
from gun import Gun

class Sprite:

    position = pygame.Vector2(0,0)
    velocity = pygame.Vector2(0,0)
    MAX_Y_VELOCITY = 30
    MAX_X_VELOCITY = 10
    projectiles = []
    

    def __init__(self,screen,background,width=25,size= 25,colour="red"):
        self.background = background
        self.screen = screen
        self.position = pygame.Vector2(0,0)
        self.velocity = pygame.Vector2(0,0)
        self.playerRectangle = pygame.Rect(self.position.x,self.position.y,width,size)
        self.colour = colour
        self.isGrounded()
        self.gun = Gun(self.playerRectangle)

    def updatePosition(self):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

        # self.playerRectangle.move(self.position.x,self.position.y)
    
    def changeXVelocity(self,increment):
            if self.velocity.x+increment>self.MAX_X_VELOCITY:
                self.velocity.x=self.MAX_X_VELOCITY
            else:
                self.velocity.x += increment

    def changeYVelocity(self,increment):
            if self.velocity.y+increment>self.MAX_Y_VELOCITY:
                self.velocity.y=self.MAX_Y_VELOCITY
            else:
                self.velocity.y += increment
    
    def isGrounded(self):
        return(self.background.checkGrounded(self.playerRectangle))
    
    def update(self,dt):
        self.updatePosition(dt)
        self.playerRectangle.topleft = (self.position.x,self.position.y)

    def draw(self):
        pygame.draw.rect(self.screen,self.colour,self.playerRectangle)
        # draw all users projectiles
        for projectile in self.projectiles:
            pass
        pass
    
    def fire(self, angle):
        self.gun.fire_gun(angle)
        pass
        

        


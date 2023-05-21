import pygame
import Background as background
import math
from gun import Gun
from Vector import Vector

class Sprite:

    position = pygame.Vector2(0,0)
    velocity = pygame.Vector2(0,0)
    MAX_Y_VELOCITY = 21
    MAX_X_VELOCITY = 8
    
    gravity = 1
    def __init__(self,screen,background,width=24,size= 24,colour="red",spriteImage = "player.png",rendered = False,health = 100):
        self.background = background
        self.screen = screen
        self.spriteImage =  pygame.image.load(spriteImage)
        self.position = pygame.Vector2(400,100)
        self.coordinates = self.calculateCoordinates(self.position.x, self.position.y)
        self.velocity = pygame.Vector2(0,0)
        self.playerRectangle = pygame.Rect(self.position.x,self.position.y,width,size)
        self.colour = colour
        self.isGrounded()
        self.rendered = rendered
        self.health = health
        # self.gun = Gun(self.playerRectangle)

    def updatePosition(self,dt):
        xVel = self.velocity.x*dt
        yVel = self.velocity.y*dt
        if self.velocity.x>0:
            self.velocity.x = self.velocity.x-0.8
            if self.velocity.x < 0:
                self.velocity.x=0
        else:
            self.velocity.x = self.velocity.x+0.8
            if self.velocity.x > 0:
                self.velocity.x=0
        
        if self.velocity.y>0:
            self.velocity.y = self.velocity.y-0.01
            if self.velocity.y < 0.001:
                self.velocity.y=0
        else:
            self.velocity.y = self.velocity.y+0.01
            if self.velocity.y > -0.001:
                self.velocity.y=0

        if (0 > (self.position.x + xVel)):
            self.position.x = 0
            self.velocity.x = 0
        elif (self.position.x+self.playerRectangle.width + xVel) > 800:
            self.position.x=800-self.playerRectangle.width
            self.velocity.x=0         
        else:
            if(xVel>self.MAX_X_VELOCITY):
                xVel=self.MAX_X_VELOCITY
            elif(xVel<0-self.MAX_X_VELOCITY):
                xVel = 0-self.MAX_X_VELOCITY
            self.position.x+=xVel
        if (0 > (self.position.y + yVel)):
            self.position.y=0
            self.velocity.y=0
        elif (self.position.y+self.playerRectangle.height + yVel)>800:     
            self.position.y=800-self.playerRectangle.height
            self.velocity.y=0
        else:
            if(yVel>self.MAX_Y_VELOCITY):
                yVel=self.MAX_Y_VELOCITY
            elif(yVel<0-self.MAX_Y_VELOCITY):
                yVel = 0-self.MAX_Y_VELOCITY
            self.position.y+=yVel

        self.background.handlePlayerCollision(self,self.position.x-xVel,self.position.y-yVel)

    
    def changeXVelocity(self,increment):
            if self.velocity.x+increment>self.MAX_X_VELOCITY:
                self.velocity.x=self.MAX_X_VELOCITY
            elif self.velocity.x+increment<0-self.MAX_X_VELOCITY:
                self.velocity.x=0-self.MAX_X_VELOCITY
            else:
                self.velocity.x += increment

    def changeYVelocity(self,increment):
            if self.velocity.y+increment>self.MAX_Y_VELOCITY:
                self.velocity.y=self.MAX_Y_VELOCITY
            elif self.velocity.y+increment<0-self.MAX_Y_VELOCITY:
                self.velocity.y=0-self.MAX_Y_VELOCITY
            else:
                self.velocity.y += increment
    
    def isGrounded(self):
        return(self.background.checkGrounded(self.playerRectangle))

    def calculateCoordinates(self,x,y):
        return(Vector(int(self.position.x/self.background.tileSize),round(self.position.y/self.background.tileSize)))
    
    def update(self,dt):
        self.updatePosition(dt)
        
        #print(self.coordinates)
        self.playerRectangle.topleft = (self.position.x,self.position.y)
    
    def updateSprite(self):
        self.screen.blit(self.spriteImage, self.playerRectangle.topleft)


        

        


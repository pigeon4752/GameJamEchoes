import pygame
class Sprite:
    position = pygame.Vector2(0,0)
    velocity = pygame.Vector2(0,0)
    

    def __init__(self,screen):
        self.screen = screen

    def updatePosition(self):
        position.x += velocity.x
        position.y += velocity.y
    
    def incrementXVelocity(self,increment):
        self.velocity.x += increment

    def incrementYVelocity(self,increment):
        self.velocity.y += increment
    
    def isGrounded():
        pass


        

        


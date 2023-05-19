import pygame
class Entity:
    position = pygame.Vector2(0,0)
    velocity = pygame.Vector2(0,0)
    

    def __init__(self,screen):
        self.screen = screen

    def updatePosition(self):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
    
    def changeXVelocity(self,increment):
        self.velocity.x += increment

    def changeYVelocity(self,increment):
        self.velocity.y += increment
    
    def isGrounded():
        pass


        

        


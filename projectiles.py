import pygame 

class Projectile():
    def __init__(self, x, y,xVelocity,yVelocity):
        self.position = pygame.Vector2(x,y)
        self.speed = pygame.Vector2(xVelocity,yVelocity)
        self.projectileRectangle = pygame.Rect(x, y, 3, 6)
    
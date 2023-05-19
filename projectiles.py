import pygame 

class Projectile():
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 10
        self.projectileRectangle = pygame.Rect.Rect()
    
import pygame 

class Projectile:
    def __init__(self, x, y, angle=180):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 3
        self.projectileRectangle = pygame.Rect(x, y, 3, 6)

    def update(self):
        pass
    
    def travel(self):
        pass
    


        
    
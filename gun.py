import pygame
from projectiles import Projectile

class Gun:
    # height and width attributes
    width = 10
    height = 5
    
    def __init__(self, player_rect):
        self.gunRect = pygame.Rect(0, 0, Gun.width, Gun.height)
        

    def fire_gun(self, angle, click_duration):
        projectile = Projectile(self.gunRect.x, self.gunRect.y, angle=angle)
        print("pewpew")
        pass


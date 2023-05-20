import pygame
import os
from projectiles import Projectile

class Gun:
    # height and width attributes
    width = 10
    height = 5
    angle = 0
    def __init__(self, player_rect,screen):
        self.player_rect = player_rect
        self.screen = screen
        self.gunImage = pygame.image.load(os.path.join('gun.png'))

        
    def fire_gun(self, angle, click_duration):
        pass
    #     projectile = Projectile(self.gunRect.x, self.gunRect.y, angle=angle)
    #     print("pewpew")
    #     pass

    def setAngle(self, angle):
        self.angle = angle
    
    def update(self):
        pygame.transform.rotate(self.gunImage, self.angle)

    def draw(self):
        self.screen.blit(self.gunImage, (self.player_rect.centerx, self.player_rect.centery))
        pass

    def rotate(self,angle):
        pass


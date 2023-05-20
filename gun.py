import pygame
import os
from projectiles import Projectile

class Gun:

    def __init__(self, player_rect, screen):
        self.screen = screen
        self.player_rect = player_rect
        self.gunImage = pygame.image.load(os.path.join('gun.png'))
        
    def fire_gun(self, angle, click_duration):
        #projectile = Projectile(self.gunRect.x, self.gunRect.y, angle=angle)
        pass

    def setAngle(self, angle):
        self.angle = angle
    
    def update(self):
        self.gunImage = pygame.transform.rotate(self.gunImage, self.angle)

    def draw(self):
        self.screen.blit(self.gunImage, (self.player_rect.centerx, self.player_rect.centery))

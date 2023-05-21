import pygame
import os
import math
from projectiles import Projectile

class Gun:
    # height and width attributes
    width = 30
    height = 10
    angle = 0
    projectile_speed = 10
    MAX_VELOCITY = 15

    def __init__(self, player_rect,screen):
        self.player_rect = player_rect
        self.screen = screen
        self.gunImage = pygame.transform.scale((pygame.image.load(os.path.join('SonarGun.png'))), (self.width, self.height))
        # self.gunImage = pygame.transform.scale(self.gunImage, (10, 5))
        
    def fire_gun(self, angle, click_duration, background, screen):
        # speed is evaluated in proportion to the click_duration
        yVelocity = ((self.projectile_speed*0.8*click_duration) * math.sin(math.radians(angle)))
        xVelocity = ((self.projectile_speed*0.8*click_duration) * math.cos(math.radians(angle)))
        while xVelocity>self.MAX_VELOCITY or xVelocity<0-self.MAX_VELOCITY:
            xVelocity=xVelocity*0.9
            yVelocity= yVelocity*0.9
        while yVelocity>self.MAX_VELOCITY or yVelocity<0-self.MAX_VELOCITY:
            yVelocity=yVelocity*0.9
            xVelocity=xVelocity*0.9
        projectile = Projectile(self.player_rect.centerx ,self.player_rect.centery ,xVelocity ,yVelocity, background, screen)
        return projectile
        
    #     projectile = Projectile(self.gunRect.x, self.gunRect.y, angle=angle)
    #     print("pewpew")
    #     pass

    def update(self):
        self.gunSprite = pygame.transform.rotate(self.gunImage, -(self.angle))

    def draw(self):
        self.screen.blit(self.gunSprite, (self.player_rect.x+14, self.player_rect.y+15))
        pass

    def rotate(self,angle):
        pass


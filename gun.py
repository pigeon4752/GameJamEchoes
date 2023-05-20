import pygame
from projectiles import Projectile

class Gun:
    # height and width attributes
    width = 10
    height = 5
    angle = 0
    def __init__(self, player_rect,surface):
        self.screen=pygame.Surface((800,800))
        self.player_rect = player_rect
        self.gunRect = pygame.Rect(0, 0, Gun.width, Gun.height)
        
    def fire_gun(self, angle, click_duration):
        projectile = Projectile(self.gunRect.x, self.gunRect.y, angle=angle)
        print("pewpew")
        pass

    def setAngle(self,angle):
        self.angle = angle

    def draw(self):
        self.gunRect.topleft=(self.player_rect.left+(self.player_rect.width/2),self.player_rect.top+(self.player_rect.height/2))
        pygame.draw.rect(self.screen,"yellow",self.gunRect)
        self.rotate(self.angle)

    def rotate(self,angle):
        pygame.transform.rotate(self.screen,angle)


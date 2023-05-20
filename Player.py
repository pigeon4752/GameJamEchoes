import pygame
from Sprite import Sprite
from gun import Gun
class Player(Sprite):
    moveSpeed = 2
    gravity = 1

    def update(self,dt):
        self.changeYVelocity(self.gravity*dt)
        # self.updatePosition()
        super().update(dt)


    def passAngleToGun(self,angle):
        self.gun.setAngle(angle)

    def draw(self):
        super().draw()
    
    def fire(self, angle, click_duration):
        self.gun.fire_gun(angle, click_duration)
        print(click_duration)
        print("click")


    def __init__(self,screen,background,moveSpeed):
        super().__init__(screen,background)
        self.moveSpeed = moveSpeed
        self.gun = Gun(self.playerRectangle,screen)
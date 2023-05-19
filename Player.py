import pygame
from Sprite import Sprite
class Player(Sprite):
    moveSpeed = 5
    gravity = 1

    def update(self,dt):
        self.changeYVelocity(self.gravity*dt)
        # self.updatePosition()
        super().update(dt)

    def __init__(self,screen,background,moveSpeed):
        super().__init__(screen,background)
        self.moveSpeed = moveSpeed
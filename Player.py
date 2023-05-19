import pygame
import Sprite as Sprite
class Player(Sprite):
    moveSpeed = 5

    def __init__(self,moveSpeed):
        super().__init__()
        self.moveSpeed
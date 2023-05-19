import pygame
from entity import Entity
class Player(Entity):
    moveSpeed = 5

    def __init__(self,moveSpeed):
        super().__init__()
        self.moveSpeed = moveSpeed
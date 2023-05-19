import pygame
from Sprite import Sprite
class Player(Sprite):
    def __init__(self,screen,background,width=10,size= 10,colour="red"):
        super().__init__(screen,background,width,size,colour)
    
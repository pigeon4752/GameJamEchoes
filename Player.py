import pygame
from Sprite import Sprite
from gun import Gun
class Player(Sprite):
    moveSpeed = 2
    

    def update(self,dt):
        self.changeYVelocity(self.gravity*dt)
        self.coordinates = self.calculateCoordinates(self.position.x, self.position.y)
        self.background.modifyCoordinateMap(self.coordinates,self.calculateCoordinates(self.coordinates.x, self.coordinates.y),2)
        # self.updatePosition()
        super().update(dt)


    def passAngleToGun(self,angle):
        self.gun.setAngle(angle)

    def draw(self):
        super().draw()
    
    def fire(self, angle, click_duration):
        self.gun.fire_gun(angle, click_duration)



    def __init__(self,screen,background,moveSpeed,rendered = True):
        super().__init__(screen,background,rendered=rendered)
        self.moveSpeed = moveSpeed
        self.gun = Gun(self.playerRectangle,screen)
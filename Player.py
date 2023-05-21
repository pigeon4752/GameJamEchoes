import pygame
from Sprite import Sprite
from gun import Gun
from projectileHandler import ProjectileHandler
from AnimationHandler import AnimationHandler

class Player(Sprite):
    moveSpeed = 1.5
    gravity = 1.5

    def update(self,dt):
        self.changeYVelocity(self.gravity*dt)
        self.background.modifyCoordinateMap(self.coordinates,self.calculateCoordinates(self.position.x, self.position.y),2)
        #print(self.coordinates)
        #print(self.calculateCoordinates(self.coordinates.x, self.coordinates.y)
        self.coordinates = self.calculateCoordinates(self.position.x, self.position.y)
        
        # self.updatePosition()
        super().update(dt)
        self.background.addLight(self.position.x-20,self.position.y,50,10)

    def passAngleToGun(self,angle):
        self.gun.setAngle(angle)

    def updateSprite(self):
        self.AnimationHandler.moveConductor.play()
        super().updateSprite(self.AnimationHandler.animObjs)
    
    def fire(self, angle, click_duration):
        projectile = self.gun.fire_gun(angle, click_duration, self.background, self.screen)
        self.projectileHandler.addProjectile(projectile)


    def __init__(self,screen,background,moveSpeed,rendered = True):
        super().__init__(screen,background,rendered=rendered)
        self.moveSpeed = moveSpeed
        self.gun = Gun(self.playerRectangle,screen)
        self.projectileHandler = ProjectileHandler()
        self.AnimationHandler = AnimationHandler("Oldman.png", 2, 4, ['idle_right', 'walk_right'])
        
        
import pygame
from Sprite import Sprite
from gun import Gun
from projectileHandler import ProjectileHandler
from AnimationHandler import AnimationHandler
import math

class Player(Sprite):
    moveSpeed = 1.5
    gravity = 1.5

    def update(self,dt):
        self.changeYVelocity(self.gravity*dt)
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

    def addBoost(self, x, y, size, intensity):
        # Calculate the distance between the player's position and the boost point
        dx = x - self.position.x
        dy = y - self.position.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        
        # Check if the player is within the boost radius
        if distance <= size:
            # Calculate the direction vector away from the boost point
            direction = (dx / distance, dy / distance)
            
            # Apply the boost to the player's velocity
            self.velocity.x-=(direction[0] * intensity)
            self.velocity.y-=(direction[1] * intensity)
        return True
    
    def addGrapple(self, x, y, intensity):
        # Calculate the distance between the player's position and the boost point
        dx = x - self.position.x
        dy = y - self.position.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        
        # Check if the player is within the boost radius
        
            # Calculate the direction vector away from the boost point
        direction = (dx / distance, dy / distance)
            
            # Apply the boost to the player's velocity
        self.velocity.x-=(direction[0] * intensity)
        self.velocity.y-=(direction[1] * intensity)
        return True

    def __init__(self,screen,background,moveSpeed,rendered = True):
        super().__init__(screen,background,rendered=rendered)
        self.moveSpeed = moveSpeed
        self.gun = Gun(self,screen)
        self.projectileHandler = ProjectileHandler()
        self.AnimationHandler = AnimationHandler("Oldman.png", 2, 4, ['idle_right', 'walk_right'])
        
        
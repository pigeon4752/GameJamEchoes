import pygame
class KeyHandler():

    def handleKeys(self,keys):
        if keys[pygame.K_w]:
            # print("'W' key is being pressed")
            self.player.changeYVelocity(self.player.moveSpeed)
        if keys[pygame.K_a]:
            # print("'A' key is being pressed")
            self.player.changeXVelocity(-self.player.moveSpeed)
        if keys[pygame.K_s]:
            # print("'S' key is being pressed")
            self.player.changeYVelocity(-self.player.moveSpeed)
        if keys[pygame.K_d]:
            # print("'D' key is being pressed")
            self.player.changeXVelocity(self.player.moveSpeed)

    def __init__(self,player):
        self.player = player
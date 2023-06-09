import pygame
class KeyHandler():

    def handleKeys(self,keys,dt):
        if keys[pygame.K_w]:
            # print("'W' key is being pressed")
            if (self.player.velocity.y == 0):
                self.player.changeYVelocity(-15)
        if keys[pygame.K_a]:
            # print("'A' key is being pressed")
            self.player.changeXVelocity(-self.player.moveSpeed)
        if keys[pygame.K_s]:
            # print("'S' key is being pressed")
            self.player.changeYVelocity(self.player.moveSpeed)
        if keys[pygame.K_d]:
            # print("'D' key is being pressed")
            self.player.changeXVelocity(self.player.moveSpeed)
        if keys[pygame.K_j]:
            self.background.lightAllTiles()
        # else:
        #     self.background.decreaseBrightness
        if keys[pygame.K_l]:
            self.background.printMap()
            print(self.player.coordinates.x)
            print(self.player.coordinates.y)
            

    def __init__(self,player,background):
        self.player = player
        self.background = background
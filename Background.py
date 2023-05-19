import pygame
class Background:
    
    def __init__(self,screen):
        self.screen = screen
        self.rectArray = []
        self.createNewBackground()
        
    
    def createNewBackground(self):
        rectangle = pygame.Rect(100, self.screen.get_height() - 100, self.screen.get_width()-200, 100)
        
        self.rectArray.append(("blue",rectangle))
    
    def updatePosition(self):
        for rect in self.rectArray:
            pygame.draw.rect(self.screen,rect[0],rect[1])

    def isGrounded(self):
        for rect in self.rectArray:
            print(rect[0].bottom)

    def checkGrounded(self, rectangle):
        pass

    def handlePlayerCollision(self,player,previousX,previousY):
        playerTop = player.position.y
        playerRight = player.position.x+player.playerRectangle.width
        playerBottom = player.position.y+player.playerRectangle.height
        playerLeft = player.position.x

        for rect in self.rectArray:
            if playerRight > rect[1].left and playerLeft < rect[1].right:
                # Player is within the horizontal bounds of the current platform
                if previousY + player.playerRectangle.height <= rect[1].top:
                    # Player was above the platform in the previous frame
                    if playerBottom > rect[1].top:  # Added check
                        player.position.y = rect[1].top - player.playerRectangle.height
                        player.velocity.y = 0
                elif previousY >= rect[1].top + rect[1].height:
                    # Player was below the platform in the previous frame
                    if playerTop < rect[1].bottom:  # Added check
                        player.position.y = rect[1].top + rect[1].height
                        player.velocity.y = 0

            if playerBottom > rect[1].top and playerTop < rect[1].bottom:
                # Player is within the vertical bounds of the current platform
                if previousX + player.playerRectangle.width <= rect[1].left:
                    # Player was to the left of the platform in the previous frame
                    if playerRight > rect[1].left:  # Added check
                        player.position.x = rect[1].left - player.playerRectangle.width
                        player.velocity.x = 0
                elif previousX >= rect[1].right:
                    # Player was to the right of the platform in the previous frame
                    if playerLeft < rect[1].right:  # Added check
                        player.position.x = rect[1].right
                        player.velocity.x = 0

                    


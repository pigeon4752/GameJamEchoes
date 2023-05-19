import pygame
from mouseHandler import MouseHandler
import Background as Background
from Player import Player
from keyHandler import KeyHandler
from EntityHandler import EntityHandler
from Background import Background

class main:

    pygame.init()
    screen = pygame.display.set_mode([1000, 600])
    background = Background(screen)
    clock = pygame.time.Clock()
    player1 = Player(screen,background,5)
    keyHandler = KeyHandler(player1)
    entityHandler = EntityHandler()
    entityHandler.addEntity(player1)

    running = True
    while running:
        dt = clock.tick(60)
        dt = dt/50
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get state of all keys
        keys = pygame.key.get_pressed()
        keyHandler.handleKeys(keys,dt)

        screen.fill((255, 255, 255))
        background.updatePosition()
        entityHandler.updateEntities(dt)


        # Flip the display

        pygame.display.flip()
        


# Done! Time to quit.

pygame.quit()
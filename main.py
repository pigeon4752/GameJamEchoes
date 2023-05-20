import pygame
from mouseHandler import MouseHandler
import Background as Background
from Player import Player
from keyHandler import KeyHandler
from EntityHandler import EntityHandler
from Background import Background

class main:

    pygame.init()
    screen = pygame.display.set_mode([800, 800])
    background = Background(screen)
    clock = pygame.time.Clock()
    player1 = Player(screen,background,5)
    keyHandler = KeyHandler(player1)
    entityHandler = EntityHandler()
    entityHandler.addEntity(player1)
    bg = pygame.image.load("background.png")
    

    running = True
    while running:
        dt = clock.tick(60)
        dt = dt/50
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # need to make mousehandler instance
                MouseHandler.increment_counter()

            elif event.type == pygame.MOUSEBUTTONUP:
                angle = MouseHandler.mouse_angle()
                click_duration = MouseHandler.click_duration()
                player1.gun.fire_gun(angle, click_duration)

        # Get state of all keys
        keys = pygame.key.get_pressed()
        keyHandler.handleKeys(keys,dt)
        entityHandler.updateEntities(dt)
        screen.fill((255, 255, 255))
        screen.blit(bg, (0, 0))
        background.updatePosition()
        


        # Flip the display

        pygame.display.flip()
        


# Done! Time to quit.

pygame.quit()
import pygame
import Background as Background
from player import Player
from keyHandler import KeyHandler


class main:

    player1 = Player()
    keyHandler = KeyHandler(player1)


    pygame.init()
    screen = pygame.display.set_mode([500, 500])

    background = Background.Background(screen)
    
    

    clock = pygame.time.Clock()

    running = True
    player1 = player.Player(screen, background)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get state of all keys
        keys = pygame.key.get_pressed()
        keyHandler.handleKeys(keys)

        screen.fill((255, 255, 255))
        player1.updatePosition()
        


         # Draw a solid blue circle in the center

        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)


        # Flip the display

        pygame.display.flip()
        dt = clock.tick(60)


# Done! Time to quit.

pygame.quit()
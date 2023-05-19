import pygame
class main:
    pygame.init()
    screen = pygame.display.set_mode([500, 500])
    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False

        screen.fill((255, 255, 255))


         # Draw a solid blue circle in the center

        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)


        # Flip the display

        pygame.display.flip()


# Done! Time to quit.

pygame.quit()
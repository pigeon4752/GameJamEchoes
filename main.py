import pygame
from mouseHandler import MouseHandler

class main:
    pygame.init()
    screen = pygame.display.set_mode([500, 500])
    mouseHandler = MouseHandler()

    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseHandler.increment_counter()
            
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_coords = pygame.mouse.get_pos()
                print(mouseHandler.mouse_angle(mouse_coords, (250, 250)))
                
        screen.fill((255, 255, 255))


         # Draw a solid blue circle in the center

        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)


        # Flip the display

        pygame.display.flip()


# Done! Time to quit.

pygame.quit()
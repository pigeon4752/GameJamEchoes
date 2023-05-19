import pygame



class main:

    def handleKeys(keys):
        if keys[pygame.K_a]:
            print("'A' key is being pressed")


    pygame.init()
    screen = pygame.display.set_mode([500, 500])
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get state of all keys
        keys = pygame.key.get_pressed()
        handleKeys(keys)
        
        screen.fill((255, 255, 255))


         # Draw a solid blue circle in the center

        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)


        # Flip the display

        pygame.display.flip()
        dt = clock.tick(60)


# Done! Time to quit.

pygame.quit()
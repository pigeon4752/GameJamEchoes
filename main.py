import pygame
from mouseHandler import MouseHandler
import Background as Background
from Player import Player
from keyHandler import KeyHandler
from EntityHandler import EntityHandler
from Background import Background

class main:

    pygame.init()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    
    screen = pygame.display.set_mode([SCREEN_HEIGHT, SCREEN_WIDTH])
    background = Background(screen,SCREEN_WIDTH,SCREEN_HEIGHT)
    clock = pygame.time.Clock()
    player1 = Player(screen,background,5)
    keyHandler = KeyHandler(player1,background)
    entityHandler = EntityHandler()
    entityHandler.addEntity(player1)
    bg = pygame.image.load("background.png")
    
    running = True
    while running:
        dt = clock.tick(60)
        dt = dt/40

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # need to make mousehandler instance
                MouseHandler.increment_counter()

            elif event.type == pygame.MOUSEBUTTONUP:
                angle = MouseHandler().mouse_angle()
                click_duration = MouseHandler().click_duration()
                player1.gun.fire_gun(angle, click_duration)

        
        #screen.blit(bg, (0, 0))
        

        # Get state of all keys
        keys = pygame.key.get_pressed()

        ##THERE IS A NECESSARY ORDER
        ## WE WANT THE RECTANGLE/HITBOX AROUND THE SPRITE TO BE COVERED OVER BY THE WHITE AS IT CAN'T BE MADE TRANSPARENT
        ## THE HITBOX IS CONSIDERED AN ENTITY/ ALL RECTANGLES ARE CONSIDERED ENTITIES
        keyHandler.handleKeys(keys,dt)
        entityHandler.updateEntities(dt) ##DRAW ALL HITBOXES 
        screen.fill((0, 0, 0))
        #screen.fill((255, 255, 255)) ## WIPE HITBOES
        #screen.blit(bg, (0, 0)) ## ADD BACKGROUND
        #background.addBigFog()
        entityHandler.updateSprites(dt) ## UPDATE ALL SPRITES

        background.updateMap() ## Add all walls
        #background.addFog()
        
        
        


        # Flip the display

        pygame.display.flip()
        


# Done! Time to quit.

pygame.quit()
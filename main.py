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
    keyHandler = KeyHandler(player1)
    entityHandler = EntityHandler()
    entityHandler.addEntity(player1)
    bg = pygame.image.load("background.PNG")
    
    running = True
    while running:
        dt = clock.tick(60)
        dt = dt/50
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get state of all keys
        keys = pygame.key.get_pressed()

        ##THERE IS A NECESSARY ORDER
        ## WE WANT THE RECTANGLE/HITBOX AROUND THE SPRITE TO BE COVERED OVER BY THE WHITE AS IT CAN'T BE MADE TRANSPARENT
        ## THE HITBOX IS CONSIDERED AN ENTITY/ ALL RECTANGLES ARE CONSIDERED ENTITIES
        keyHandler.handleKeys(keys,dt)
        entityHandler.updateEntities(dt) ##DRAW ALL HITBOXES 
        screen.fill((255, 255, 255)) ## WIPE HITBOES
        #screen.blit(bg, (0, 0)) ## ADD BACKGROUND
        background.addBigFog()
        entityHandler.updateSprites(dt) ## UPDATE ALL SPRITES

        background.updateMap() ## Add all walls
        background.addFog()
        
        
        


        # Flip the display

        pygame.display.flip()
        


# Done! Time to quit.

pygame.quit()
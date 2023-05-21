import pygame
from mouseHandler import MouseHandler
import Background as Background
from Goblin import Goblin
from Player import Player
from keyHandler import KeyHandler
from EntityHandler import EntityHandler
from Background import Background
from projectiles import Projectile
from projectileHandler import ProjectileHandler


class main:

    pygame.init()
    SCREEN_WIDTH = 768
    SCREEN_HEIGHT = 768
    
    screen = pygame.display.set_mode([SCREEN_HEIGHT, SCREEN_WIDTH])
    background = Background(screen,SCREEN_WIDTH,SCREEN_HEIGHT)
    clock = pygame.time.Clock()
    player1 = Player(screen,background,5)
    mouseHandler = MouseHandler()
    
    gobbo = Goblin(screen,background)
    
    keyHandler = KeyHandler(player1,background)
    entityHandler = EntityHandler()
    entityHandler.addEntity(player1)
    entityHandler.addEntity(gobbo)
    bg = pygame.image.load("background.png")

    projectileHandler = ProjectileHandler()


    projectile = Projectile(400,400,11,0,background,screen)
    projectileHandler.addProjectile(projectile)

    mousehandler = MouseHandler()

    mouse_down = False
    running = True
    while running:
        dt = clock.tick(40)
        dt = dt/40

        angle = mousehandler.mouse_angle(pygame.mouse.get_pos(), player1.position)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True

            elif event.type == pygame.MOUSEBUTTONUP:
                click_duration = mousehandler.click_duration()
                # fire projectile at given angle and click strength
                player1.fire(angle, click_duration)
                mouse_down = False
                

        # indicates length of time mouse down. for charging shot
        if mouse_down:
            mousehandler.increment_counter()

        #screen.blit(bg, (0, 0))
        

        # Get state of all keys
        keys = pygame.key.get_pressed()
        keyHandler.handleKeys(keys,dt)
        screen.fill((0, 0, 0))
        entityHandler.updateEntities(dt) ##DRAW ALL HITBOXES
        projectileHandler.update()
        background.updateMap() ## Add all walls and fog
        player1.gun.angle = angle
        player1.gun.update()
        player1.gun.draw()
       
        
    
        # Flip the display

        pygame.display.flip()
        


# Done! Time to quit.

pygame.quit()
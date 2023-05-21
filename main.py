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
import os

class main:

    pygame.init()
    SCREEN_WIDTH = 768
    SCREEN_HEIGHT = 768
    
    screen = pygame.display.set_mode([SCREEN_HEIGHT, SCREEN_WIDTH])
    
    pygame.display.set_caption("Mine Goblin")
    icon_image = pygame.image.load("jumboBroadclothIcon.png")
    pygame.display.set_icon(icon_image)
    clock = pygame.time.Clock()
    
    mouseHandler = MouseHandler()

    SONG_END = pygame.USEREVENT+1


    def playMusic(songName):
        pygame.mixer.init()
        song = os.path.join(songName)
        pygame.mixer.music.load(song)
        pygame.mixer.music.set_volume(0.8)
        pygame.mixer.music.set_endevent(pygame.USEREVENT+1)
        pygame.mixer.music.play()

    story = False # SET TO FALSE FOR NO STORY
    playMusic("IntroSong.mp3")
    pygame.mixer.Sound("munch.mp3").play()
    storyImage = pygame.image.load(os.path.join("story0.png"))
    pressCount = 0
    TOTAL_STORY_FRAMES = 3
    while story:
        dt = clock.tick(60)
        dt = dt/40
        # STORYBOARD LOOP
        for event in pygame.event.get():
            if event.type == SONG_END:
                print("song over")
                pygame.mixer.music.unload()
                playMusic("IntroSong.mp3")     
            if event.type == pygame.QUIT:
                story=False
                running = False
                continue
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                pygame.Surface.convert_alpha(storyImage)
                end = 255
                while end > 0:
                    pygame.Surface.fill(screen,(0,0,0))
                    screen.blit(storyImage,(0,0))
                    storyImage.set_alpha(end)
                    pygame.display.flip()
                    end-=3
                    if end<0:
                        end=0               
                if pressCount >=TOTAL_STORY_FRAMES-1:
                    story = False
                    pygame.mixer.Sound("swallow.mp3").play()
                else:
                    pressCount+=1
                    storyImage = pygame.image.load(os.path.join("story" + str(pressCount) + ".png"))
                    storyImage.set_alpha(255)
                pass
        screen.blit(storyImage,(0,0))
        pygame.display.flip()
    
    background = Background(screen,SCREEN_WIDTH,SCREEN_HEIGHT)

    #gobbo = Goblin(screen,background)
    
    player1 = Player(screen,background,5)
    keyHandler = KeyHandler(player1,background)
    entityHandler = EntityHandler()
    entityHandler.addEntity(player1)
    #entityHandler.addEntity(gobbo)
    
    #bg = pygame.image.load("background.png")

    projectileHandler = ProjectileHandler()


    #projectile = Projectile(400,400,11,0,background,screen)
    #projectileHandler.addProjectile(projectile)

    mousehandler = MouseHandler()


    mouse_down = False
    running = True
    while running:
        # MAIN GAME LOOP
        dt = clock.tick(60)
        dt = dt/40
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
            elif event.type == pygame.MOUSEBUTTONUP:
                angle = mousehandler.mouse_angle(pygame.mouse.get_pos(), player1.position)
                click_duration = mousehandler.click_duration()
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

        #gun updates
        player1.gun.angle = (mousehandler.mouse_angle(pygame.mouse.get_pos(), player1.position))
        entityHandler.updateEntities(dt) # DRAW ALL HITBOXES
        projectileHandler.update()
        background.updateMap() # Update light

        pygame.display.flip()
        


    # Done! Time to quit.
    pygame.quit()
    
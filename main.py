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
from multiplayer import Multiplayer
import time
import os

class main:
    
    def __init__(self,story = False,multiplayer = True):


        pygame.init()
        SCREEN_WIDTH = 768
        SCREEN_HEIGHT = 768
        
        
        self.screen = pygame.display.set_mode([SCREEN_HEIGHT, SCREEN_WIDTH])
        
        pygame.display.set_caption("Mine Goblin")
        icon_image = pygame.image.load("jumboBroadclothIcon.png")
        pygame.display.set_icon(icon_image)
        
        
        self.story(pygame.time.Clock(),story=False)
        clock = pygame.time.Clock()
        self.background = Background(self.screen,SCREEN_WIDTH,SCREEN_HEIGHT)
        multiplayerValid = False
        if multiplayer:
            
            secondPlayer = self.instantiateMultiplayer(self.background.player)
            if secondPlayer != None:
                self.background.addEntity(secondPlayer)
                multiplayerValid = True

            
        
        
        entityHandler = EntityHandler(self.background.entityArray)
        keyHandler = KeyHandler(self.background.player,self.background)
        projectileHandler = ProjectileHandler()
        mouseHandler = MouseHandler()

        
        
        running = True
        while running:
            # MAIN GAME LOOP
            dt = clock.tick(60)
            dt = dt/40
            for event in pygame.event.get():
                mouseHandler.handleClicks(event,self.background.player)
                if event.type == pygame.QUIT:
                    running = False
                
                    
                                  
                      
            # Get state of all keys
            keys = pygame.key.get_pressed()
            keyHandler.handleKeys(keys,dt)
            self.screen.fill((0, 0, 0))
            entityHandler.updateEntities(dt) # DRAW ALL HITBOXES
            projectileHandler.update()
            self.background.updateMap() # Update light
            if multiplayerValid:
                self.multiplayer.updateOpponent(self.background.player, secondPlayer)
            if self.background.player.dead:
                entityHandler.resetEntities(dt)

            pygame.display.flip()
            


        # Done! Time to quit.
        pygame.quit()
        self.multiplayer.wipe()


    def instantiateMultiplayer(self,player):

        self.multiplayer = Multiplayer(player)
        if self.multiplayer.valid:
            loaded = False
            while not loaded:
                loaded,opponent = self.multiplayer.getOtherPlayer()

                time.sleep(0.2)
            
            return(Player(self.screen,self.background,2,x=opponent["xPos"],y=opponent["yPos"]))
        else:
            return(None)
            


    def story(self,clock,story = False):
        SONG_END = pygame.USEREVENT+1


        def playMusic(songName):
            pygame.mixer.init()
            song = os.path.join(songName)
            pygame.mixer.music.load(song)
            pygame.mixer.music.set_volume(0.8)
            pygame.mixer.music.set_endevent(pygame.USEREVENT+1)
            pygame.mixer.music.play()

        #story = False # SET TO FALSE FOR NO STORY
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
                        pygame.Surface.fill(self.screen,(0,0,0))
                        self.screen.blit(storyImage,(0,0))
                        storyImage.set_alpha(end)
                        pygame.display.flip()
                        end-=3
                        if end<0:
                            end=0               
                    if pressCount >=TOTAL_STORY_FRAMES-1:
                        story = False
                        pygame.mixer.Sound("im_coming_to_get_you.mp3").play()
                    else:
                        pressCount+=1
                        storyImage = pygame.image.load(os.path.join("story" + str(pressCount) + ".png"))
                        storyImage.set_alpha(255)
                    pass
            self.screen.blit(storyImage,(0,0))
            pygame.display.flip()
    
if __name__ == "__main__":

    main()
from Bot import Bot
from gun import Gun
import random
import threading
class Goblin(Bot):
    def __init__(self,screen,background,rendered = False):
        super().__init__(screen,background)
        gobbo = threading.Thread(target=self.run, args=())
        gobbo.start()

    def run(self):
        while self.health>0:
            #print(self.position.x)
            self.changeXVelocity(random.randint(-20,20))
            self.changeYVelocity(random.randint(-10,10))
        time.sleep(100)
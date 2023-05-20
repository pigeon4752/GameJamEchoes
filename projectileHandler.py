

class ProjectileHandler():
    projectiles = []

    def addProjectile(self,proj):
        self.projectiles.append(proj)

    def removeProjectile(self,proj):
        self.projectiles.remove(proj)

    def update(self):
        for proj in self.projectiles:
            remove = proj.update()
            if remove:
                self.removeProjectile(proj)
                continue
            proj.draw()


    def __init__(self):
        pass
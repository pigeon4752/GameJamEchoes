import pyganim

class AnimationHandler:
    def __init__(self, spritesheet, rows, columns, animTypes, rects=[]):
        self.animObjs = {}
        self.unpackSpritesheet(spritesheet, rows, columns, animTypes, rects=rects)
        self.moveConductor = pyganim.PygConductor(self.animObjs)
        
    def unpackSpritesheet(self, spritesheet, rows, columns, animTypes, rects=[]):
        images = pyganim.getImagesFromSpriteSheet(spritesheet, rows=rows, cols=columns, rects=rects)
        frames = [list(zip(images[i:i+columns], [100] * columns)) for i in range(0, len(images), columns)]
        for i, animType in enumerate(animTypes):
            self.animObjs[animType] = pyganim.PygAnimation(frames[i])
            # making complementary left movement animations for moving
            if 'right' in animType:
                leftAnim = animType.replace('right', 'left')
                self.animObjs[leftAnim] = self.animObjs[animType].getCopy()
                self.animObjs[leftAnim].flip(True, False)
                self.animObjs[leftAnim].makeTransformsPermanent()
        
    
class Tile:

    
    
    def __init__(self,image,rect,shadow,x,y,damaging = False,damageRate = 0,glows = False):
        self.image = image
        self.image.convert_alpha()
        self.rect = rect
        self.shadow = 0
        if glows:
            self.shadow = 100
        self.x = x
        self.y = y
        self.key = self.calculateKey(x,y)
        self.damaging = damaging
        self.damageRate = damageRate
        self.glows = glows 
    #max shadow is 255 and that is pitch blackz
    def calculateKey(self,x,y):
        return(x,"_",y)
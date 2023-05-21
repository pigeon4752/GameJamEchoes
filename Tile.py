class tile:

    
    
    def __init__(self,image,rect,shadow,x,y):
        self.image = image
        self.image.convert_alpha()
        self.rect = rect
        self.shadow = 0
        self.x = x
        self.y = y
        self.key = self.calculateKey(x,y)
    #max shadow is 255 and that is pitch blackz
    def calculateKey(self,x,y):
        return(x,"_",y)
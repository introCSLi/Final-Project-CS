import os, random, time
path = os.getcwd()

class Creature:
    def __init__ (self,x,y,r,g,img,w,h,F):
        self.x=x
        self.y=y
        self.r=r
        self.g=g
        self.w=w
        self.h=h
        self.f=0
        self.F=F
        self.vx=0
        self.vy=0
        self.dir = 1
        self.img = loadImage(path+"/Images/"+"Watergirl.png")
        
    def gravity(self):
        if self.y+self.r < self.g:
            self.vy += 0.4
            if self.y+self.r+self.vy > self.g:
                self.vy = self.g-(self.y+self.r)
        else:
            self.vy = 0
            
            
    def update(self):
        self.gravity()
        self.x += self.vx
        self.y += self.vy
        
        
class Fireboy(Creature):
    def __init__(self,x,y,r,g,img,w,h,F):
        Creature.__init__(self,x,y,r,g,img,w,h,F)
        self.keyHandler = {LEFT:False, RIGHT:False, UP:False}
    
    
    
    
    
#class Watergirl(Fireboy):
    
    #all same except for starting location, keys to move, image, and collecting diamonds, and lava/water 




class Game:
    def __init__ (self,w,h,g):
        self.x=0
        self.w=w
        self.h=h
        self.g=g
        
    def display(self):

 
        image(img,0,0,self.w-x%self.w,self.h,x%self.w,0,self.w,self.h)
        image(img,self.w-x%self.w,0,x%self.w,self.h,0,0,x%self.w,self.h)


        
g = Game(1280,720,585)
def setup():
    size(g.w, g.h)
    

    
def draw():
    background(0)
    g.display()



def keyPressed():
    if keyCode == LEFT:
        g.fireboy.keyHandler[LEFT] = True
    elif keyCode == RIGHT:
        g.fireboy.keyHandler[RIGHT] = True
    elif keyCode == UP:
        g.fireboy.keyHandler[UP] = True
        
def keyReleased():
    if keyCode == "a":                                 #not sure about the keycode
        g.watergirl.keyHandler[LEFT] = False
    elif keyCode == "d":
        g.watergirl.keyHandler[RIGHT] = False
    elif keyCode == "w":
        g.watergirl.keyHandler[UP] = False

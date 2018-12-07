import os, random, time
path = os.getcwd() + "/"

class Creature:
    def __init__ (self, x, y, r, g, img):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.img = loadImage(path + "images/" + img)
        # self.w=w
        # self.h=h
        # self.f=0
        # self.F=F
        self.vx = 0
        self.vy = 0
        # self.dir = 1
       
        
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
        
    def display(self):
        self.update()
        self.img.resize(50,50)
        image(self.img, self.x, self.y)
        
        stroke(255,0,0)
        
class Fireboy(Creature):
    def __init__(self,x,y,r,g,img):
        Creature.__init__(self, x, y, r, g, img)
        self.keyHandler = {LEFT:False, RIGHT:False, UP:False}
    
    def update(self):
        self.gravity() 
        
        if self.keyHandler[LEFT]:
            self.vx = -5
            # self.direction = -1
        elif self.keyHandler[RIGHT]:
            self.vx = 5
            # self.direction = 1
        else:
            self.vx = 0
            
        if self.keyHandler[UP] and self.y + self.r == self.g:
            self.vy = -12
            
        # if self.x - self.r < 0:
        #     self.x = self.r 
        
        self.x += self.vx
        self.y += self.vy
        
    
    
    
    
#class Watergirl(Fireboy):
    
    #all same except for starting location, keys to move, image, and collecting diamonds, and lava/water 




class Game:
    def __init__ (self,w,h,g):
        self.x=0
        self.w=w
        self.h=h
        self.g=g
        self.fireboy = Fireboy(0, 50, 50, self.g, "boy.png")
    
        
    def display(self):

        self.fireboy.display()
    
        # image(img,0,0,self.w-x%self.w,self.h,x%self.w,0,self.w,self.h)
        # image(img,self.w-x%self.w,0,x%self.w,self.h,0,0,x%self.w,self.h)


g = Game(400, 400, 390)

def setup():
    size(g.w, g.h)
    background(255)

def draw():
    background(255)
    g.display()


def keyPressed():
    if keyCode == LEFT:
        g.fireboy.keyHandler[LEFT] = True
    elif keyCode == RIGHT:
        g.fireboy.keyHandler[RIGHT] = True
    elif keyCode == UP:
        g.fireboy.keyHandler[UP] = True
        
def keyReleased():
    if keyCode == LEFT:
        g.fireboy.keyHandler[LEFT] = False
    elif keyCode == RIGHT:
        g.fireboy.keyHandler[RIGHT] = False
    elif keyCode == UP:
        g.fireboy.keyHandler[UP] = False
    # elif keyCode == "a":                                 #not sure about the keycode
    #     g.watergirl.keyHandler[LEFT] = False
    # elif keyCode == "d":
    #     g.watergirl.keyHandler[RIGHT] = False
    # elif keyCode == "w":
    #     g.watergirl.keyHandler[UP] = False

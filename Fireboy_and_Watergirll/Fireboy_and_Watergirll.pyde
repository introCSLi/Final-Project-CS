import os, random, time
path = os.getcwd() + "/"

class Creature:
    def __init__ (self, x, y, r, g, img):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.img = loadImage(path + "images/" + img + ".png")
        self.vx = 0
        self.vy = 0
        self.direction1 = 0
        self.direction2 = 0
       
        
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
    
        if self.direction1 == 1:
            self.boyRight.resize(50,50)
            image(self.boyRight, self.x, self.y)
        elif self.direction1 == -1:
            self.boyLeft.resize(50,50)
            image(self.boyLeft, self.x, self.y)

        if self.direction2 == 1:
            self.girlRight.resize(50,50)
            image(self.girlRight, self.x, self.y)
        elif self.direction2 == -1:
            self.girlLeft.resize(50,50)
            image(self.girlLeft, self.x, self.y)
        if self.vx == 0:
            self.direction1 = 0
            self.direction2 = 0
            self.img.resize(50,50)
            image(self.img, self.x, self.y)
                
        stroke(255,0,0)
        
class Fireboy(Creature):
    def __init__(self,x,y,r,g,img):
        Creature.__init__(self, x, y, r, g, img)
        self.keyHandler = {LEFT:False, RIGHT:False, UP:False}
        self.boyLeft = loadImage(path + "images/" + img + "_left"+ ".png")
        self.boyRight = loadImage(path + "images/" + img + "_right" + ".png")
                                 
    
    def update(self):
        self.gravity() 
        
        if self.keyHandler[LEFT]:
            self.vx = -5
            self.direction1 = -1
        elif self.keyHandler[RIGHT]:
            self.vx = 5
            self.direction1 = 1
        else:
            self.vx = 0
            
        if self.keyHandler[UP] and self.y + self.r == self.g:
            self.vy = -12
            
        # if self.x - self.r < 0:
        #     self.x = self.r 
        
        self.x += self.vx
        self.y += self.vy
        

        
    
    
    
class Watergirl(Creature):
    def __init__(self,x,y,r,g,img):
        Creature.__init__(self, x, y, r, g, img)
        self.keyHandler = {LEFT:False, RIGHT:False, UP:False}
        self.girlLeft = loadImage(path + "images/" + img + "_left"+ ".png")
        self.girlRight = loadImage(path + "images/" + img + "_right" + ".png")
        
    def update(self):
        self.gravity() 
        
        if self.keyHandler[LEFT]:
            self.vx = -5
            self.direction2 = -1
        elif self.keyHandler[RIGHT]:
            self.vx = 5
            self.direction2 = 1
        else:
            self.vx = 0
            
        if self.keyHandler[UP] and self.y + self.r == self.g:
            self.vy = -12
            
        # if self.x - self.r < 0:
        #     self.x = self.r 
        
        self.x += self.vx
        self.y += self.vy



class Game:
    def __init__ (self,w,h,g):
        self.x=0
        self.w=w
        self.h=h
        self.g=g
        self.fireboy = Fireboy(0, 50, 50, self.g, "boy")
        #self.fireboy2 = Fireboy(0, 50, 50, self.g, "boy")
        self.watergirl=Watergirl(0, 50, 50, self.g, "girl")
        # self.bgImage = loadImage(path + "images/" + "background.png")
        
    def display(self):
        # image(self.bgImage, 0, 0)
        self.fireboy.display()
        self.watergirl.display()
        

g = Game(1000, 750, 740)

def setup():
    size(g.w, g.h)

bg = loadImage(path+"images/background.png")

def draw():
    background(bg)
    g.display()


def keyPressed():
    if keyCode == LEFT:
        g.fireboy.keyHandler[LEFT] = True
    elif keyCode == RIGHT:
        g.fireboy.keyHandler[RIGHT] = True
    elif keyCode == UP:
        g.fireboy.keyHandler[UP] = True
        
        
    elif key =="a":
        g.watergirl.keyHandler[LEFT] = True
    elif key=="d":
        g.watergirl.keyHandler[RIGHT] = True
    elif key=="w":
        g.watergirl.keyHandler[UP] = True
        
        
def keyReleased():
    if keyCode == LEFT:
        g.fireboy.keyHandler[LEFT] = False
    elif keyCode == RIGHT:
        g.fireboy.keyHandler[RIGHT] = False
    elif keyCode == UP:
        g.fireboy.keyHandler[UP] = False
   
    elif key =="a":
        g.watergirl.keyHandler[LEFT] = False
    elif key=="d":
        g.watergirl.keyHandler[RIGHT] = False
    elif key=="w":
        g.watergirl.keyHandler[UP] = False
   

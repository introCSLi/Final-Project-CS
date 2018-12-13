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
            
        for p in g.platforms:
            
            
            if self.y+self.r <= p.y and self.x+self.r >= p.x and self.x <= p.x+p.w:       #if the creature is above a platform and between the platform borders
                self.g = p.y                                                              #set the ground to platform coordinates
                break
            elif self.y<=p.y+p.h and self.x+self.r >= p.x and self.x <= p.x+p.w:          #else, if upper coordinate of creature is within the platform height and borders,
                 self.y+=1                                                                #make it out of the platform range
                 self.vy=3                                                                #give it a downward velocity
            self.g = g.g
            
            
            
            # if self.y+self.r <= p.y and self.x+self.r >= p.x and self.x <= p.x+p.w:
            #     self.g = p.y
            # break
            # elif self.y<=p.y+p.h and self.x+self.r >= p.x and self.x <= p.x+p.w:
            #     self.y+=1
            #     self.vy=3
            # self.g = g.g
            
    def update(self):
        self.gravity()
        self.x += self.vx
        self.y += self.vy
        
    def display(self):
        self.update()
    
        if self.direction1 == 1:
            self.boyRight.resize(60,60)
            image(self.boyRight, self.x, self.y)
        elif self.direction1 == -1:
            self.boyLeft.resize(60,60)
            image(self.boyLeft, self.x, self.y)

        if self.direction2 == 1:
            self.girlRight.resize(60,60)
            image(self.girlRight, self.x, self.y)
        elif self.direction2 == -1:
            self.girlLeft.resize(60,60)
            image(self.girlLeft, self.x, self.y)
        if self.vx == 0:
            self.direction1 = 0
            self.direction2 = 0
            self.img.resize(60,60)
            image(self.img, self.x, self.y)
                

class Fireboy(Creature):
    def __init__(self,x,y,r,g,img):
        Creature.__init__(self, x, y, r, g, img)
        self.keyHandler = {LEFT:False, RIGHT:False, UP:False}
        self.boyLeft = loadImage(path + "images/" + img + "_left"+ ".png")
        self.boyRight = loadImage(path + "images/" + img + "_right" + ".png")
        self.dmndCnt1 = 0
                                 
    
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
            self.vy = -11
        
        self.x += self.vx
        self.y += self.vy
        
        for d in g.diamonds:
            if self.distance(d) <= self.r + d.r and d.v == "f":
                g.diamonds.remove(d)
                self.dmndCnt1 += 1
                
        for l in g.lava:
            if self.distance(d)<=self.r + d.r and d.v == "w":
                print("Game over boy")
        
    def distance(self, target):
        return ((self.x - target.x)**2 + (self.y - target.y)**2)**0.5
    
    
class Watergirl(Creature):
    def __init__(self,x,y,r,g,img):
        Creature.__init__(self, x, y, r, g, img)
        self.keyHandler = {LEFT:False, RIGHT:False, UP:False}
        self.girlLeft = loadImage(path + "images/" + img + "_left"+ ".png")
        self.girlRight = loadImage(path + "images/" + img + "_right" + ".png")
        self.dmndCnt2 = 0
        
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
            self.vy = -11
    
        self.x += self.vx
        self.y += self.vy
        
        for d in g.diamonds:
            if self.distance(d) <= self.r + d.r and d.v == "w":
                g.diamonds.remove(d)  
                
        for l in g.lava:
            if self.x>=l.x and self.x <= l.x+l.w and self.y>=l.y and self.y <= l.y-l.h and l.v=="f":
                print("game over, girl")
            
    def distance(self, target):
        return ((self.x - target.x)**2 + (self.y - target.y)**2)**0.5
    
class Platform:
    def __init__(self, x, y, w, h, img):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = loadImage(path+"images/"+img)
        
    def display(self):
        image(self.img, self.x - g.x, self.y, self.w, self.h)
        
class Diamond:
    def __init__(self, x, y, w, h, img, r, v):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = loadImage(path+"images/"+img)
        self.r = r
        self.v = v
        
    def display(self):
        image(self.img, self.x - g.x, self.y, self.w, self.h)
        
class Lava:
    def __init__(self, x, y, w, h, img, v):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = loadImage(path+"images/"+img)
        self.v=v
    def display(self):
        image(self.img, self.x - g.x, self.y, self.w, self.h)
    
        

class Game:
    def __init__ (self,w,h,g):
        self.x=0
        self.w=w
        self.h=h
        self.g=g
        self.fireboy = Fireboy(0, 650, 50, self.g, "boy")
        self.watergirl=Watergirl(0, 560, 50, self.g, "girl")
        self.platforms = []
        self.diamonds = []
        self.lava=[]
        f = open(path+"/platforms.csv","r")
        for l in f:
            l = l.strip().split(",")
            if l[0] == "platform long":
                self.platforms.append(Platform(int(l[1]),int(l[2]),int(l[3]),int(l[4]),"platform.png"))
            elif l[0]=="platform short":
                self.platforms.append(Platform(int(l[1]),int(l[2]),int(l[3]),int(l[4]),"platform.png"))
            elif l[0]=="red":
                self.diamonds.append(Diamond(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "diamond_fire.png",15,"f"))
            elif l[0]=="blue":
                self.diamonds.append(Diamond(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "diamond_water.png",15,"w"))
            elif l[0]=="lava":
                self.lava.append(Lava(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "lava.PNG", "f"))
            elif l[0]=="water":
                self.lava.append(Lava(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "water.png", "w"))
        
    def display(self):
        for p in self.platforms:
            p.display()
            
        for d in self.diamonds:
            d.display()
            
        for l in self.lava:
            l.display()
            
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
   

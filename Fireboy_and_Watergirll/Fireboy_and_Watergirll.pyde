import os
import random
import time
path = os.getcwd() + "/"

class Creature:

    def __init__(self, x, y, r, g, img):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.img = loadImage(path + "images/" + img + ".png")
        self.vx = 0
        self.vy = 0
        self.direction1 = 0
        self.direction2 = 0
        self.stop_x = False

    def gravity(self):
        if self.y + 2 * self.r < self.g:
            self.vy += 0.3
            if self.y + 2 * self.r + self.vy > self.g:
                self.vy = self.g - (self.y + 2 * self.r)
        else:
            self.vy = 0

        self.g = g.g
        for p in g.platforms:
            
            if self.x + self.r >= p.x and self.x <= p.x + p.w - self.r:
                if self.y + 2 * self.r <= p.y:
                    self.g = p.y
               
                elif self.y + self.vy <= p.y + p.h -10 and self.y >= p.y + p.h - 10:
                    
                    self.vy = self.y - p.y - p.h+10
                
                    

    def update(self):
        self.gravity()
        self.x += self.vx
        self.y += self.vy

    def display(self):
        self.update()

        if self.direction1 == 1:
            image(self.boyRight, self.x, self.y)
        elif self.direction1 == -1:
            image(self.boyLeft, self.x, self.y)

        if self.direction2 == 1:
            image(self.girlRight, self.x, self.y)
        elif self.direction2 == -1:
            image(self.girlLeft, self.x, self.y)
        if self.vx == 0:
            self.direction1 = 0
            self.direction2 = 0
            image(self.img, self.x, self.y)


class Fireboy(Creature):

    def __init__(self, x, y, r, g, img):
        Creature.__init__(self, x, y, r, g, img)
        self.keyHandler = {LEFT: False, RIGHT: False, UP: False}
        self.boyLeft = loadImage(path + "images/" + img + "_left" + ".png")
        self.boyRight = loadImage(path + "images/" + img + "_right" + ".png")
        self.dmndCnt1 = 0

    def update(self):
        self.gravity()

        if self.x-self.r/2>=0 and self.x<=1000 and self.keyHandler[LEFT]:
            if self.stop_x == False:
                self.vx = -8
                self.direction1 = -1
            else:
                self.vx = 0
        elif self.x>=0 and self.x+2*self.r<=1000 and self.keyHandler[RIGHT]:
            if self.stop_x == False:
                self.vx = 8
                self.direction1 = 1
            else:
                self.vx = 0
        else:
            self.vx = 0

        if self.keyHandler[UP] and self.y + 2 * self.r == self.g:
            self.vy = -10

        self.x += self.vx
        self.y += self.vy

        for d in g.diamonds:
            if self.distance(d) <= self.r + d.r and d.v == "f":
                g.diamonds.remove(d)
                self.dmndCnt1 += 1

        for l in g.lava:
            if self.distance(l) <= 2 * self.r + l.r and l.v == "w":
                print("Game over boy")
       # for button in g.buttons: 
        #    if self.distance(button) <= self.r + d.r and d.v == "p":
                #move purple bar down while standing
          #  elif self.distance(button) <= self.r + d.r and d.v == "y":
                #move the yellow bar
                
    def distance(self, target):
        return ((self.x - target.x) ** 2 + (self.y - target.y) ** 2) ** 0.5


class Watergirl(Creature):

    def __init__(self, x, y, r, g, img):
        Creature.__init__(self, x, y, r, g, img)
        self.keyHandler = {LEFT: False, RIGHT: False, UP: False}
        self.girlLeft = loadImage(path + "images/" + img + "_left" + ".png")
        self.girlRight = loadImage(path + "images/" + img + "_right" + ".png")
        self.dmndCnt2 = 0

    def update(self):
        self.gravity()
        if self.x-self.r/2>=0 and self.x<=1000 and self.keyHandler[LEFT]:
            if self.stop_x == False:
                self.vx = -8
                self.direction2 = -1
            else:
                self.vx = 0
        elif self.x>=0 and self.x+2*self.r<=1000 and self.keyHandler[RIGHT]:
            if self.stop_x == False:
                self.vx = 8
                self.direction2 = 1
            else:
                self.vx = 0
        else:
            self.vx = 0

        if self.keyHandler[UP] and self.y + 2 * self.r == self.g:
            self.vy = -10

        self.x += self.vx
        self.y += self.vy

        for d in g.diamonds:
            if self.distance(d) <= self.r + d.r and d.v == "w":
                g.diamonds.remove(d)

        for l in g.lava:
            if self.distance(l) <= 2 * self.r + l.r and l.v == "f":
                print("game over, girl")
                
        # for button in g.buttons: 
        #     if self.distance(button) <= self.r + d.r and d.v == "p":
        #         #move purple bar down while standing on it, move back up otherwise 
        #     elif self.distance(button) <= self.r + d.r and d.v == "y":
        #         #move the yellow bar
    def distance(self, target):
        return ((self.x - target.x-target.w/2) ** 2 + (self.y - target.y) ** 2) ** 0.5

class Platform:

    def __init__(self, x, y, w, h, img):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = loadImage(path + "images/" + img)

    def display(self):
        image(self.img, self.x - g.x, self.y, self.w, self.h)
        
class Doors:
    def __init__(self, x, y, w, h, img):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = loadImage(path + "images/" + img)

    def display(self):
        image(self.img, self.x - g.x, self.y, self.w, self.h)
        
class Bars:
    def __init__(self, x, y, w, h, img):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = loadImage(path + "images/" + img)

    def display(self):
        image(self.img, self.x - g.x, self.y, self.w, self.h)
    
    
class Diamond:

    def __init__(self, x, y, w, h, img, r, v):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = loadImage(path + "images/" + img)
        self.r = r
        self.v = v

    def display(self):
        image(self.img, self.x - g.x, self.y, self.w, self.h)

class Lava:

    def __init__(self, x, y, r, w, h, img, v):
        self.x = x
        self.y = y
        self.r = r
        self.w = w
        self.h = h
        self.img = loadImage(path + "images/" + img)
        self.v = v

    def display(self):
        image(self.img, self.x - g.x, self.y, self.w, self.h)
        
class Buttons:
    def __init__(self, x, y, r, w, h, img, v):
        self.x = x
        self.y = y
        self.r = r
        self.w = w
        self.h = h
        self.img = loadImage(path + "images/" + img)
        self.v = v

    def display(self):
        image(self.img, self.x - g.x, self.y, self.w, self.h)
        
class Game:

    def __init__(self, w, h, g):
        self.x = 0
        self.w = w
        self.h = h
        self.g = g
        self.fireboy = Fireboy(0, 650, 30, self.g, "boy")
        self.watergirl = Watergirl(0, 560, 30, self.g, "girl")
        self.platforms = []
        self.diamonds = []
        self.lava = []
        self.doors=[]
        self.bars=[]
        self.buttons=[]
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
                self.lava.append(Lava(int(l[1]),int(l[2]),15,int(l[3]),int(l[4]), "lava.PNG", "f"))
            elif l[0]=="water":
                self.lava.append(Lava(int(l[1]),int(l[2]),15,int(l[3]),int(l[4]), "water.png", "w"))
            elif l[0]=="boy_door":
                self.doors.append(Doors(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "boy door closed.PNG"))
            elif l[0]=="girl_door":
                self.doors.append(Doors(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "girl door closed.PNG"))
            elif l[0]=="purple_bar":
                self.bars.append(Bars(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "purple bar.PNG"))
            elif l[0]=="yellow_bar":
                self.bars.append(Bars(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "yellow bar.PNG"))
            elif l[0]=="yellow button":
                self.bars.append(Bars(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "yellow button.png"))
            elif l[0]=="purple button":
                self.bars.append(Bars(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "purple button.PNG"))
    
    def display(self):
        for p in self.platforms:
            p.display()

        for d in self.diamonds:
            d.display()

        for l in self.lava:
            l.display()
        
        for d in self.doors:
            d.display()
            
        for b in self.bars:
            b.display()
            
        for button in self.buttons:
            button.display()
            
        self.fireboy.display()
        self.watergirl.display()

   # def checkwin():
        #if all diamonds are collected
        #if both characters are in the right position: 
            #open the doors
            #display a "game won" image, with a time score
g = Game(1000, 750, 750)

def setup():
    size(g.w, g.h)

bg = loadImage(path + "images/background.png")

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

    elif key == "a":
        g.watergirl.keyHandler[LEFT] = True
    elif key == "d":
        g.watergirl.keyHandler[RIGHT] = True
    elif key == "w":
        g.watergirl.keyHandler[UP] = True


def keyReleased():
    if keyCode == LEFT:
        g.fireboy.keyHandler[LEFT] = False
    elif keyCode == RIGHT:
        g.fireboy.keyHandler[RIGHT] = False
    elif keyCode == UP:
        g.fireboy.keyHandler[UP] = False

    elif key == "a":
        g.watergirl.keyHandler[LEFT] = False
    elif key == "d":
        g.watergirl.keyHandler[RIGHT] = False
    elif key == "w":
        g.watergirl.keyHandler[UP] = False

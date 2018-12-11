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
            #print(self.y, p.y, ":", self.vy, self.y - p.y - p.h + 10)
            
            if self.x + self.r >= p.x and self.x <= p.x + p.w - self.r:
                if self.y + 2 * self.r <= p.y:
                    self.g = p.y
               
                elif self.y + self.vy <= p.y + p.h -10 and self.y >= p.y + p.h - 10:
                    
                    self.vy = self.y - p.y - p.h + 10
                    
            # if self.x + self.r >= p.x + p.w: #and self.y <= p.y + p.h - self.r:
            #     self.stop_x = True
      
            #     if 
            # if self.y <= p.y + p.h and self.x + self.r >= p.x and self.x <= p.x + p.w - self.r:
            #     print("fg")
            #     self.vy = 5
        
        # elif self.y+self.r>=p.y+p.h and self.y<=p.y and self.x+self.r >= p.x and self.x-self.r <= p.x+p.w/1.35:
        # elif self.y+self.r>=p.y+p.h and self.y<=p.y and self.x+self.r >= p.x and self.x <= p.x+p.w:
        #     self.y+=1
        #     self.vy=0
        #     self.vy=5
        # self.g = g.g
            
                
        # for p in g.platforms:
        #     if self.y + 2*self.r <= p.y and self.x + 2*self.r >= p.x and self.x <= p.x + p.w:
        #         self.g = p.y

        # for p in g.platforms:
        # if self.y >= p.y + p.h and  self.x + 2*self.r >= p.x and self.x <= p.x + p.w:
        #     if self.y >= p.y + p.h:
        # self.y += 1
        #         print('check')
        #         self.vy = 3

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

        # ellipse(self.x + self.r, self.y + self.r, self.r * 2, self.r * 2)


class Fireboy(Creature):

    def __init__(self, x, y, r, g, img):
        Creature.__init__(self, x, y, r, g, img)
        self.keyHandler = {LEFT: False, RIGHT: False, UP: False}
        self.boyLeft = loadImage(path + "images/" + img + "_left" + ".png")
        self.boyRight = loadImage(path + "images/" + img + "_right" + ".png")
        self.dmndCnt1 = 0

    def update(self):
        self.gravity()

        if self.keyHandler[LEFT]:
            if self.stop_x == False:
                self.vx = -5
                self.direction1 = -1
            else:
                self.vx = 0
        elif self.keyHandler[RIGHT]:
            if self.stop_x == False:
                self.vx = 5
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
            if self.distance(d) <= 2 * self.r + d.r and d.v == "f":
                g.diamonds.remove(d)
                self.dmndCnt1 += 1

        for l in g.lava:
            if self.distance(l) <= 2 * self.r + l.r and l.v == "w":
                print("Game over boy")

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

        if self.keyHandler[LEFT]:
            if self.stop_x == False:
                self.vx = -5
                self.direction2 = -1
            else:
                self.vx = 0
        elif self.keyHandler[RIGHT]:
            if self.stop_x == False:
                self.vx = 5
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
            if self.distance(d) <= 2 * self.r + d.r and d.v == "w":
                g.diamonds.remove(d)

    def distance(self, target):
        return ((self.x - target.x) ** 2 + (self.y - target.y) ** 2) ** 0.5

class Platform:

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
                self.lava.append(Lava(int(l[1]),int(l[2]),15,int(l[3]),int(l[4]), "lava.png", "f"))
            elif l[0]=="water":
                self.lava.append(Lava(int(l[1]),int(l[2]),15,int(l[3]),int(l[4]), "water.png", "w"))

    def display(self):
        for p in self.platforms:
            p.display()

        for d in self.diamonds:
            d.display()

        for l in self.lava:
            l.display()

        self.fireboy.display()
        self.watergirl.display()


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

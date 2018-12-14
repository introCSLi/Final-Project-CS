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
                    self.vy = self.y - p.y - p.h + 10
                    

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
            self.vx = -8
            self.direction1 = -1
        elif self.x>=0 and self.x+2*self.r<=1000 and self.keyHandler[RIGHT]:
            self.vx = 8
            self.direction1 = 1
        else:
            self.vx = 0

        if self.keyHandler[UP] and self.y + 2 * self.r == self.g:
            self.vy = -11

        self.x += self.vx
        self.y += self.vy

        for d in g.diamonds:
            if self.distance(d) <= 2 * self.r + d.r and d.v == "f":
                g.diamonds.remove(d)
                self.dmndCnt1 += 1

        for l in g.lava:
            if self.x + self.r >= l.x and self.x + self.r <= l.x + l.w and self.y + 2*self.r >= l.y and self.y + 2*self.r <= l.y + l.h and l.v == 'w':
                image(g.gameOver, g.w/2 - 250, g.h/2 - 90)
                textSize(30)
                text("press space to restart", g.w/2 - 160, g.h/2 + 140)
                g.endOfGame = True
    
        for d in g.doors:
            if self.distance(d) <= self.r and d.v == 'b':
                d.boy_door_open = True 
            else:
                d.boy_door_open = False    
        
            

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
            self.vx = -8
            self.direction2 = -1
        elif self.x>=0 and self.x+2*self.r<=1000 and self.keyHandler[RIGHT]:
            self.vx = 8
            self.direction2 = 1
        else:
            self.vx = 0

        if self.keyHandler[UP] and self.y + 2 * self.r == self.g:
            self.vy = -11

        self.x += self.vx
        self.y += self.vy

        for d in g.diamonds:
            if self.distance(d) <= 2 * self.r + d.r and d.v == "w":
                g.diamonds.remove(d)
                
        for l in g.lava:
            if self.x + self.r >= l.x and self.x + self.r <= l.x + l.w and self.y + 2*self.r >= l.y and self.y + 2*self.r <= l.y + l.h and l.v == 'f':
                image(g.gameOver, g.w/2 - 250, g.h/2 - 90)
                textSize(30)
                text("press space to restart", g.w/2 - 160, g.h/2 + 140)
                g.endOfGame = True
    
        for d in g.doors:
            if self.distance(d) <= d.w/2 and d.v == 'g':
                d.girl_door_open = True 
            else:
                d.girl_door_open = False

    def distance(self, target):
        return ((self.x - target.x) ** 2 + (self.y - target.y) ** 2) ** 0.5
    
class Doors:
    def __init__(self, x, y, w, h, img, v):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = loadImage(path + "images/" + img)
        self.v = v
        self.boy_door_open = False
        self.girl_door_open = False
        self.boy_open = loadImage(path + "images/boy_door_open.png")
        self.girl_open = loadImage(path + "images/girl_door_open.png")
 
    def display(self):
        if self.boy_door_open == False and self.v == 'b':
            image(self.img, self.x - g.x, self.y, self.w, self.h)
        elif self.boy_door_open == True and self.v == "b":
            image(self.boy_open, self.x - g.x, self.y, self.w, self.h)
        if self.girl_door_open == False and self.v == 'g':
            image(self.img, self.x - g.x, self.y, self.w, self.h)
        elif self.girl_door_open == True and self.v == "g":
            image(self.girl_open, self.x - g.x, self.y, self.w, self.h)
        g.checkWin()
            
         
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
         
class Bars:
     def __init__(self, x, y, w, h, img):
         self.x = x
         self.y = y
         self.w = w
         self.h = h
         self.img = loadImage(path + "images/" + img)
 
     def display(self):
         image(self.img, self.x - g.x, self.y, self.w, self.h)

class Game:

    def __init__(self, w, h, g, levelTwo):
        self.x = 0
        self.w = w
        self.h = h
        self.g = g
        self.fireboy = Fireboy(0, 650, 30, self.g, "boy")
        self.watergirl = Watergirl(0, 560, 30, self.g, "girl")
        self.gameOver = loadImage(path + "images/game_over.png")
        self.levelTwo = levelTwo
        self.endOfGame = False
        self.platforms = []
        self.diamonds = []
        self.lava = []
        self.buttons=[]
        self.doors=[]
        self.bars=[]
        
        
        if self.levelTwo == False:
            f = open(path+"/setUpGame_1.csv","r")
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
                elif l[0]=="boy_door":
                    self.doors.append(Doors(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "boy_door_closed.png", "b"))
                elif l[0]=="girl_door":
                    self.doors.append(Doors(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "girl_door_closed.png", "g"))
                elif l[0]=="purple_bar":
                    self.bars.append(Bars(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "purple_bar.png"))
                elif l[0]=="water":
                    self.lava.append(Lava(int(l[1]),int(l[2]),15,int(l[3]),int(l[4]), "water.png", "w"))
                elif l[0]=="yellow_bar":
                    self.bars.append(Bars(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "yellow_bar.png"))
                elif l[0]=="yellow_button":
                    self.bars.append(Bars(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "yellow_button.png"))
                elif l[0]=="purple_button":
                    self.bars.append(Bars(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "purple_button.png"))
        else:
            f = open(path+"/setUpGame_2.csv","r")
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
                elif l[0]=="boy_door":
                    self.doors.append(Doors(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "boy_door_closed.png", "b"))
                elif l[0]=="girl_door":
                    self.doors.append(Doors(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "girl_door_closed.png", "g"))
                elif l[0]=="purple_bar":
                    self.bars.append(Bars(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "purple_bar.png"))
                elif l[0]=="water":
                    self.lava.append(Lava(int(l[1]),int(l[2]),15,int(l[3]),int(l[4]), "water.png", "w"))
                elif l[0]=="yellow_bar":
                    self.bars.append(Bars(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "yellow_bar.png"))
                elif l[0]=="yellow_button":
                    self.bars.append(Bars(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "yellow_button.png"))
                elif l[0]=="purple_button":
                    self.bars.append(Bars(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "purple_button.png"))
                    
                    
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
        
    def checkWin(self):
        cnt = 0
        for d in self.doors:
            if d.boy_door_open == True:
                cnt += 1
            if d.girl_door_open == True:
                cnt += 1
        if cnt == 2:
            g.__init__(1000, 750, 750, True)
        
    


g = Game(1000, 750, 750, False)

def setup():
    size(g.w, g.h)

bg = loadImage(path + "images/background.png")

def draw():
    if not g.endOfGame:
        background(bg)
        g.display()


def keyPressed():
    # code for space is 32
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
        
    if g.endOfGame == True and keyCode == 32:
        g.__init__(1000, 750, 750, g.levelTwo) 

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

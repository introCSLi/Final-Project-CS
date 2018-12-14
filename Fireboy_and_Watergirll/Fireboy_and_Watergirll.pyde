import os, random, time
path = os.getcwd() + "/"
add_library('minim')
player = Minim(this)

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
        
        #checking for collision with the platforms: if the character jumps and there's a platform above, 
        #he won't jump over it; if there's a platform below him, he'll stand on it
        for p in g.platforms:
            if self.x + self.r >= p.x and self.x <= p.x + p.w - self.r:
                if self.y + 2 * self.r <= p.y and self.g > p.y:
                    self.g = p.y
                elif self.y + self.vy <= p.y + p.h -10 and self.y >= p.y + p.h - 10:
                    self.vy = self.y - p.y - p.h + 10
                    
        #checking for collision with the bars, making sure the characters follow them on screen
        for bar in g.bars:
            if self.x + self.r >= bar.x and self.x <= bar.x + bar.w - self.r:
                if self.y + 2 * self.r <= bar.y and self.g > bar.y:
                    if bar.state == 0:
                        self.g = bar.y
                    elif bar.state == 2:
                        self.y -= 1
                        self.g = bar.y - 1
                    elif bar.state == 1:
                        self.y += 0
                        self.g = bar.y + 1
                elif self.y + self.vy <= bar.y + bar.h -10 and self.y >= bar.y + bar.h - 10:
                    self.vy = self.y - bar.y - bar.h + 10
                    

    def update(self):
        self.gravity()
        self.x += self.vx
        self.y += self.vy

    def display(self):
        self.update()
        
        #changing the direction for displaying pictures of the characters
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
        self.stop_x1 = False
    
    def update(self):
        self.gravity()
        
        #prevents fireboy from leaving the premises of the screen
        if self.x-self.r/2>=0 and self.x<=1000 and self.keyHandler[LEFT]:
            if self.stop_x1 == False:
                self.vx = -8
                self.direction1 = -1
        elif self.x>=0 and self.x+2*self.r<=1000 and self.keyHandler[RIGHT]:
            if self.stop_x1 == False:
                self.vx = 8
                self.direction1 = 1
        else:
            self.vx = 0

        if self.keyHandler[UP] and self.y + 2 * self.r == self.g:
            self.vy = -11

        self.x += self.vx
        self.y += self.vy
        
        for p in g.platforms: 
            if self.y + self.r >= p.y and self.y + self.r <= p.y + p.h and ( abs(self.x + self.r - (p.x + p.w))< 10 or abs(self.x + self.r - p.x)< 10):
                self.stop_x1 = True
            else:
                self.stop_x1 = False
        
        #collecing the diamonds
        for d in g.diamonds:
            if self.distance(d) <= self.r + d.r and d.v == "f":
                self.dmndCnt1 += 1
                g.dmndSound.rewind()
                g.dmndSound.play()
                g.diamonds.remove(d)
                
        
        #if the character steps on lava, the game restarts
        for l in g.lava:
            if self.x + self.r >= l.x and self.x + self.r <= l.x + l.w and self.y + 2*self.r >= l.y and self.y + 2*self.r <= l.y + l.h and l.v == 'w':
                image(g.gameOver, g.w/2 - 250, g.h/2 - 90)
                textSize(30)
                text("press space to restart", g.w/2 - 160, g.h/2 + 140)
                g.gameOverSound.rewind()
                g.gameOverSound.play()
                g.endOfGame = True
        
        #changing the conditions to open the doors
        for d in g.doors:
            if self.distance(d) <= self.r and d.v == 'b':
                d.boy_door_open = True 
            else:
                d.boy_door_open = False  
                  
        #pressing the buttons, platforms go down
        for button in g.buttons: 
            if self.distance(button) <= 45:
                button.button_pressed_boy= True
            elif self.distance(button) > 45:
                button.button_pressed_boy=False
                
    #measuring the distance between the character and an object    
    def distance(self, target):
        return ((self.x - target.x) ** 2 + (self.y - target.y) ** 2) ** 0.5


class Watergirl(Creature):

    def __init__(self, x, y, r, g, img):
        Creature.__init__(self, x, y, r, g, img)
        self.keyHandler = {LEFT: False, RIGHT: False, UP: False}
        self.girlLeft = loadImage(path + "images/" + img + "_left" + ".png")
        self.girlRight = loadImage(path + "images/" + img + "_right" + ".png")
        self.dmndCnt2 = 0
        self.stop_x2 = False

    def update(self):
        self.gravity()
        
        #prevents fireboy from leaving the premises of the screen
        if self.x-self.r/2>=0 and self.x<=1000 and self.keyHandler[LEFT]:
            if self.stop_x2 == True:
                self.vx *= -1
                return
            self.vx = -8
            self.direction2 = -1
        elif self.x>=0 and self.x+2*self.r<=1000 and self.keyHandler[RIGHT]:
            if self.stop_x2 == True:
                self.vx *= -1
                return
            self.vx = 8
            self.direction2 = 1
        else:
            self.vx = 0

        if self.keyHandler[UP] and self.y + 2 * self.r == self.g:
            self.vy = -11

        self.x += self.vx
        self.y += self.vy
        
        #collecing the diamonds
        for d in g.diamonds:
            if self.distance(d) <= self.r + d.r and d.v == "w":
                self.dmndCnt2 += 1
                g.dmndSound.rewind()
                g.dmndSound.play()
                g.diamonds.remove(d)
                
        #if the character steps on water, the game restarts
        for l in g.lava:
            if self.x + self.r >= l.x and self.x + self.r <= l.x + l.w and self.y + 2*self.r >= l.y and self.y + 2*self.r <= l.y + l.h and l.v == 'f':
                image(g.gameOver, g.w/2 - 250, g.h/2 - 90)
                textSize(30)
                text("press space to restart", g.w/2 - 160, g.h/2 + 140)
                g.gameOverSound.rewind()
                g.gameOverSound.play()
                g.endOfGame = True
    
        #changing the conditions to open the doors
        for d in g.doors:
            if self.distance(d) <= d.w/2 and d.v == 'g':
                d.girl_door_open = True 
            else:
                d.girl_door_open = False
                
        #pressing the buttons, platforms go down
        for button in g.buttons: 
            if self.distance(button) <= 45:
                button.button_pressed_girl= True
            elif self.distance(button) > 45:
                button.button_pressed_girl=False


                
    #measuring the distance between the character and an object    
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
 
    #displaying the closed/opened doors depending on whether the characters stand in front of them
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
    def __init__(self, x, y, w, h, col, img, v):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.col = col
        self.img = loadImage(path + "images/" + img)
        self.v = v
        self.button_pressed_boy = False
        self.button_pressed_girl = False
        self.button_held = False

    def display(self):
        image(self.img, self.x - g.x, self.y, self.w, self.h)
        
        if (self.button_pressed_boy == True or self.button_pressed_girl == True) and self.button_held == False:
            print('click')
            self.button_held = True
            for bar in g.bars:
                if bar.v==self.col:
                    bar.button_pressed = True
        elif (self.button_pressed_boy == False and self.button_pressed_girl == False) and self.button_held == True:
            print('clack')
            self.button_held = False
            for bar in g.bars:
                if bar.v==self.col:
                    bar.button_pressed = False
            
            
         
class Bars:
    def __init__(self, x, y, w, h, img, v, bot):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.v=v
        self.img = loadImage(path + "images/" + img)
        self.vy=0
        self.button_pressed = False
        #0 - standing, 1 - going down, 2 - going up
        self.state = 0
        
        self.top = y
        self.bot = bot
        

    def display(self):
        image(self.img, self.x - g.x, self.y, self.w, self.h)
        if self.button_pressed == True:
            if self.y < self.bot:
                self.y += 1
                self.state = 1
            else:
                self.state = 0
        else:
            if self.y > self.top:
                self.y -= 1
                self.state = 2
            else:
                self.state = 0

class Game:

    def __init__(self, w, h, g, levelTwo):
        self.x = 0
        self.w = w
        self.h = h
        self.g = g
        self.fireboy = Fireboy(0, 650, 30, self.g, "boy")
        self.watergirl = Watergirl(0, 560, 30, self.g, "girl")
        self.gameOver = loadImage(path + "images/game_over.png")
        #levelTwo is responsible for switching to the second level of the game
        self.levelTwo = levelTwo
        #if we're on level 2, two images that will be used at the end of the game are loaded
        if self.levelTwo == True:
            self.endPic = loadImage(path + "images/end.png")
            self.gameWin = loadImage(path + "images/win.png")
        self.endOfGame = False
        self.platforms = []
        self.diamonds = []
        self.lava = []
        self.buttons=[]
        self.doors=[]
        self.bars=[]
        self.flag = 0
        self.amDmnd = 0
        self.dmndSound = player.loadFile(path+"sounds/diamond.mp3")
        self.winSound = player.loadFile(path+"sounds/win.mp3")
        self.levelUp = player.loadFile(path+"sounds/level.mp3")
        self.gameOverSound = player.loadFile(path+"sounds/game_over.mp3")
        
        #depending on the level, we iterate through different .csv files to set up the levels
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
                    self.amDmnd += 1
                elif l[0]=="blue":
                    self.diamonds.append(Diamond(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "diamond_water.png",15,"w"))
                    self.amDmnd += 1
                elif l[0]=="lava":
                    self.lava.append(Lava(int(l[1]),int(l[2]),15,int(l[3]),int(l[4]), "lava.png", "f"))
                elif l[0]=="water":
                    self.lava.append(Lava(int(l[1]),int(l[2]),15,int(l[3]),int(l[4]), "water.png", "w"))
                elif l[0]=="boy_door":
                    self.doors.append(Doors(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "boy_door_closed.png", "b"))
                elif l[0]=="girl_door":
                    self.doors.append(Doors(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "girl_door_closed.png", "g"))
                elif l[0]=="purple_bar":
                    self.bars.append(Bars(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "purple_bar.png", "p",  395))
                elif l[0]=="yellow_bar":
                    self.bars.append(Bars(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "yellow_bar.png", "y", 520 ))
                elif l[0]=="yellow_button":
                    self.buttons.append(Buttons(int(l[1]),int(l[2]),int(l[3]),int(l[4]),"y", "yellow_button.png", "y"))
                elif l[0]=="purple button1":
                    self.buttons.append(Buttons(int(l[1]),int(l[2]),int(l[3]),int(l[4]),"p", "purple_button.png", "p1"))
                elif l[0]=="purple button2":
                    self.buttons.append(Buttons(int(l[1]),int(l[2]),int(l[3]),int(l[4]),"p", "purple_button.png", "p2"))
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
                    self.amDmnd += 1
                elif l[0]=="blue":
                    self.diamonds.append(Diamond(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "diamond_water.png",15,"w"))
                    self.amDmnd += 1
                elif l[0]=="lava":
                    self.lava.append(Lava(int(l[1]),int(l[2]),15,int(l[3]),int(l[4]), "lava.png", "f"))
                elif l[0]=="water":
                    self.lava.append(Lava(int(l[1]),int(l[2]),15,int(l[3]),int(l[4]), "water.png", "w"))
                elif l[0]=="boy_door":
                    self.doors.append(Doors(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "boy_door_closed.png", "b"))
                elif l[0]=="girl_door":
                    self.doors.append(Doors(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "girl_door_closed.png", "g"))
                elif l[0]=="purple_bar":
                    self.bars.append(Bars(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "purple_bar.png", "p",  460))
                elif l[0]=="yellow_bar":
                    self.bars.append(Bars(int(l[1]),int(l[2]),int(l[3]),int(l[4]), "yellow_bar.png", "y", 625 ))
                elif l[0]=="yellow_button":
                    self.buttons.append(Buttons(int(l[1]),int(l[2]),int(l[3]),int(l[4]),"y", "yellow_button.png", "y"))
                elif l[0]=="purple_button1":
                    self.buttons.append(Buttons(int(l[1]),int(l[2]),int(l[3]),int(l[4]),"p", "purple_button.png", "p1"))
                elif l[0]=="purple_button2":
                    self.buttons.append(Buttons(int(l[1]),int(l[2]),int(l[3]),int(l[4]),"p", "purple_button.png", "p2"))
                    
                    
    def display(self):
        for p in self.platforms:
            p.display()

        for d in self.diamonds:
            d.display()

        for l in self.lava:
            l.display()
        
        for d in self.doors:
             d.display()
        if self.endOfGame == False:
                
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
                
        #if both doors are open on level one, we move to the level two
        #if both doors are open on level two, the game is won
        if cnt == 2:
            if self.levelTwo == True:
                self.flag = 1
                image(self.endPic, 0, 0)
                image(self.gameWin, self.w/2 - 250, self.h/2 - 250)
                textSize(25)
                if (self.fireboy.dmndCnt1 + self.watergirl.dmndCnt2) == self.amDmnd:
                    text("congrats, you have collected all the diamonds", g.w/2 - 270, g.h/2 + 320)
                else:
                    text("you did not collect all the diamonds, but nice try.",g.w/2 - 270, g.h/2 + 320)
                textSize(30)
                text("to play again, press enter", g.w/2 - 180, g.h/2 + 280)
                self.winSound.rewind()
                self.winSound.play()
                g.endOfGame = True
                return 
            self.levelUp.rewind()
            self.levelUp.play()
            g.__init__(1000, 750, 750, True)
    
#initializing the game, starting with level one
g = Game(1000, 750, 750, False)

def setup():
    size(g.w, g.h)

bg = loadImage(path + "images/background.png")

def draw():
    if not g.endOfGame:
        background(bg)
        g.display()

   
def keyPressed():
    #moving the characters
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
    #used to restart the level after the user stepped in lava
    if g.endOfGame == True and keyCode == 32:
        g.__init__(1000, 750, 750, g.levelTwo) 
    #used to restart the game when the user finished both levels
    if g.endOfGame == True and g.levelTwo == True and g.flag == 1 and keyCode == 10:
        g.__init__(1000, 750, 750, False)

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

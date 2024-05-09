import pygame
import random
import math
waddles = pygame.image.load('images/waddles.png') #load your spritesheet
waddles.set_colorkey((255, 0, 255))

#contants
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4

class enemy:
    def __init__ (self, x, y):
        
        #player variable
        self.xpos = x
        self.ypos = y
        self.vx = 0
        self.vy = 0
        self.frameWidth = 69
        self.frameHeight = 69
        self.RowNum = 2
        self.frameNum = 0
        self.ticker = 0
        self.direction = "None"
        self.isAlive = True

    def move(self, map, ticker, px, py):

        if ticker % 40 == 0:
            num = random.randrange(0,4)
            if num == 0:
                self.vx = 3
                self.RowNum = 3
                self.direction = RIGHT #teacher gave left and right but i added down and up 
            elif num == 1:
                self.vx = -3
                self.RowNum = 2
                self.direction = LEFT
            elif num == 2:
                self.vy = 3
                self.RowNum = 1
                self.direction = DOWN
            elif num == 3:
                self.vy = -3
                self.RowNum = 0
                self.direction = UP
            else:
                self.vy = 0
                self.vx = 0

        if self.vx !=  0 or self.vy != 0: #left animation
            self.ticker+=1
            if self.ticker%10==0: #only change frames every 10 ticks
              self.frameNum+=1
            if self.frameNum>3: 
               self.frameNum = 0
        
        if abs(int(py/50) - int(self.ypos/50))<2: #teacher provided right and left and alex/partner helped me with the other two
            if px < self.xpos:
                self.xpos-=3
                self.direction = LEFT
            else:
                self.xpos+=3
                self.direction = RIGHT
       
        if abs(int(px/50) - int(self.xpos/50))<2:
            if py < self.ypos:
                self.ypos-=3
                self.direction = UP
            else:
                self.ypos+=3
                self.direction = DOWN


        
        if self.direction == RIGHT and map[int((self.ypos ) /50)][int( (self.xpos + 20) / 50)] ==2: #was provide with left an right and i added 
            self.direction = UP
            self.xpos -= 3
        if self.direction == LEFT and map[int((self.ypos ) /50)][int( (self.xpos - 20) / 50)] == 2:
            self.direction = DOWN
            self.xpos += 3
        if self.direction == UP and map[int((self.ypos ) /50)][int( (self.xpos + 20) / 50)] ==2:
            self.direction = RIGHT
            self.xpos -= 3
        if self.direction == DOWN and map[int((self.ypos ) /50)][int( (self.xpos - 20) / 50)] == 2:
            self.direction = LEFT
            self.xpos+= 3

        if self.direction == RIGHT:# was provided with right and left and i added up and down
            self.xpos += 3
        elif self.direction == LEFT:
            self.xpos -= 3
        elif self.direction == UP:
            self.xpos += 3
        elif self.direction == DOWN:
            self.xpos -= 3
    def draw(self, screen):
        if self.isAlive == True:
            screen.blit(waddles, (self.xpos, self.ypos), (self.frameWidth*self.frameNum, self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))
    
    def die(self, ballx, bally):
        if math.sqrt((self.xpos-ballx)**2 + (self.ypos-bally)**2) <= 20:
            self.isAlive = False
    def talk(self):
        num = random.randrange(0,3)
        if num == 0:
            print("onik onik !!!")
        if num == 1:
            print("hey hey you im gonna get you!!")
        else:
            print(" i hate you!!")
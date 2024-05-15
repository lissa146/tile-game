import pygame
import random
import math
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 20)
NPC = pygame.image.load('images/npc2.png') #load your spritesheet
NPC.set_colorkey((255, 255, 255))
#contants
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4

class npc:
    def __init__ (self, x, y):
        
        #player variable
        self.xpos = 100
        self.ypos = 400
        self.vx = 0
        self.vy = 0
        self.frameWidth = 45
        self.frameHeight = 69
        self.RowNum = 2
        self.frameNum = 0
        self.ticker = 0
        self.direction = RIGHT
        self.isAlive = True
        self.isTalking = False
        self.talkTimer = 0
        self.label = "howdy"
        self.text_surface = font.render(self.label, False, (255,255,255))


    def draw(self, screen, ticker):
            screen.blit(NPC, (self.xpos, self.ypos), (self.frameWidth*self.frameNum, self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))
            if self.isAlive == True:
                pygame.draw.circle(screen, (0, 250, 250), (self.xpos, self.ypos), 10)
            if ticker-self.talkTimer < 200:
                pygame.draw.rect(screen, (0,0,0), (self.xpos, self.ypos, 120, 30))
                screen.blit(self.text_surface, (self.xpos+50, self.ypos+10))
            else:
                self.isTalking = False
    
    def move(self,ticker, map):

        if self.ticker % 40 == 0:
            num = random.randrange(0,4)
            if num == 0:
                self.vx = 3
                self.RowNum = 3
                self.direction = RIGHT
                 #teacher gave left and right but i added down and up 
            elif num == 1:
                self.vx = 3
                self.RowNum = 3
                self.direction = LEFT
                self.vx = -3
                self.RowNum = 2
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

        if self.direction == RIGHT:# was provided with right and left and i added up and down
            self.xpos += 3
        elif self.direction == LEFT:
            self.xpos -= 3
        elif self.direction == UP:
            self.xpos += 3
        elif self.direction == DOWN:
            self.xpos -= 3

    def talk(self, ticker):
        if self.isTalking == False:
            self.talkTimer = ticker
            self.isTalking = True
            num = random.randrange(0,3)
            if num ==0:
                self.label = "howdy"
            elif num == 1:
                 self.label = "birds arent reall!!!!!!"
            elif num == 2:
                 self.label = "i love dounuts!!!!!!!!!!"
            else:
                 self.label = "tess tess tess tess tess tess"

            self.text_surface = font.render(self.label, False, (255,255,255))




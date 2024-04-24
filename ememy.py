import pygame
import random
import math

#contants
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4

class enemy:
    def __init__ (self):
        
        #player variable
        self.xpos = 400
        self.ypos = 200
        self.vx = 0
        self.vy = 0
        self.frameWidth = 69
        self.frameHeight = 69
        self.RowNum = 2
        self.frameNum = 0
        self.ticker = 0
        self.direction = "None"
        self.isAlive = True

    def move(self, map, ticker, player):

        if ticker % 40 == 0:
            num = random.randrange(0,4)
            if num == 0:
                self.direction = RIGHT #teacher gave left and right but i added down and up 
            elif num == 1:
                self.direction = LEFT
            elif num == 2:
                self.direction = DOWN
            elif num == 3:
                self.direction = UP
        
        if abs(int(player.ypos/50) - int(self.ypos/50))<2:
            if player.xpos < self.xpos:
                self.xpos-=3
                self.direction = LEFT
            else:
                self.xpos+=3
                self.direction = RIGHT
       
        if abs(int(player.xpos/50) - int(self.xpos/50))<2:
            if player.ypos < self.ypos:
                self.ypos-=3
                self.direction = UP
            else:
                self.ypos+=3
                self.direction = DOWN

        
        if self.direction == RIGHT and map[int((self.ypos ) /50)][int( (self.xpos + 20) / 50)] ==2:
            self.direction = UP
            self.xpos -= 6
        if self.direction == LEFT and map[int((self.ypos ) /50)][int( (self.xpos - 20) / 50)] == 2:
            self.direction = DOWN
            self.xpos += 6
        if self.direction == UP and map[int((self.ypos ) /50)][int( (self.xpos + 20) / 50)] ==2:
            self.direction = RIGHT
            self.xpos -= 6
        if self.direction == DOWN and map[int((self.ypos ) /50)][int( (self.xpos - 20) / 50)] == 2:
            self.direction = LEFT
            self.xpos+= 6

        if self.direction == RIGHT:
            self.xpos += 3
        elif self.direction == LEFT:
            self.xpos -= 3
        elif self.direction == UP:
            self.xpos += 3
        elif self.direction == DOWN:
            self.xpos -= 3
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 255), (self.xpos, self.ypos, 30, 30))

    def die(self, ballx, bally):
        if math.sqrt((self.xpos-ballx)**2 + (self.ypos-bally)**2) <= 20:
            self.isAlive = False
        

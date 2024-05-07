import pygame
import random
import math

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
        self.ypos = 500
        self.vx = 0
        self.vy = 0
        self.frameWidth = 69
        self.frameHeight = 69
        self.RowNum = 2
        self.frameNum = 0
        self.ticker = 0
        self.direction = "None"

    def draw(self, screen):
            pygame.draw.rect(screen, (255, 0, 255), (self.xpos, self.ypos, 30, 30))
    
    def move(self,ticker, map):

        if self.ticker % 40 == 0:
            num = random.randrange(0,4)
            if num == 0:
                self.direction = RIGHT #teacher gave left and right but i added down and up 
            elif num == 1:
                self.direction = LEFT
            elif num == 2:
                self.direction = DOWN
            elif num == 3:
                self.direction = UP

        if self.direction == RIGHT:# was provided with right and left and i added up and down
            self.xpos += 3
        elif self.direction == LEFT:
            self.xpos -= 3
        elif self.direction == UP:
            self.xpos += 3
        elif self.direction == DOWN:
            self.xpos -= 3

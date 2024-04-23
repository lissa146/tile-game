import pygame
import random

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
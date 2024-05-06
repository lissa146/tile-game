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

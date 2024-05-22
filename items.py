import pygame
pygame.init()

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4

class item:
    def __init__ (self, x, y,type):
        
        #player variable
        self.xpos = x
        self.ypos = y
        self.vx = 0
        self.vy = 0
        self.frameWidth = 45
        self.frameHeight = 69
        self.RowNum = 2
        self.frameNum = 0
        self.ticker = 0
        self.isAlive = True
        self.type = type
        self.collected = False


    def draw(self, screen,x ,y):
            if self.collected == False:
                if self.type == "dount":
                    pygame.draw.circle(screen, (250, 0, 0), (self.x, self.y), 10)
                    pygame.draw.circle(screen, (250, 250, 0), (self.x, self.y), 5)
                elif self.type == "ring":
                    pygame.draw.circle(screen, (250, 0, 0), (self.x, self.y), 10)
                    pygame.draw.circle(screen, (0, 250, 0), (self.x, self.y), 5)


            if self.collected == True:
                if self.type == "dount":
                    pygame.draw.circle(screen, (250, 0, 0), (self.x, self.y), 10)
                    pygame.draw.circle(screen, (250, 250, 0), (self.x, self.y), 5)
                elif self.type == "ring":
                    pygame.draw.circle(screen, (250, 0, 0), (self.x, self.y), 10)
                    pygame.draw.circle(screen, (0, 250, 0), (self.x, self.y), 5)
    def collect_item(self, item):
        item.collect()
        self.inventory.appened(item)
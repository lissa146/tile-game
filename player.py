import pygame
Chicken = pygame.image.load('images/chicken.png') #load your spritesheet
Chicken.set_colorkey((255, 0, 255))

#contants
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
W = 5


class Player:
    def __init__ (self):
        
        #player variable
        self.xpos = 400
        self.ypos = 415
        self.vx = 0
        self.vy = 0
        self.frameWidth = 69
        self.frameHeight = 69
        self.RowNum = 2
        self.frameNum = 0
        self.ticker = 0
        self.direction = RIGHT
        
    def draw(self, screen):
        screen.blit(Chicken, (self.xpos, self.ypos), (self.frameWidth*self.frameNum, self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))
    
    def move(self, keys, map):
        #left/right---------------------
        # left movement
        if keys[LEFT] == True:
            self.vx = -3
            self.RowNum = 2
            self.direction = LEFT
        #right movement
        elif keys[RIGHT] == True:
            self.vx = 3
            self.RowNum = 3
            self.direction = RIGHT
        else:
             self.vx = 0
        #up/down-------------------
        if keys[UP] == True:
            self.vy = -3
            self.RowNum = 0
            self.direction = UP
        elif keys[DOWN] == True:
            self.vy = 3
            self.RowNum = 1
            self.direction = DOWN
        else:
            self.vy = 0
            
        if self.vx !=  0 or self.vy != 0: #left animation
            self.ticker+=1
            if self.ticker%10==0: #only change frames every 10 ticks
              self.frameNum+=1
            if self.frameNum>7: 
               self.frameNum = 0
        #collison
        #left colliosn
        if map[int((self.ypos) / 50)][int((self.xpos - 23) /50)] == 2 : #if you collide left
            self.xpos+=3 #bump player right
            
        #right collsion
        if map[int((self.ypos) / 50)][int((self.xpos + 69 + 5) /50)] == 2 : #if you collide right
            self.xpos-=3#bump to the left
            
        # up collsion
        if map[int((self.ypos-23) / 50)][int((self.xpos ) /50)] == 2 :
            self.ypos+=3
            
        #down coillion 
        if map[int((self.ypos+74) / 50)][int((self.xpos ) /50)] == 2 :
            self.ypos-=3
            
        self.xpos+=self.vx #update player xpos
        self.ypos += self.vy

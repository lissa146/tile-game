import pygame
from player import player
from fireball import fireball
pygame.init()
pygame.display.set_caption("top down grid game")# window tile
screen = pygame.display.set_mode((1200,900))#game screen
clock = pygame.time.Clock()#set up clock
gameover = False#variable game loop

#instantiatre player
p1 = player()
ball = fireball()

#constants
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
W = 5
keys = [False, False, False, False, False] # this list hgoldd whether each key has been pressed 

map = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
       [2,1,1,1,1,2,2,1,1,0,0,1,1,1,1,2,2,1,1,2,2,2,2,2],
       [2,1,1,1,1,2,2,1,1,0,0,1,1,1,1,2,2,1,1,2,2,2,2,2],
       [2,0,0,2,2,2,2,0,0,0,0,0,0,2,2,2,2,0,0,2,2,2,2,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2],
       [2,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,2,2,0,2,2,2,2,2],
       [2,3,2,3,3,3,2,2,0,0,0,3,2,3,3,3,2,2,0,2,2,2,2,2],
       [2,3,2,3,3,3,0,0,0,0,0,3,2,3,3,3,0,0,0,2,2,2,2,2],
       [2,3,2,3,3,0,0,0,0,0,0,3,2,3,3,0,0,0,0,2,2,2,2,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,1,1,1,1,2,2,1,1,0,0,1,1,1,1,2,2,1,1,2,2,2,2,2],
       [2,1,1,1,1,2,2,1,1,0,0,1,1,1,1,2,2,1,1,2,2,2,2,2],
       [2,0,0,2,2,2,2,0,0,0,0,0,0,2,2,2,2,0,0,2,2,2,2,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2],
       [2,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,2,2,0,2,2,2,2,2],
       [2,3,2,3,3,3,2,2,0,0,0,3,2,3,3,3,2,2,0,2,2,2,2,2],
       [2,3,2,3,3,3,0,0,0,0,0,3,2,3,3,3,0,0,0,2,2,2,2,2],
       [2,2,2,2,2,2,2,2,2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

brick = pygame.image.load('images/brick.jpg')
dirt = pygame.image.load('images/dirt.jpg')
grass = pygame.image.load('images/grass.jpg')

while not gameover:
    clock.tick(60)#fps
    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#quit game if x is presed in top corner
            gameover = True
        if event.type == pygame.KEYDOWN:#quit game if x is presed in top corner
            if event.key == pygame.K_LEFT:
                keys[LEFT] = True
            
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = True
            elif event.key == pygame.K_UP:
                keys[UP] = True
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = True
            elif event.key == pygame.K_SPACE:
                keys[SPACE] == True
                ball.shoot(p1.xpos, p1.ypos, p1.direction)
        
        elif  event.type == pygame.KEYUP:#quit game if x is presed in top corner
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            elif event.key == pygame.K_UP:
                keys[UP] = False
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = False
            elif event.key == pygame.K_SPACE:
                keys[SPACE] == False
                ball.shoot(p1.xpos, p1.ypos, p1.direction)
        
    #pycals
    #if keys[SPACE] == True:
        #ball.shoot(p1.xpos, p1.ypos, p1.direction)
        
    p1.move(keys, map)
    ball.move(p1.direction, p1.xpos, p1.ypos)
    #render
    screen.fill((0,0,0))#wipe screen
   
    
    #print(p1.vx, p1.vy, p1.xpos, p1.ypos)
    #map
    for i in range(len(map)):
        for j in range(len(map[i])):
                if map[i][j] == 1:
                    screen.blit(dirt, (j * 50, i * 50), (0, 0, 50, 50))
                if map[i][j] == 2:
                    screen.blit(brick, (j * 50, i * 50), (0, 0, 50, 50))
                if map[i][j] == 3:
                    screen.blit(grass, (j * 50, i * 50), (0, 0, 50, 50))
    p1.draw(screen)
    if ball.isAlive == True:
        ball.draw(screen)
                
    pygame.display.flip()
    
    
pygame.quit()

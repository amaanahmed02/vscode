
import sys 

import pygame 
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("first game")



walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')


clock = pygame.time.Clock()

x  = 50 
y = 425 
width = 64                             
height = 64                             
vel = 10 
flag = True 
jump = False
jumpcount = 10 
walkcount = 0 



def redraw ():
    global walkcount 
    win.blit(bg , (0,0))

    if walkcount + 1>=90 : 
        walkcount = 0 
    
    if left : 
        win.blit(walkLeft[walkcount//3],(x,y))
        walkcount+=1 
    elif right : 
        win.blit(walkRight[walkcount//3],(x,y))
        walkcount+=1 
    else : 
        win.blit(char,(x,y))
    pygame.display.update()




while flag :
    clock.tick(90)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    listofmoves = pygame.key.get_pressed()
    if listofmoves[pygame.K_LEFT] and x> vel:
            x -= vel
            left = True 
            right = False
    elif listofmoves[pygame.K_RIGHT] and x < 500 - width - vel :
            x+=vel
            right = True 
            left  = False
    else : 
        left = False
        right = False
        walkcount = 0 
    if not(jump):
        if listofmoves[pygame.K_SPACE]: 
            jump = True 
            left = False
            right = False
            walkcount = 0 
    
    else : 
        if jumpcount>=-10 : 
            neg = 1 
            if jumpcount<0:
                neg = -1
            y -= (jumpcount**2)*neg*0.5
            jumpcount -=1 
        else: 
            jump = False
            jumpcount = 10 
    
    redraw()



    

pygame.quit()
  
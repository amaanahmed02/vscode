import pygame 
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("first game")

x  = 50 
y = 50 
width = 100 
height = 120 
vel = 10 
flag = True 
while flag :
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    listofmoves = pygame.key.get_pressed()
    if listofmoves[pygame.K_LEFT]:
        x -= vel
    if listofmoves[pygame.K_UP]:
        y-=vel 
    if listofmoves[pygame.K_DOWN]:
        y+=vel
    if listofmoves[pygame.K_RIGHT]:
        x+=vel

    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x,y,width , height))
    pygame.display.update()

pygame.quit()

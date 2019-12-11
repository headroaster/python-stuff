import pygame

#Initialise the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((1024, 768))

#Caption and Icons
pygame.display.set_caption("Greedy Assholes")
icon = pygame.image.load('tophatIcon.png')
pygame.display.set_icon(icon)

n = 3

playerIcons = [pygame.image.load('raceCarIcon.png'),\
               pygame.image.load('dionysusIcon.png'),\
               pygame.image.load('tophatIcon.png'),\
               pygame.image.load('skierIcon.png')]

#Players
playerImg = playerIcons[n]
playerX = 650
playerY = 650

def player(x,y):
    screen.blit(playerImg, (x, y))


#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #if key pressed, check for arrows
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            playerX -= 2
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            playerX += 2
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            playerY -= 2
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            playerY += 2
            
    
    screen.fill((0,0,0))
    if playerX <= 50:
        playerX = 50
    elif playerX >= 650:
        playerX = 650
    if playerY <= 50:
        playerY = 50
    elif playerY >= 650:
        playerY = 650
    player(playerX, playerY)
    pygame.display.update()




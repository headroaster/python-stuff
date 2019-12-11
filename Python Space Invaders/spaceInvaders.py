import pygame
import random
import math
from pygame import mixer


#Initialise the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((1024, 768))

#Background
background = pygame.image.load('spaceInvaderBackground.jpg')

#background Sound
mixer.music.load('background.wav')
mixer.music.set_volume(.00)
mixer.music.play(-1)

#Caption and Icons
pygame.display.set_caption("Destroy Galactic Invading Force!")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('spaceship.png')
playerX = 460
playerY = 690
playerX_Change = 0
   
#Bullet
bulletImg = pygame.image.load('bulletIcon.png')
bulletX = 0
bulletY = 650
bulletX_Change = 0
bulletY_Change = 15
bullet_state = "ready"

#Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_Change = []
enemyY_Change = []
num_of_enemies = 24

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(100, 910))
    enemyY.append(random.randint(50, 60))
    enemyX_Change.append(4)
    enemyY_Change.append(50)

score_value = 0

font = pygame.font.Font('monof56.ttf', 32)
over_font = pygame.font.Font('monof56.ttf', 92)
title_font = pygame.font.Font('monof56.ttf', 92)

testX = 10
testY = 10

def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255), (0, 0, 0))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("Game Over, Man", True, (255, 255, 255), (0, 0, 0))
    screen.blit(over_text, (180, 288))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def bullet(x, y):
    global bullet_state
    bullet_state = "fired"
    screen.blit(bulletImg, (x+26, y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX, 2))+(math.pow(enemyY-bulletY, 2))
    if distance < 32:
        return True
    else: 
        return False

def titleScreen():
    gameOver = True
    while gameOver == True:
        screen.fill ((255,0,255))
        title_text = title_font.render("Shoot the Fuckerz!!", True, (255, 255, 255), (0, 0, 0))
        screen.blit(title_text, (180, 188))
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                gameOver = False

    screen.fill ((255,0,255))
    title_text = title_font.render("Shoot the Fuckerz!!", True, (255, 255, 255), (0, 0, 0))
    screen.blit(title_text, (180, 188))

#Game Loop
running = True
while running:

    screen.fill((0,0,0))
    #Background Image
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #if key pressed, check for movement
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            playerX_Change = -4
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            playerX_Change = 4
        if event.key == pygame.K_SPACE:
            if bullet_state == "ready":
                bullet_sound = mixer.Sound('shoot.wav')
                bullet_sound.set_volume(.125)
                bullet_sound.play()
                bulletX = playerX
                bullet(bulletX, bulletY)
        



    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            playerX_Change = 0
 
    #Enemy Movement
    for i in range(num_of_enemies):
        #Game Over
        if enemyY[i] > 650:
            for j in range (num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            
            
        enemyX[i] += enemyX_Change[i]
        if enemyX[i] <= 50:
            enemyX_Change[i] = 2
            enemyY[i] += enemyY_Change[i]
        elif enemyX[i] >= 910:
            enemyX_Change[i] = -2
            enemyY[i] += enemyY_Change[i] 

        #Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('boom.wav')
            explosion_sound.set_volume(25)
            explosion_sound.play()
            bulletY = 650
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(100, 910)
            enemyY[i] = random.randint(50, 60)

        enemy(enemyX[i], enemyY[i], i)

    #Bullet Movement
    if bulletY <= 0:
        bulletY = 650
        bullet_state = "ready"
        
    if bullet_state == "fired":
        bullet(playerX, bulletY)
        bulletY -= bulletY_Change 

    #Keep player in bounds  
    playerX += playerX_Change
    if playerX <= 50:
        playerX = 50
    elif playerX >= 910:
        playerX = 910

    player(playerX, playerY)
    show_score(testX, testY)
    pygame.display.update()

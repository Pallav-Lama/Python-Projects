import pygame
from pygame.constants import *
from pygame import mixer
import random
import math

#initialize the pygame
pygame.init()


# create the screen
screen = pygame.display.set_mode((800, 600))

#background
background = pygame.image.load("sprites/background.png")

#Background sound
mixer.music.load("audio/background.wav")
mixer.music.play(-1)

# title and icon
pygame.display.set_caption("Space Invaders by Pallav Lama")
icon = pygame.image.load("sprites/ufo.png")
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load("sprites/player.png")
playerX = 370
playerY = 480
playerX_change = 0

# enemy

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("sprites/enemy.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 200))
    enemyX_change.append(4)
    enemyY_change.append(40)


#bullet

# ready = bullet is not showing on the screen
# fire = bullet is moving
bulletImg = pygame.image.load("sprites/bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

#score

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

#game_over_text
over_font = pygame.font.Font("freesansbold.ttf", 64)

def showScore(x, y):
    score= font.render(f"score: {score_value}", True, (255, 255, 255))
    screen.blit(score, (x,y))

def game_over_text():
    over_text= over_font.render(f"GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX- bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True

#main game loop
running = True
while running:
    #RGB parameters
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        #if keystrokes is pressed check whether it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                playerX_change = -5

            if event.key == K_RIGHT:
                playerX_change = 5
            
            if event.key == K_SPACE:
                bullet_sound = mixer.Sound("audio/laser.wav")
                bullet_sound.play()
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        
        if event.type == pygame.KEYUP:
            if event.key == K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change 

    for i in range(num_of_enemies):

        #Game Over

        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i]  += enemyX_change[i]

        if enemyX[i] >= 730:
            enemyX_change[i] = -4
            enemyY[i]  += enemyY_change[i]

        elif enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i]  += enemyY_change[i]

         #collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound("audio/explosion.wav")
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 200)
            
        enemy(enemyX[i], enemyY[i], i)


    #bullet_movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        if bulletY == 0:
            bulletY = 480
            bullet_state = "ready"


    if playerX <= 0:
        playerX = 0

    elif playerX >= 736:
        playerX = 736
    
    player(playerX, playerY)
    showScore(textX, textY)
    pygame.display.update()
        

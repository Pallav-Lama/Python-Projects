import pygame
from pygame import key
from pygame.locals import *
import sys
import random
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

#ball movement
def ballMovement():
    global ballX_speed, ballY_speed, score1, score2, score_time
    ball.x += ballX_speed
    ball.y += ballY_speed

    #boundaries
    if ball.top <= 0 or ball.bottom >= win_size[1]:
        collision_sound.play()
        ballY_speed *= -1

    #player1/ computer side border
    if ball.left <= 0: 
        score2 += 1
        score_sound.play()
        score_time = pygame.time.get_ticks()

    #player2 side border
    if ball.right >= win_size[0]:
        score1 += 1
        score_sound.play()
        score_time = pygame.time.get_ticks()

    #player2 and ball
    if ball.colliderect(player2) and ballX_speed > 0:
        collision_sound.play()
        if abs(ball.right-player2.left) < 10:
            ballX_speed *= -1
        
        elif abs(ball.bottom - player2.top) < 10 and ballY_speed > 0:
            ballY_speed *= -1
        
        elif abs(ball.top - player2.bottom) < 19 and ballY_speed < 0:
            ballY_speed *= -1
        
            
    #player1 and ball
    if ball.colliderect(player1) and ballX_speed < 0:
        collision_sound.play()
        if abs(ball.left - player1.right) < 10:
            ballX_speed *= -1
        
        elif abs(ball.bottom - player1.top) < 10 and ballY_speed > 0:
            ballY_speed *= -1
        
        elif abs(ball.top - player1.bottom) < 10 and ballY_speed < 0:
            ballY_speed *= -1

# player2 boundary
def player2Movement():
    if player2.top <= 0:
        player2.top = 0
 
    if player2.bottom >= win_size[1]:
        player2.bottom = win_size[1] 

# player1 boundary
def player1Movement():
    if player1.top <= 0:
        player1.top = 0
 
    if player1.bottom >= win_size[1]:
        player1.bottom = win_size[1] 
    
    if player1.top < ball.y:
        player1.top += player1Y_speed

    if player1.bottom > ball.y:
        player1.bottom -= player1Y_speed
  
def ballRestart():
    global ballX_speed, ballY_speed, score_time
    ball.center = (win_size[0]/2 , win_size[1]/2 )

    current_time = pygame.time.get_ticks()
    if current_time - score_time < 700:
        num1 = game_font.render("3", False, (255, 255, 255))
        WIN.blit(num1, (win_size[0]/ 2 - 10, win_size[1]/2 + 20))
    if 700 < current_time - score_time < 1400:
        num2 = game_font.render("2", False, (255, 255, 255))
        WIN.blit(num2, (win_size[0]/ 2 - 10, win_size[1]/2 + 20))
    if 1400 < current_time - score_time < 2100:
        num3 = game_font.render("1", False, (255, 255, 255))
        WIN.blit(num3, (win_size[0]/ 2 - 10, win_size[1]/2 + 20))

    if current_time - score_time < 2100:
        ballX_speed, ballY_speed = 0, 0
    
    else:
        ballX_speed = 7 * random.choice((1, -1))
        ballY_speed = 7 * random.choice((1, -1))
        score_time = None
   
clock = pygame.time.Clock()

#for displaying windows of width 800 and height 600
win_size = (800, 600)
WIN = pygame.display.set_mode(win_size)

#for writing captions
pygame.display.set_caption("Pong by Pallav Lama")
# player1
player1X = 50
player1Y = win_size[1]/2 - 75
player1Y_speed = 9
player1 = pygame.Rect(player1X , player1Y, 20, 150)

# player2
player2X = 750
player2Y = win_size[1]/2 - 75
player2Y_speed = 0
player2 = pygame.Rect(player2X , player2Y, 20, 150)
player2_change = 8


# ball
ballX = win_size[0]/2 - 15
ballY = win_size[1]/2 - 15
ballX_speed = 7 * random.choice((1, -1))
ballY_speed = 7 * random.choice((1, -1))
ball = pygame.Rect(ballX , ballY, 30, 30)

#text variables for displaying score
score1 = 0
score2 = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

#score_timer
score_time = True

#sound 
collision_sound = pygame.mixer.Sound("audio/pong.ogg")
score_sound = pygame.mixer.Sound("audio/point.wav")

#main game loop
running = True
while running:
    WIN.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    
    ballMovement()
    player1Movement()
    player2Movement()

    #player1movement
    if event.type == KEYDOWN:
        if event.key == K_UP:
            player2.y -= player2_change
        
        if event.key == K_DOWN:
            player2.y += player2_change

    pygame.draw.rect(WIN, (255, 255, 255), player1)
    pygame.draw.rect(WIN, (255, 255, 255), player2)
    pygame.draw.ellipse(WIN, (255, 255, 255), ball)
    pygame.draw.aaline(WIN, (200, 200, 200), (win_size[0]/2, 0), (win_size[0]/2, win_size[1]))

    player1_text = game_font.render(f"Player 1: {score1}", False, (255, 255, 255))
    player2_text = game_font.render(f"Player 2: {score2}", False, (255, 255, 255))
    WIN.blit(player1_text, (220, 50))
    WIN.blit(player2_text, (420, 50))

    if score_time:
        ballRestart()

    pygame.display.update()
    clock.tick(60)

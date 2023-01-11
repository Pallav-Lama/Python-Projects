import random
import pygame
from pygame.locals import *
import sys

#Global variables in game
FPS = 32
SCREENWIDTH = 350
SCREENHEIGHT = 600
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = 400
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = "gallery/Sprites/player.png"
BACKGROUND = "gallery/Sprites/images.png" 
PIPE = "gallery/Sprites/pipe.png"

def welcomeScreen():
    # shows welcome images on the screen
    playerx = int(SCREENWIDTH/ 5) 
    playery = int((SCREENHEIGHT - GAME_SPRITES["player"].get_height())/2)
    basex = 0
    while True:
        for event in pygame.event.get():
            #if user clicks the cross button, close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            
            #if the user presses space or upkey, start the game
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0,-100))
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
                SCREEN.blit(GAME_SPRITES['message'], (0, 0))
                SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def mainGame():
    score = 0
    playerx = int(SCREENWIDTH/ 5) 
    playery = int(SCREENWIDTH/ 5)  
    basex = 0

    #create two pipes for blitting on the screen
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    #list of upper pipes  
    upperPipes = [
        {"x" : SCREENWIDTH + 200, "y": newPipe1[0]['y']},
        {"x" : SCREENWIDTH + 200 + (SCREENWIDTH/2), "y": newPipe2[0]['y']}
    ]  
    #list of lower pipes 
    lowerPipes = [
        {"x" : SCREENWIDTH + 200, "y": newPipe1[1]['y']},
        {"x" : SCREENWIDTH + 200 + SCREENWIDTH/2, "y": newPipe2[1]['y']}
    ]    

    pipeVelX = -4

    playerVelY = -9

    playerMaxVelY = 10

    playerMinVelY = -8

    playerAccY = 1

    playerFlapV = -8 #velocity while flapping
 
    playerFlapped = False #It is true only when the bird is flapping

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapV
                    playerFlapped = True
                    GAME_SOUNDS["wing"].play()

        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes)
        #if player is crashed
        if crashTest:
            return 
        
        # check score
        playerMidPos = playerx + GAME_SPRITES["player"].get_width()/2
        for pipe in upperPipes:
            pipeMidPos = pipe["x"] + GAME_SPRITES["pipe"][0].get_width() /2 
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                score += 1
                GAME_SOUNDS["point"].play()
            
        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False

        playerHeight = GAME_SPRITES["player"].get_height()
        playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

        #move pipes to the left
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe["x"] += pipeVelX
            lowerPipe["x"] += pipeVelX
        #add a new pipe when the first pipe is about to cross to the left of the screen
        if 0 < upperPipes[0] ["x"] < 5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

        # if the pipe is out of the screen, remove it
        if upperPipes[0] ["x"] < -GAME_SPRITES["pipe"] [0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)
        
        #blitting sprites
        SCREEN.blit(GAME_SPRITES["background"], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_SPRITES["pipe"][0], (upperPipe ["x"], upperPipe["y"]))
            SCREEN.blit(GAME_SPRITES["pipe"][1], (lowerPipe["x"], lowerPipe["y"]))

        SCREEN.blit(GAME_SPRITES["base"], (basex, GROUNDY))
        SCREEN.blit(GAME_SPRITES["player"], (playerx, playery))
        SCREEN.blit(GAME_SPRITES["base"], (basex, GROUNDY))
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES["numbers"][digit].get_width()
        Xoffset = (SCREENWIDTH- width)/2

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES["numbers"][digit], (Xoffset, SCREENHEIGHT * 0.12))
            Xoffset += GAME_SPRITES["numbers"] [digit].get_width()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery > GROUNDY - 55  or playery< 0:
        GAME_SOUNDS["hit"].play()
        return True

    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES["pipe"][0].get_height()
        if(playery < pipeHeight + pipe["y"] and abs(playerx- pipe["x"]) < GAME_SPRITES["pipe"][0].get_width()):
            GAME_SOUNDS["hit"].play()
            return True

    for pipe in lowerPipes:
        if (playery + GAME_SPRITES["player"].get_height() > pipe["y"]) and abs(playerx- pipe["x"]) < GAME_SPRITES["pipe"][0].get_width():
            GAME_SOUNDS["hit"].play()
            return True
 

    return False


def getRandomPipe():
    #generate positions of two pipes(upper and lower) for blitting
    pipeHeight = GAME_SPRITES["pipe"][0].get_height()
    offset = SCREENHEIGHT / 4
    y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES["base"].get_height() - 1.2 * offset))
    pipeX = SCREENWIDTH + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {"x" : pipeX, "y" : -y1}, #upper pipe
        {"x" : pipeX, "y" : y2} #lower pipe
    ]
    return pipe


if __name__ == "__main__":
    #this will be the main point from where our game will start
    pygame.init() #inititalize all the modules of pygame
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Flappy Bird by Pallav Lama")
    GAME_SPRITES['numbers'] = ( 
        pygame.image.load("gallery/Sprites/0.png").convert_alpha(),
        pygame.image.load("gallery/Sprites/1.png").convert_alpha(),
        pygame.image.load("gallery/Sprites/2.png").convert_alpha(),
        pygame.image.load("gallery/Sprites/3.png").convert_alpha(),
        pygame.image.load("gallery/Sprites/4.png").convert_alpha(),
        pygame.image.load("gallery/Sprites/5.png").convert_alpha(),
        pygame.image.load("gallery/Sprites/6.png").convert_alpha(),
        pygame.image.load("gallery/Sprites/7.png").convert_alpha(),
        pygame.image.load("gallery/Sprites/8.png").convert_alpha(),
        pygame.image.load("gallery/Sprites/9.png").convert_alpha(),
    )
    GAME_SPRITES['message'] = pygame.image.load("gallery/Sprites/message.png").convert()
    GAME_SPRITES['base'] = pygame.image.load("gallery/Sprites/base.png").convert_alpha()
    GAME_SPRITES['pipe'] = (
    pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
    pygame.image.load(PIPE).convert_alpha()
    )
    #Game Sounds
    GAME_SOUNDS['die'] =pygame.mixer.Sound ("gallery/Audio/die.wav")
    GAME_SOUNDS['hit'] =pygame.mixer.Sound ("gallery/Audio/hit.wav")
    GAME_SOUNDS['point'] =pygame.mixer.Sound ("gallery/Audio/point.wav")
    GAME_SOUNDS['swoosh'] =pygame.mixer.Sound ("gallery/Audio/swoosh.wav")
    GAME_SOUNDS['wing'] =pygame.mixer.Sound ("gallery/Audio/wing.wav")

    GAME_SPRITES["background"] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES["player"] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen() #shows welcome screen to the user until the player's event
        mainGame() #This is the function
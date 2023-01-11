import pygame, sys
from pygame.locals import *
import random
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 4), Vector2(4, 4), Vector2(3, 4)]
        self.direction = Vector2(0, 0)
        self.new_block = False
        

        self.head_up = self.image_load("head_up.png")
        self.head_down = self.image_load("head_down.png")
        self.head_left = self.image_load("head_left.png")
        self.head_right = self.image_load("head_right.png")

        self.tail_up = self.image_load("tail_up.png")
        self.tail_down = self.image_load("tail_down.png")
        self.tail_left = self.image_load("tail_left.png")
        self.tail_right = self.image_load("tail_right.png")
        
        self.body_bl = self.image_load("body_bl.png")
        self.body_br = self.image_load("body_br.png")
        self.body_horizontal = self.image_load("body_horizontal.png")

        self.body_tl = self.image_load("body_tl.png")
        self.body_tr = self.image_load("body_tr.png")
        self.body_vertical = self.image_load("body_vertical.png")
        
    def image_load(self, imagename):
        return pygame.image.load(f"images/{imagename} ")

    def draw_snake(self):
        self.update_head_graphics()
        for index, block in enumerate(self.body):
            x_pos = block.x * cell_size
            y_pos = block.y  * cell_size
            snake_rect = pygame.Rect(x_pos, y_pos , cell_size, cell_size)

            if index == 0:
                screen.blit(self.head,snake_rect)
            
            elif index == len(self.body)-1:
                self.update_tail_graphics() 
                screen.blit(self.tail, snake_rect)
            
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, snake_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, snake_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, snake_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, snake_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, snake_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, snake_rect)
                    

    
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        if head_relation == Vector2(-1, 0):
            self.head = self.head_right
        if head_relation == Vector2(0, 1):
            self.head = self.head_up
        if head_relation == Vector2(0, -1):
            self.head = self.head_down
   
    def update_tail_graphics(self):
        tail_relation = self.body[-1] - self.body[-2]
        if tail_relation == Vector2(-1, 0):
            self.tail = self.tail_left
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_right
        if tail_relation == Vector2(0, -1):
            self.tail = self.tail_up
        if tail_relation == Vector2(0, 1):
            self.tail = self.tail_down

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
        
    def add_block(self):
        self.new_block = True
    
        
    def reset(self):
        self.body = [Vector2(5, 4), Vector2(4, 4), Vector2(3, 4)]
        self.direction = Vector2(0, 0)


class FRUIT:
    def __init__(self):
        self.randomized()
        self.fruit_img = pygame.image.load("images/apple.png")

    def draw_fruit(self):
        x_pos = self.pos.x * cell_size
        y_pos = self.pos.y * cell_size
        fruit_rect = pygame.Rect(x_pos, y_pos , cell_size, cell_size)
        screen.blit(self.fruit_img,fruit_rect)

    def randomized(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class MAINGAME:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.blit_score()
        self.snake.move_snake()
        self.check_collision() 

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        
        
    def check_collision(self):
        #snake with border
        if self.snake.body[0].x < 0 or self.snake.body[0].x > cell_number-1: 
            self.snake.reset()
        if self.snake.body[0].y < 0 or self.snake.body[0].y > cell_number-1: 
            self.snake.reset()
        
        #snake and fruits
        if self.snake.body[0] == self.fruit.pos:
            self.snake.add_block()
            self.fruit.randomized()
            self.blit_score()
        
        for block in self.snake.body[1:]:
            if block == self.fruit.pos :
                self.fruit.randomized()
        
        #snake with body
        for block in self.snake.body[1:]:
            if self.snake.body[0] == block:
                self.snake.reset()

            
    def blit_score(self):
        score = str(len(self.snake.body)-2)
        text_font = pygame.font.Font("freesansbold.ttf", 32)
        x = cell_number * cell_size - 50
        y = cell_number * cell_size - 40
        scorescreen = text_font.render(score, True, (255, 255, 255))
        screen.blit(self.fruit.fruit_img, (x - 50,y-5))
        screen.blit(scorescreen, (x,y))


    def draw_grass(self):
        grass_colour = (167, 209, 61)
        for row in range(cell_number):
            if row % 2 == 0:
                for column in range(cell_number):
                    if column % 2 == 0:
                        grass = pygame.Rect(column * cell_size, row * cell_size, cell_size , cell_size)
                        pygame.draw.rect(screen, grass_colour, grass)
            else:
                for column in range(cell_number):
                    if column % 2 != 0:
                        grass = pygame.Rect(column * cell_size, row * cell_size, cell_size , cell_size)
                        pygame.draw.rect(screen, grass_colour, grass)

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
cell_size = 40
cell_number = 15


main_game = MAINGAME()

screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
pygame.display.set_caption("Snake by Pallav Lama")


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False     
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT and main_game.snake.direction.x != -1:
                main_game.snake.direction = Vector2(1, 0)
            if event.key == K_LEFT and main_game.snake.direction.x != 1:
                main_game.snake.direction = Vector2(-1, 0)
            if event.key == K_UP and main_game.snake.direction.y != 1:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == K_DOWN and main_game.snake.direction.y != -1:
                main_game.snake.direction = Vector2(0, 1)

    screen.fill((175,215,70)) 
    main_game.draw_elements()
    main_game.blit_score()
    pygame.display.update()
    clock.tick(60)

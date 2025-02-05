import pygame
import random

pygame.init()
pygame.display.set_caption('Питон')
FPS = 50
orange = (255, 159, 0)
black = (0, 0, 0)
gray = (90, 90, 90)
width = 800
height = 800
d = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont(None, 25)
score_font = pygame.font.SysFont(None, 35)


def scoree(score):
    value = score_font.render("Ваш счёт: " + str(score), True, orange)
    d.blit(value, [0, 0])


def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(d, orange, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    d.blit(mesg, [width / 6, height / 3])


def game():
    over = False
    close = False
    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0
    list = []
    length = 1
    fx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    fy = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
    while not over:
        while close == True:
            d.fill(gray)
            message("Змейка умерла( Нажмите E чтобы выйти или R для повторной игры", orange)
            scoree(length - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        over = True
                        close = False
                    if event.key == pygame.K_r:
                        game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            close = True
        x1 += x1_change
        y1 += y1_change
        d.fill(gray)
        pygame.draw.rect(d, black, [fx, fy, snake_block, snake_block])
        spisok = []
        spisok.append(x1)
        spisok.append(y1)
        list.append(spisok)
        if len(list) > length:
            del list[0]
        for x in list[:-1]:
            if x == spisok:
                close = True
        snake(snake_block, list)
        scoree(length - 1)
        pygame.display.update()
        if x1 == fx and y1 == fy:
            fx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            fy = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()

game()
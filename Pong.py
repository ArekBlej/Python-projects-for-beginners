import pygame
import sys
from pygame.locals import *

pygame.init()

WIFTH_OF_WINDOW = 800
HEIGHT_OF_WINDOW = 400

WIFTH_OF_PADDLE = 100
HEIGHT_OF_PADDLE = 20

WIFTH_OF_BALL = 20
HEIGHT_OF_BALL = 20

GREEN = (0,255,0)

BLUE = (0,0,255)

RED = (255, 0, 0)

FPS = 30
fpsClock = pygame.time.Clock()

PADDLE_POSITION = (350,360)
PADDLE_AI_POSIOTION = (350, 20)

PADDLE_1 = pygame.Surface([WIFTH_OF_PADDLE, HEIGHT_OF_PADDLE])
PADDLE_1.fill(BLUE)

PADDLE_AI = pygame.Surface([WIFTH_OF_PADDLE, HEIGHT_OF_PADDLE])
PADDLE_AI.fill(RED)

PADDLE_1_RECTANGLE = PADDLE_1.get_rect()
PADDLE_1_RECTANGLE.x = PADDLE_POSITION[0]
PADDLE_1_RECTANGLE.y = PADDLE_POSITION[1]

PADDLE_AI_RECTANGLE = PADDLE_AI.get_rect()
PADDLE_AI_RECTANGLE.x = PADDLE_AI_POSIOTION[0]
PADDLE_AI_RECTANGLE.y = PADDLE_AI_POSIOTION[1]

SPEED_AI = 5

COLOR_OF_WINDOW = (230,255,255)

window_of_game = pygame.display.set_mode((WIFTH_OF_WINDOW, HEIGHT_OF_WINDOW), 0, 32)
pygame.display.set_caption("Gra Pong")

SPEED_BALL_X = 6
SPEED_BALL_Y = 6

BALL = pygame.Surface([WIFTH_OF_BALL, HEIGHT_OF_BALL], pygame.SRCALPHA, 32).convert_alpha()
pygame.draw.ellipse(BALL, GREEN, [0, 0, WIFTH_OF_BALL, HEIGHT_OF_BALL])

BALL_RECTANGLE = BALL.get_rect()
BALL_RECTANGLE.x = WIFTH_OF_WINDOW/2
BALL_RECTANGLE.y = HEIGHT_OF_WINDOW/2

PKT_1 = '0'
PKT_AI = '0'
fontObj = pygame.font.Font('freesansbold.ttf', 64)

def print_points_1():
    tekst_1 = fontObj.render(PKT_1, True, (0, 0, 0))
    tekst_rectangle_1 = tekst_1.get_rect()
    tekst_rectangle_1.center = (HEIGHT_OF_WINDOW/2, HEIGHT_OF_WINDOW*0.75)
    window_of_game.blit(tekst_1, tekst_rectangle_1)

def print_points_ai():
    tekst_ai = fontObj.render(PKT_AI, True, (0, 0, 0))
    tekst_rectangle_ai = tekst_ai.get_rect()
    tekst_rectangle_ai.center = (HEIGHT_OF_WINDOW/2, HEIGHT_OF_WINDOW/4)
    window_of_game.blit(tekst_ai, tekst_rectangle_ai)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            mouseX, mouseY = event.pos
            move = mouseX - (WIFTH_OF_PADDLE/2)
            if move > WIFTH_OF_WINDOW - WIFTH_OF_PADDLE:
                move = WIFTH_OF_WINDOW - WIFTH_OF_PADDLE
            if move < 0:
                move = 0
            PADDLE_1_RECTANGLE.x = move

    BALL_RECTANGLE.move_ip(SPEED_BALL_X, SPEED_BALL_Y)

    if BALL_RECTANGLE.right >= WIFTH_OF_WINDOW:
        SPEED_BALL_X *= -1
    if BALL_RECTANGLE.left <= 0:
        SPEED_BALL_X *= -1
    if BALL_RECTANGLE.top <=0:
        SPEED_BALL_Y *= -1
        BALL_RECTANGLE.x = WIFTH_OF_WINDOW/2
        BALL_RECTANGLE.y = HEIGHT_OF_WINDOW/2
        PKT_1 = str(int(PKT_1) + 1)
    if BALL_RECTANGLE.bottom >= HEIGHT_OF_WINDOW:
        BALL_RECTANGLE.x = WIFTH_OF_WINDOW/2
        BALL_RECTANGLE.y = HEIGHT_OF_WINDOW/2
        PKT_AI = str(int(PKT_AI) + 1)

    if BALL_RECTANGLE.centerx > PADDLE_AI_RECTANGLE.centerx:
        PADDLE_AI_RECTANGLE.x += SPEED_AI
    elif BALL_RECTANGLE.centerx < PADDLE_AI_RECTANGLE.centerx:
        PADDLE_AI_RECTANGLE.x -= SPEED_AI
    if BALL_RECTANGLE.colliderect(PADDLE_AI_RECTANGLE):
        SPEED_BALL_Y *= -1
        BALL_RECTANGLE.top = PADDLE_AI_RECTANGLE.bottom

    if BALL_RECTANGLE.colliderect(PADDLE_1_RECTANGLE):
        SPEED_BALL_Y *= -1
        BALL_RECTANGLE.bottom = PADDLE_1_RECTANGLE.top

    window_of_game.fill(COLOR_OF_WINDOW)
    window_of_game.blit(PADDLE_1, PADDLE_1_RECTANGLE)
    window_of_game.blit(PADDLE_AI, PADDLE_AI_RECTANGLE)
    window_of_game.blit(BALL, BALL_RECTANGLE)
    print_points_1()
    print_points_ai()
    pygame.display.update()
    fpsClock.tick(FPS)
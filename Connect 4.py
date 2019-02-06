import numpy as np
import pygame
import sys
import math

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 175, 0)
WHITE = (255, 255, 255)

ROWS = 6
COLUMNS = 7

def create_board():
    board = np.zeros((ROWS, COLUMNS))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROWS - 1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROWS):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winnig_move(board, piece):
    for c in range(COLUMNS - 3):
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    for c in range(COLUMNS - 3):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    for c in range(COLUMNS - 3):
        for r in range(3, ROWS):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def draw_board(board):
    for c in range(COLUMNS):
        for r in range(ROWS):
            pygame.draw.rect(screen, BLUE, (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK, (c * SQUARE_SIZE + SQUARE_SIZE//2, r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE//2), RADIUS)
    for c in range(COLUMNS):
        for r in range(ROWS):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (c * SQUARE_SIZE + SQUARE_SIZE//2, height - r * SQUARE_SIZE - SQUARE_SIZE + SQUARE_SIZE//2), RADIUS)
            if board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (c * SQUARE_SIZE + SQUARE_SIZE//2, height - r * SQUARE_SIZE - SQUARE_SIZE + SQUARE_SIZE//2), RADIUS)
    pygame.display.update()

def is_full_array(board):
    for c in range(COLUMNS):
        for r in range(ROWS):
            if board[r][c] == 0:
                return False
    return True

game_over = False
board = create_board()

turn = 0

pygame.init()
SQUARE_SIZE = 100
RADIUS = int(SQUARE_SIZE/2 - 5)
width = (ROWS + 1) * SQUARE_SIZE
height = COLUMNS * SQUARE_SIZE

size = (width, height)
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("monospace", 55)
draw_board(board)
pygame.display.update()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE ))
            pos_x = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (pos_x, SQUARE_SIZE//2), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (pos_x, SQUARE_SIZE//2), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
            #print(event.pos)
            if turn == 0:
                pos_x = event.pos[0]
                col = int(math.floor(pos_x/SQUARE_SIZE))
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)
                    if winnig_move(board, 1):
                        game_over = True
                else:
                    turn -= 1
            else:
                pos_x = event.pos[0]
                col = int(math.floor(pos_x / SQUARE_SIZE))
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)
                    if winnig_move(board, 2):
                        game_over = True
                else:
                    turn -= 1
            if is_full_array(board):
                game_over = True
            turn += 1
            turn %= 2
            print_board(board)
            draw_board(board)

            if game_over:
                fontObj = pygame.font.Font('C:\\Windows\\Fonts\\arial.ttf', 54)
                if turn == 1 and is_full_array(board) == False:
                    text_render = fontObj.render("CZERWONE WYGRAŁY!", True, (250, 250, 250))
                    screen.blit(text_render, (60, 350))
                    pygame.display.update()
                    pygame.time.wait(3000)
                elif turn == 0 and is_full_array(board) == False:
                    text_render = fontObj.render("ŻÓŁTE WYGRAŁY!", True, (250, 250, 250))
                    screen.blit(text_render, (110, 350))
                    pygame.display.update()
                    pygame.time.wait(3000)
                elif is_full_array(board):
                    text_render = fontObj.render("REMIS!", True, (250, 250, 250))
                    screen.blit(text_render, (250, 350))
                    pygame.display.update()
                    pygame.time.wait(3000)
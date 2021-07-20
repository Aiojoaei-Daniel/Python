import numpy as np
import pygame
import sys
import math

blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (50, 100, 50)

row_count = 6
column_count = 7


def create_board():
    board = np.zeros((row_count, column_count))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece                  


def is_valid_location(board, col):
    return board[row_count-1][col] == 0         


def get_next_open_row(board, col):
    for r in range(row_count):
        if board[r][col] == 0:
            return r


def reverse_board(board):
    print(np.flip(board, 0))

    
def winning_move(board, piece):
    # verificam ce piese sunt pe orizontala
    for c in range(column_count-3):
        for r in range(row_count):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # verificam ce piese sunt pe verticala
    for c in range(column_count):
        for r in range(row_count-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # diagonala pozitiva
    for c in range(column_count-3):
        for r in range(row_count-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # diagonala negativa
    for c in range(column_count-3):
        for r in range(3, row_count):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def draw_board():
    for c in range(column_count):
        for r in range(row_count):
            pygame.draw.rect(screen, blue, (c * squaresize, r * squaresize + squaresize, squaresize, squaresize))
            pygame.draw.circle(screen, black, (int(c * squaresize + squaresize/2), int(r * squaresize + squaresize + squaresize/2)), radius)
    for c in range(column_count):
        for r in range(row_count):
            if board[r][c] == 1:
                pygame.draw.circle(screen, red, (int(c * squaresize + squaresize/2), height - int(r * squaresize + squaresize/2)), radius)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, green, (int(c * squaresize + squaresize / 2), height - int(r * squaresize + squaresize / 2)), radius)
    pygame.display.update()

game_over = False
turn = 0
board = create_board()
reverse_board(board)

pygame.init()

squaresize = 100
radius = int(squaresize/2 -5)
height = (row_count + 1) * squaresize
width = column_count * squaresize

size = (width, height)

screen = pygame.display.set_mode(size)
draw_board()                     
pygame.display.update()
myfont = pygame.font.SysFont("monospace", 70)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, black, (0, 0, width, squaresize))
            posx = event.pos[0]         # e 0 pentru ca bila sa mearga dupa cursor
            if turn == 0:
                pygame.draw.circle(screen, red, (posx, int(squaresize/2)), radius)
            else:
                pygame.draw.circle(screen, green, (posx, int(squaresize / 2)), radius)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, black, (0, 0, width, squaresize))      
            # ask player 1 input

            if turn == 0:
                posx = event.pos[0]                        
                col = int(math.floor(posx/squaresize))     

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)     
                    drop_piece(board, row, col, 1)          

                    if winning_move(board, 1):
                        label = myfont.render("Player 1 Won!", 1, red)
                        screen.blit(label, (40, 10))       
                        game_over = True
            else:
                posx = event.pos[0]
                col = int(math.floor(posx / squaresize))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        label = myfont.render("Player 2 Won!", 1, green)
                        screen.blit(label, (40, 10))
                        game_over = True

            turn += 1
            turn = turn % 2
            draw_board()
            reverse_board(board)
            if game_over:
                pygame.time.wait(1000)

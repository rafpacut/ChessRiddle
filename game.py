import pygame
import time
from drawBoard import *
from BoardClass import Board
from OpponentClass import Opponent




pygame.init()
board = Board()
boardDrawer = BoardDrawer()
opponent = Opponent()


#draw initial board
boardDrawer.init_board_draw()
pygame.display.update() 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            x = mousePos[0] // 75
            y = mousePos[1] // 75
            if board.moveKnight(x,y):
                opponent.makeMove(board)
                pygame.display.update() 
                time.sleep(0.03)

    boardDrawer.draw_knights(board)

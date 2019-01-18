import pygame
import time
from drawBoard import *
from BoardClass import Board




pygame.init()
board = Board()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            x = mousePos[0] // 75
            y = mousePos[1] // 75
            board.moveKnight(x,y)
            pygame.display.update() 
            time.sleep(0.03)
    board_draw()

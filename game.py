import pygame
import time
from drawBoard import *


pygame.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            x = mousePos[0] // 75
            y = mousePos[1] // 75
            pygame.draw.rect(game_display, teal, (x * 50 * 1.5, y * 50 * 1.5, block_width, block_height))
            pygame.display.update() 
            time.sleep(0.03)
    board_draw()

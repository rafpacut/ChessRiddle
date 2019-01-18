import pygame
import time
from drawBoard import *

isOccupiedMatrix = [ [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0] ]

knightWhiteImg = pygame.image.load("knightW.png")
knightBlackImg = pygame.image.load("knightB.png")

currentColor = "white"

def printOccupationMatrix():
    for col in isOccupiedMatrix:
        print(col)
    print()

def changeColor():
    global currentColor
    if currentColor == "white":
        currentColor = "black"
    else:
        currentColor = "white"
    
    

def moveKnight(x, y):
    isOccupiedMatrix[y][x] = 1
    if currentColor == "white":
        currentKnightImg = knightWhiteImg
    else:
        currentKnightImg = knightBlackImg

    game_display.blit(currentKnightImg, (x*75, y*75))
    changeColor()



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
            moveKnight(x,y)
            pygame.display.update() 
            time.sleep(0.03)
    board_draw()

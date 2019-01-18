import pygame
from drawBoard import *

class Board:
    def changeColor(self):
        if self.currentColor == "white":
            self.currentColor = "black"
        else:
            self.currentColor = "white"

    def moveKnight(self, x, y):
        self.isOccupiedMatrix[y][x] = 1
        if self.currentColor == "white":
            currentKnightImg = self.knightWhiteImg
        else:
            currentKnightImg = self.knightBlackImg

        game_display.blit(currentKnightImg, (x*75, y*75))
        self.changeColor()

    def __init__(self):
        self.isOccupiedMatrix = [ [0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0] ]

        self.knightWhiteImg = pygame.image.load("knightW.png")
        self.knightBlackImg = pygame.image.load("knightB.png")

        self.currentColor = "white"

    def printOccupationMatrix(self):
        for col in isOccupiedMatrix:
            print(col)
        print()

import pygame
from drawBoard import *

class Board:
    def changeColor(self):
        if self.currentColor == "white":
            self.currentColor = "black"
        else:
            self.currentColor = "white"

    def moveKnight(self, x, y):
        if self.isOccupiedMatrix[y][x] == 0:
            if self.currentColor == "white":
                currentKnightImg = self.knightWhiteImg
                self.isOccupiedMatrix[y][x] = "w"
            else:
                currentKnightImg = self.knightBlackImg
                self.isOccupiedMatrix[y][x] = "b"

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

import pygame
from drawBoard import *

class Board:
    def changeColor(self):
        if self.currentColor == "white":
            self.currentColor = "black"
        else:
            self.currentColor = "white"

    def isMoveValid(self, x, y):
        #first move
        if not self.lastLocation: #if is empty
            self.lastLocation = (x,y)
            return True
        
        if self.isValidKnightMove(x, y) and self.isBlockFree(x,y):
            return True
        return False

    def isBlockFree(self, x,y):
        return self.isOccupiedMatrix[y][x] == 0

    def isValidKnightMove(self, x, y):
        lastX = self.lastLocation[0]
        lastY = self.lastLocation[1]

        if lastX + 1 == x and lastY + 2 == y:
            return True
        if lastX + 2 == x and lastY + 1 == y:
            return True
        if lastX + 2 == x and lastY - 1 == y:
            return True
        if lastX + 1 == x and lastY - 2 == y:
            return True
        if lastX - 1 == x and lastY - 2 == y:
            return True
        if lastX - 2 == x and lastY - 1 == y:
            return True
        if lastX - 2 == x and lastY + 1 == y:
            return True
        if lastX - 1 == x and lastY + 2 == y:
            return True

        return False

    def moveKnight(self, x, y):
        if self.isMoveValid(x, y):
            if self.currentColor == "white":
                currentKnightImg = self.knightWhiteImg
                self.isOccupiedMatrix[y][x] = "w"
            else:
                currentKnightImg = self.knightBlackImg
                self.isOccupiedMatrix[y][x] = "b"

            self.lastLocation = (x, y)
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
        self.lastLocation = ()

    def printOccupationMatrix(self):
        for col in isOccupiedMatrix:
            print(col)
        print()


import random

class Opponent:
    def __init__(self):
        self.deltas = [ [1,2],[2,1], [2,-1], [1,-2],
                [-1,-2], [-2,-1], [-2, 1], [-1,2] ]


    def makeMove(self,board):
        randomDeltas = self.deltas
        random.shuffle(randomDeltas)
        lastX = board.lastLocation[0]
        lastY = board.lastLocation[1]
        for delta in randomDeltas:
            if board.moveKnight(lastX+delta[0], lastY+delta[1]):
                break



        

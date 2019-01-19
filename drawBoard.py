import pygame

# defines the width and height of the display
display_width = 600
display_height = 680
game_display = pygame.display.set_mode((display_width, display_height))


class BoardDrawer:

    def __init__(self):
    
        # defines block width and height
        self.block_height = 50 * 1.5
        self.block_width = 50 * 1.5
        
        self.factor = 25 * 1.5
        
        # defines colours
        self.white = (255, 255, 255)
        self.d_white = (250, 250, 250)
        self.black = (0, 0, 0)
        self.teal = (0, 128, 128)
        self.blue_black = (50, 50, 50)

    def draw_knights(self, board):
        x = 0
        y = 0
        for occupiedRow, y in zip(board.isOccupiedMatrix, range(8)):
            for color, x in zip(occupiedRow, range(8)):
                if color == "w":
                    game_display.blit(board.knightWhiteImg, (x*75, y*75))
                elif color == "b":
                    game_display.blit(board.knightBlackImg, (x*75, y*75))


    
    def init_board_draw(self):
        x = 0
        y = 0
        game_display.fill(self.black)
    
        for x_i in range(8):
            j = x_i % 2
            while j < 8:
                pygame.draw.rect(game_display, self.d_white, (x_i * 50 * 1.5, j * 50 *1.5, self.block_width, self.block_height))
                j += 2



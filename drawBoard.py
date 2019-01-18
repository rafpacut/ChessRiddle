import pygame

# defines the width and height of the display
display_width = 600
display_height = 680

# defines block width and height
block_height = 50 * 1.5
block_width = 50 * 1.5

factor = 25 * 1.5

# defines colours
white = (255, 255, 255)
d_white = (250, 250, 250)
black = (0, 0, 0)
teal = (0, 128, 128)
blue_black = (50, 50, 50)

game_display = pygame.display.set_mode((display_width, display_height))

def board_draw():
    x = 0
    y = 0
    game_display.fill(black)

    for x_i in range(8):
        j = x_i % 2
        while j < 8:
            pygame.draw.rect(game_display, d_white, (x_i * 50 * 1.5, j * 50 *1.5, block_width, block_height))
            j += 2


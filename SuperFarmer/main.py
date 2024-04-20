import pygame as py
from pygame.locals import *
import time

import players_data as pd
from players_data import create_users
import util
from util import convert_animal_to_img


class ImageGrid:

    def __init__( self, x, y, image, new_size ):
        self.image  = py.transform.scale(image, (new_size, new_size))
        self.rect   = image.get_rect()  # copy the image dimensions
        self.rect.x = x
        self.rect.y = y                 # move to location

    def draw( self, window ):
        window.blit( self.image, self.rect )    # paint it


class AppClass:
    def __init__(self):

        # main loop

            # drawing
            # WINDOW.fill(WHITE)
            # py.draw.rect(WINDOW, BLACK, (0, 0, WINWIDTH, WINHEIGHT))

            # process all events
        AppClass.running = True

    def play(self):
        py.init()


        WINWIDTH = 800
        WINHEIGHT = 500
        WINSIZE = (WINWIDTH, WINHEIGHT)

        CELLWIDTH = 50
        CELLHEIGHT = 50
        CELLSIZE = (CELLWIDTH, CELLHEIGHT)

        CELLMARGINX = 5  # number of pixels to the left and right of each cell
        CELLMARGINY = 5  # number of pixels to the top and bottom of each cell

        SCREENPADX = 80  # number of pixels between the GRID and the left and right of the window
        SCREENPADY = 80  # number of pixels between the GRID and the top and bottom of the window

        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)

        DONE = False  # is our program finished running?

        # information about the two buttons (red and green)
        SECONDPLAYERCUBEBUTTON = (450, 400, 200, 50)
        FIRSTPLAYERCUBEBUTTON = (150, 400, 200, 50)
        FIRSTCOLOR = GREEN
        SECONDCOLOR = RED

        # create the WINDOW and CLOCK
        WINDOW = py.display.set_mode(WINSIZE)
        py.display.set_caption('Super Farmer')
        CLOCK = py.time.Clock()

        for y in range(5):
            for x in range(12):
                if x == 5 or x == 6:
                    py.draw.rect(WINDOW, BLACK,
                                 (SCREENPADX + x*(CELLWIDTH+CELLMARGINX), SCREENPADY + y*(CELLHEIGHT+CELLMARGINY), CELLWIDTH, CELLHEIGHT))
                else:
                    py.draw.rect(WINDOW, WHITE,
                                 (SCREENPADX + x * (CELLWIDTH + CELLMARGINX), SCREENPADY + y * (CELLHEIGHT + CELLMARGINY), CELLWIDTH, CELLHEIGHT))
        py.display.flip()
        # setting up the GRID
        # cells can be accessed by GRID[row][col] ie. GRID[3][4] is the 3rd row and 4th column
        # each cell contains [x, y, color]
        # where x is the x position on the screen
        #       y is the y position on the screen
        #       color is the current color of the cell
        GRID = []

        for y in range(5):
            row = []
            for x in range(12):
                if x == 5 or x == 6:
                    row.append(
                        [x * (CELLWIDTH + CELLMARGINX) + SCREENPADX, y * (CELLHEIGHT + CELLMARGINY) + SCREENPADY,
                         BLACK])
                else:
                    row.append(
                        [x * (CELLWIDTH + CELLMARGINX) + SCREENPADX, y * (CELLHEIGHT + CELLMARGINY) + SCREENPADY, WHITE])
            GRID.append(row)

        while AppClass.running:
            for event in py.event.get():
                if event.type == QUIT:
                    AppClass.running = False

                if event.type == MOUSEBUTTONDOWN:
                    # get the position of the mouse
                    mpos_x, mpos_y = event.pos

                    # check if FIRSTPLAYERCUBEBUTTON was clicked
                    button_x_min, button_y_min, button_width, button_height = FIRSTPLAYERCUBEBUTTON
                    button_x_max, button_y_max = button_x_min + button_width, button_y_min + button_height
                    if (button_x_min <= mpos_x <= button_x_max and button_y_min <= mpos_y <= button_y_max
                            and FIRSTCOLOR == GREEN):
                        # print("TUU")
                        FIRSTCOLOR = RED
                        SECONDCOLOR = GREEN
                        players[0].add_animals(*util.rand_animals())
                        print("AAA")
                        i = 0
                        for key in players[0].animals:
                            no_anim = players[0].animals[key]
                            y = SCREENPADY + i * (CELLHEIGHT + CELLMARGINY)
                            j = 0
                            while j < 5:
                                x = SCREENPADX + j * (CELLWIDTH + CELLMARGINX)
                                if j < no_anim:
                                    image = py.image.load("Images/" + convert_animal_to_img(key)).convert_alpha()
                                    ImageGrid(x, y, image, CELLWIDTH).draw(WINDOW)
                                else:
                                    py.draw.rect(WINDOW, WHITE, (x, y, CELLWIDTH, CELLHEIGHT))
                                j += 1
                            i += 1
                        #py.display.flip()

                    # check if REDBUTTON was clicked
                    button_x_min, button_y_min, button_width, button_height = SECONDPLAYERCUBEBUTTON
                    button_x_max, button_y_max = button_x_min + button_width, button_y_min + button_height
                    if (button_x_min <= mpos_x <= button_x_max and button_y_min <= mpos_y <= button_y_max
                            and SECONDCOLOR == GREEN):
                        SECONDCOLOR = RED
                        FIRSTCOLOR = GREEN
                        players[1].add_animals(*util.rand_animals())
                        print("AAA")
                        i = 0
                        for key in players[1].animals:
                            no_anim = players[1].animals[key]
                            y = SCREENPADY + i * (CELLHEIGHT + CELLMARGINY)
                            j = 0
                            while j < 5:
                                x = SCREENPADX + (j + 7) * (CELLWIDTH + CELLMARGINX)
                                if j < no_anim:
                                    image = py.image.load('Images/' + convert_animal_to_img(key)).convert_alpha()
                                    ImageGrid(x, y, image, CELLWIDTH).draw(WINDOW)
                                else:
                                    py.draw.rect(WINDOW, WHITE, (x, y, CELLWIDTH, CELLHEIGHT))
                                j += 1
                            i += 1
                        #py.display.flip()


                            # for i in range(5):
                            #     x = SCREENPADX + i * (CELLWIDTH + CELLMARGINX)
                            #     y = SCREENPADY
                            #     image = py.image.load('rabbit.jpg').convert_alpha()
                            #     ImageGrid(x, y, image, CELLWIDTH).draw(WINDOW)

                            # CURRENTCOLOR = GREEN

                        # calculations for clicking cells

                    mpos_x -= SCREENPADX  # mouse position relative to the upper left cell
                    mpos_y -= SCREENPADY  # ^ same

                    col = mpos_x // (CELLWIDTH + CELLMARGINX)  # which cell is the mouse clicking
                    row = mpos_y // (CELLHEIGHT + CELLMARGINY)  # ^ same

                        # make sure the user clicked on the GRID area
                        # if row >= 0 and col >= 0:
                        #     try:
                        #         # calculate the boundaries of the cell
                        #         cell_x_min, cell_y_min = col * (CELLHEIGHT + CELLMARGINY), row * (
                        #                     CELLWIDTH + CELLMARGINX)
                        #         cell_x_max = cell_x_min + CELLWIDTH
                        #         cell_y_max = cell_y_min + CELLHEIGHT
                        #         # now we will see if the user clicked the cell or the margin
                        #         if cell_x_min <= mpos_x <= cell_x_max and cell_y_min <= mpos_y <= cell_y_max:
                        #             GRID[row][col][2] = CURRENTCOLOR if event.button == 1 else WHITE
                        #         else:
                        #             # the user has clicked the margin, so we do nothing
                        #             pass
                        #     except IndexError:  # clicked outside of the GRID
                        #         pass  # we will do nothing

                # logic goes here

            py.draw.rect(WINDOW, FIRSTCOLOR, FIRSTPLAYERCUBEBUTTON)
            py.draw.rect(WINDOW, SECONDCOLOR, SECONDPLAYERCUBEBUTTON)

                # for row in GRID:
                #     for x, y, color in row:
                #         py.draw.rect(WINDOW, color, (x, y, CELLWIDTH, CELLHEIGHT))

            py.display.flip()

            CLOCK.tick(60)

        py.quit()
# end class


if __name__ == '__main__':
    players = create_users(2)
    print(players)

    AppClass().play()

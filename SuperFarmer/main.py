import math

import pygame as py
from pygame.locals import *
import time

import board
from board import animalBoardCoordinates

from players_data import create_users
import util
from util import convert_animal_to_img
from util import Image

from copy import deepcopy

data = []


class AppClass:
    def __init__(self):

        # main loop

            # drawing
            # WINDOW.fill(WHITE)
            # py.draw.rect(WINDOW, BLACK, (0, 0, WINWIDTH, WINHEIGHT))

            # process all events
        AppClass.running = True

    def play(self):
        player_turn = 0
        py.init()

        WINWIDTH = 1500
        WINHEIGHT = 800
        WINSIZE = (WINWIDTH, WINHEIGHT)

        SCREENPADX = 80  # number of pixels between the GRID and the left and right of the window
        SCREENPADY = 80  # number of pixels between the GRID and the top and bottom of the window

        # Kolory
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLU = (52, 229, 235)
        BLU2 = (93, 190, 194)
        BLU3 = (38, 125, 128)

        DONE = False  # is our program finished running?

        # information about the two buttons (red and green)
        SECONDPLAYERCUBEBUTTON = (450, 400, 200, 50)
        CUBEBUTTON = (650, 600, 200, 50)
        CUBERESULT = [(650, 500), (750, 500)]
        CUBE_RESULT_MARKING_RECT = (650, 500, 200, 100)
        FIRSTCOLOR = GREEN
        SECONDCOLOR = RED

        CLOCK = py.time.Clock()

        font = py.font.Font('Fonts/BRLNSDB.ttf', 28)

        textButton = "Roll the dices"
        textSurfaceButton = font.render(textButton, True, WHITE)

        message = ""


        # create the WINDOW and CLOCK
        WINDOW = py.display.set_mode(WINSIZE)
        py.display.set_caption('Super Farmer')
        print("TUTAJ")
        CLOCK = py.time.Clock()
        CELL_SIZE = board.create_board(WINDOW)


        print(animalBoardCoordinates[0][0])
        py.draw.rect(WINDOW, RED, CUBEBUTTON)

        bluefarmer = py.image.load('Images/bluefarmer.png').convert_alpha()
        bluefarmer_width, bluefarmer_height = bluefarmer.get_size()
        redfarmer = py.image.load('Images/redfarmer.png').convert_alpha()
        redfarmer_width, redfarmer_height = redfarmer.get_size()

        # Animacja farmera
        for i in range(10):
            Image(WINWIDTH - bluefarmer_width / 4 - i * 5, WINHEIGHT - bluefarmer_height / 3 - i * 5, bluefarmer,
                  bluefarmer_width / 3 + i * 10, bluefarmer_height / 3 + i * 10).draw(WINDOW)
            py.display.update()
            CLOCK.tick(40)
        for i in range(10, -1, -1):
            py.draw.rect(WINDOW, BLACK, (WINWIDTH - bluefarmer_width / 4-i*5, WINHEIGHT - bluefarmer_height / 3-i*5,
                      bluefarmer_width / 3+i*10, bluefarmer_height / 3+i*10))
            Image(WINWIDTH - bluefarmer_width / 4 - i * 5, WINHEIGHT - bluefarmer_height / 3 - i * 5, bluefarmer,
                  bluefarmer_width / 3 + i * 10, bluefarmer_height / 3 + i * 10).draw(WINDOW)
            py.display.update()
            CLOCK.tick(40)

        #ImageGrid(-redfarmer_width / 10, WINHEIGHT - redfarmer_height / 3, redfarmer, redfarmer_width / 3,
        #          redfarmer_height / 3).draw(WINDOW)

        WINDOW.blit(textSurfaceButton, (670, 610))
        #print(util.Animal(0).value)
        # for i in range(5):
        #     board.drawcircles(WINDOW, BLU, BLU2, BLU3,
        #                       animalBoardCoordinates[0][i][len(animalBoardCoordinates[0][i]) - 1][2],
        #                       animalBoardCoordinates[0][i][len(animalBoardCoordinates[0][i]) - 1][3],
        #                       animalBoardCoordinates[0][i][len(animalBoardCoordinates[0][i]) - 1][1],
        #                       util.convert_animal_to_img(i),
        #                       animalBoardCoordinates[0][i][len(animalBoardCoordinates[0][i]) - 1][4],
        #                       CELL_SIZE)

        #board.drawcircles(WINDOW, BLU, BLU2, BLU3, animalBoardCoordinates[0][0][n-1][2],
        #                  animalBoardCoordinates[0][0][n-1][3], animalBoardCoordinates[0][0][n-1][1],
        #                  util.convert_animal_to_img(0), animalBoardCoordinates[0][0][n-1][4], CELL_SIZE)


        # for i in range(1, 5):
        #     board.draw_animal()(WINDOW, BLU, animalBoardCoordinates[0][0][i][0],
        #                       animalBoardCoordinates[0][0][i][1], CELL_SIZE / 2, 10, util.convert_animal_to_img(0))

        while AppClass.running:
            for event in py.event.get():
                if event.type == QUIT:
                    AppClass.running = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        AppClass.running = False

                if event.type == MOUSEBUTTONDOWN:
                    # get the position of the mouse
                    mpos_x, mpos_y = event.pos
                    # if tura % 2 == 1 and tura > 1:
                    #     WINDOW.fill(BLACK)
                    #     #CELL_SIZE = board.create_board(WINDOW)
                    #     py.draw.rect(WINDOW, RED, CUBEBUTTON)
                    #     WINDOW.blit(textSurfaceButton, (670, 610))
                    #
                    #     image = py.image.load('Images/smalldog.png').convert_alpha()
                    #     Image(0.7 * WINWIDTH, 0.05 * WINHEIGHT, image, 100, 100).draw(WINDOW)
                    #     image = py.image.load('Images/bigdog.png').convert_alpha()
                    #     Image(0.85 * WINWIDTH, 0.05 * WINHEIGHT, image, 100, 100).draw(WINDOW)
                    a = -1
                    b = -1
                    for i in range(5):
                        if (animalBoardCoordinates[player_turn][i][0][1] + CELL_SIZE/2 >= mpos_y >=
                                animalBoardCoordinates[player_turn][i][0][1] - CELL_SIZE/2):
                            #print("Kliknąłem w zwierz:", i)
                            a = i
                    for i in range(len(animalBoardCoordinates[0][a]) - 1):
                        if math.sqrt(math.pow(mpos_x-animalBoardCoordinates[player_turn][a][i][0], 2) + math.pow(mpos_y-animalBoardCoordinates[player_turn][a][i][1],2)) <= CELL_SIZE/2:
                            b = i
                    print("Kliknąłm w: ", a, " ", b)

                    button_x_min, button_y_min, button_width, button_height = CUBEBUTTON
                    button_x_max, button_y_max = button_x_min + button_width, button_y_min + button_height

                    if button_x_min <= mpos_x <= button_x_max and button_y_min <= mpos_y <= button_y_max:
                        py.draw.rect(WINDOW, BLACK, (0.3*WINWIDTH, 0.1*WINHEIGHT, 600, 50))
                        py.display.flip()
                        message = ""
                        # print("TUU")
                        FIRSTCOLOR = RED
                        SECONDCOLOR = GREEN
                        drawn_animals = util.rand_animals()

                        animals_before = deepcopy(players[player_turn].animals)

                        res1, res2 = players[player_turn].add_animals(drawn_animals[0], drawn_animals[1])

                        py.draw.rect(WINDOW, BLACK, CUBE_RESULT_MARKING_RECT)
                        Image(CUBERESULT[0][0], CUBERESULT[0][1], convert_animal_to_img(drawn_animals[0]), 100,
                              100).draw(WINDOW)
                        Image(CUBERESULT[1][0], CUBERESULT[1][1], convert_animal_to_img(drawn_animals[1]), 100,
                              100).draw(WINDOW)

                        print(res1, res2)
                        if res1 == util.Predators.FOX:
                            message = f"Oh no, there was a fox attack on player {player_turn+1}!"
                        elif res1 == util.Defence.SMALLDOG:
                            message = f"The small dog saved player {player_turn+1} from fox attack!"
                        if res2 == util.Predators.WOLF:
                            message = f"Oh no, there was a wolf attack on player {player_turn+1}!"
                        elif res2 == util.Defence.BIGDOG:
                            message = f"The big dog saved player {player_turn+1} from wolf attack!"
                        print("AAA")

                        alert = font.render(message, True, WHITE)
                        WINDOW.blit(alert, (0.3*WINWIDTH, 0.1*WINHEIGHT))

                        board.update_board(WINDOW, players[player_turn], animals_before, players[player_turn].animals, CELL_SIZE)


                        i = 0
                        # for key in players[0].animals:
                        #     no_anim = players[0].animals[key]
                        #     y = SCREENPADY + i * (CELLHEIGHT + CELLMARGINY)
                        #     j = 0
                        #     while j < 5:
                        #         x = SCREENPADX + j * (CELLWIDTH + CELLMARGINX)
                        #         if j < no_anim:
                        #             image = py.image.load("Images/" + convert_animal_to_img(key)).convert_alpha()
                        #             ImageGrid(x, y, image, CELLWIDTH).draw(WINDOW)
                        #         else:
                        #             py.draw.rect(WINDOW, WHITE, (x, y, CELLWIDTH, CELLHEIGHT))
                        #         j += 1
                        #     i += 1
                        #py.display.flip()
                        player_turn += 1
                        player_turn %= 2

                    # check if REDBUTTON was clicked
                    button_x_min, button_y_min, button_width, button_height = SECONDPLAYERCUBEBUTTON
                    button_x_max, button_y_max = button_x_min + button_width, button_y_min + button_height
                    if (button_x_min <= mpos_x <= button_x_max and button_y_min <= mpos_y <= button_y_max
                            and SECONDCOLOR == GREEN):
                        SECONDCOLOR = RED
                        FIRSTCOLOR = GREEN
                        res1, res2 = players[1].add_animals(*util.rand_animals())
                        if res1 == util.Predators.FOX:
                            print("Oh no, there was a fox attack on player 2!")
                        elif res1 == util.Defence.SMALLDOG:
                            print("The small dog saved player 2 from fox attack!")
                        if res2 == util.Predators.WOLF:
                            print("Oh no, there was a wolf attack on player 2!")
                        elif res2 == util.Defence.BIGDOG:
                            print("The big dog saved player 2 from wolf attack!")
                        i = 0
                        # for key in players[1].animals:
                        #     no_anim = players[1].animals[key]
                        #     y = SCREENPADY + i * (CELLHEIGHT + CELLMARGINY)
                        #     j = 0
                        #     while j < 5:
                        #         x = SCREENPADX + (j + 7) * (CELLWIDTH + CELLMARGINX)
                        #         if j < no_anim:
                        #             image = py.image.load('Images/' + convert_animal_to_img(key)).convert_alpha()
                        #             ImageGrid(x, y, image, CELLWIDTH).draw(WINDOW)
                        #         else:
                        #             py.draw.rect(WINDOW, WHITE, (x, y, CELLWIDTH, CELLHEIGHT))
                        #         j += 1
                        #     i += 1
                        #py.display.flip()


                            # for i in range(5):
                            #     x = SCREENPADX + i * (CELLWIDTH + CELLMARGINX)
                            #     y = SCREENPADY
                            #     image = py.image.load('rabbit.jpg').convert_alpha()
                            #     ImageGrid(x, y, image, CELLWIDTH).draw(WINDOW)

                            # CURRENTCOLOR = GREEN

                        # calculations for clicking cells

                    if 0.7 * WINWIDTH <= mpos_x <= 0.7 * WINWIDTH + 50 and 0.1 * WINHEIGHT <= mpos_y <= 0.1 * WINHEIGHT + 50:
                        # Small dog icon clicked
                        print("Small dog")
                        print(players[player_turn].animals)
                        print(players[player_turn].buy_small_dog())
                        print(players[player_turn].dogs)
                    if 0.85 * WINWIDTH <= mpos_x <= 0.85 * WINWIDTH + 50 and 0.1 * WINHEIGHT <= mpos_y <= 0.1 * WINHEIGHT + 50:
                        # Big dog icon clicked
                        print("Big dog")
                        print(players[player_turn].animals)
                        print(players[player_turn].buy_big_dog())
                        print(players[player_turn].dogs)

                    mpos_x -= SCREENPADX  # mouse position relative to the upper left cell
                    mpos_y -= SCREENPADY  # ^ same

                    # col = mpos_x // (CELLWIDTH + CELLMARGINX)  # which cell is the mouse clicking
                    # row = mpos_y // (CELLHEIGHT + CELLMARGINY)  # ^ same

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

            #py.draw.rect(WINDOW, FIRSTCOLOR, CUBEBUTTON)
            #py.draw.rect(WINDOW, SECONDCOLOR, SECONDPLAYERCUBEBUTTON)

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
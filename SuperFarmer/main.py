import math

import pygame as py
from pygame.locals import *
from pygame import time

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

        def is_mouse_over(rect):
            mouse_x, mouse_y = py.mouse.get_pos()
            return rect[0] < mouse_x < rect[0] + rect[2] and rect[1] < mouse_y < rect[1] + rect[3]
        # end def

        def get_clicked_circle(mouse_x, mouse_y):
            a = -1
            b = -1
            for i in range(5):
                if (animalBoardCoordinates[player_turn][i][0][1] + CELL_SIZE / 2 >= mpos_y >=
                        animalBoardCoordinates[player_turn][i][0][1] - CELL_SIZE / 2):
                    a = i
            for i in range(len(animalBoardCoordinates[0][a]) - 1):
                if math.sqrt(math.pow(mpos_x - animalBoardCoordinates[player_turn][a][i][0], 2) + math.pow(
                        mpos_y - animalBoardCoordinates[player_turn][a][i][1], 2)) <= CELL_SIZE / 2:
                    b = i
            print("Kliknąłm w: ", a, " ", b)
            return a, b
        # end def

        WINWIDTH = 1500
        WINHEIGHT = 800
        WINSIZE = (WINWIDTH, WINHEIGHT)

        SCREENPADX = 80  # number of pixels between the GRID and the left and right of the window
        SCREENPADY = 80  # number of pixels between the GRID and the top and bottom of the window

        # Kolory
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        DARKRED = (145, 0, 0)
        DARKGREY = (59, 59, 59)
        GREEN = (0, 255, 0)
        BLU = (52, 229, 235)
        BLU2 = (93, 190, 194)
        BLU3 = (38, 125, 128)

        DONE = False  # is our program finished running?

        # information about the two buttons (red and green)
        SECONDPLAYERCUBEBUTTON = (450, 400, 200, 50)
        CUBEBUTTON = (650, 600, 200, 50)
        CUBERESULT = [(650, 500), (750, 500)]
        CUBE_RESULT_MARKING_RECT = (650, 490, 200, 100)

        INFO_RECT = (0.2*WINWIDTH, 0.05*WINHEIGHT, 650, 50)

        # Dogs buttons
        SMALL_DOG_BUTTON = (0.7 * WINWIDTH, 0.05 * WINHEIGHT, 80, 80)
        BIG_DOG_BUTTON = (0.85 * WINWIDTH, 0.05 * WINHEIGHT, 80, 80)
        RECT_BEHIND_SMALL_DOG_IMAGE = (0.7 * WINWIDTH - 5, 0.05 * WINHEIGHT - 10, 95, 100)
        RECT_BEHIND_BIG_DOG_IMAGE = (0.85 * WINWIDTH - 5, 0.05 * WINHEIGHT - 10, 95, 100)

        CLOCK = py.time.Clock()

        font = py.font.Font('Fonts/BRLNSDB.ttf', 28)

        cube_button_text_surface = font.render("Roll the dices", True, WHITE)

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

        WINDOW.blit(cube_button_text_surface, (670, 610))
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

        # Dogs bank
        small_dog = py.image.load('Images/smalldog.png')
        Image(SMALL_DOG_BUTTON[0], SMALL_DOG_BUTTON[1], small_dog, SMALL_DOG_BUTTON[2], SMALL_DOG_BUTTON[3]).draw(WINDOW)
        big_dog = py.image.load('Images/bigdog.png')
        Image(BIG_DOG_BUTTON[0], BIG_DOG_BUTTON[1], big_dog, BIG_DOG_BUTTON[2], BIG_DOG_BUTTON[3]).draw(WINDOW)

        dog_cost = font.render("Cost:", True, WHITE)
        WINDOW.blit(dog_cost, (SMALL_DOG_BUTTON[0]-70, SMALL_DOG_BUTTON[1]))
        WINDOW.blit(dog_cost, (BIG_DOG_BUTTON[0]+BIG_DOG_BUTTON[2]+20, BIG_DOG_BUTTON[1]))
        board.draw_animal(WINDOW, board.BLUE, SMALL_DOG_BUTTON[0] - 40, SMALL_DOG_BUTTON[1] + 50, 50, 10,
                          util.Animal.SHEEP, 255)
        board.draw_animal(WINDOW, board.BLUE, BIG_DOG_BUTTON[0] + BIG_DOG_BUTTON[2] + 50, BIG_DOG_BUTTON[1] + 50, 50,
                          10, util.Animal.COW, 255)

        dog_info_1 = font.render("Buy them", True, WHITE)
        dog_info_2 = font.render("       by", True, WHITE)
        dog_info_3 = font.render("  clicking", True, WHITE)
        WINDOW.blit(dog_info_1, (SMALL_DOG_BUTTON[0] + SMALL_DOG_BUTTON[2] + 10, SMALL_DOG_BUTTON[1]))
        WINDOW.blit(dog_info_2, (SMALL_DOG_BUTTON[0] + SMALL_DOG_BUTTON[2] + 10, SMALL_DOG_BUTTON[1] + 28))
        WINDOW.blit(dog_info_3, (SMALL_DOG_BUTTON[0] + SMALL_DOG_BUTTON[2] + 10, SMALL_DOG_BUTTON[1] + 56))

        # For exchange
        start = -1
        for_exchange = [None, None, None]

        while AppClass.running:

            if is_mouse_over(CUBEBUTTON):
                py.draw.rect(WINDOW, DARKRED, CUBEBUTTON)
                WINDOW.blit(cube_button_text_surface, (670, 610))
            else:
                py.draw.rect(WINDOW, RED, CUBEBUTTON)
                WINDOW.blit(cube_button_text_surface, (670, 610))

            if is_mouse_over(SMALL_DOG_BUTTON):
                py.draw.rect(WINDOW, DARKGREY, RECT_BEHIND_SMALL_DOG_IMAGE)
                Image(SMALL_DOG_BUTTON[0], SMALL_DOG_BUTTON[1], small_dog, SMALL_DOG_BUTTON[2],
                      SMALL_DOG_BUTTON[3]).draw(WINDOW)
            else:
                py.draw.rect(WINDOW, BLACK, RECT_BEHIND_SMALL_DOG_IMAGE)
                Image(SMALL_DOG_BUTTON[0], SMALL_DOG_BUTTON[1], small_dog, SMALL_DOG_BUTTON[2],
                      SMALL_DOG_BUTTON[3]).draw(WINDOW)

            if is_mouse_over(BIG_DOG_BUTTON):
                py.draw.rect(WINDOW, DARKGREY, RECT_BEHIND_BIG_DOG_IMAGE)
                Image(BIG_DOG_BUTTON[0], BIG_DOG_BUTTON[1], big_dog,
                      BIG_DOG_BUTTON[2], BIG_DOG_BUTTON[3]).draw(WINDOW)
            else:
                py.draw.rect(WINDOW, BLACK, RECT_BEHIND_BIG_DOG_IMAGE)
                Image(BIG_DOG_BUTTON[0], BIG_DOG_BUTTON[1], big_dog, BIG_DOG_BUTTON[2],
                      BIG_DOG_BUTTON[3]).draw(WINDOW)

            for event in py.event.get():
                if event.type == QUIT:
                    AppClass.running = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        AppClass.running = False

                if event.type == MOUSEBUTTONDOWN:
                    # Get the position of the mouse
                    mpos_x, mpos_y = event.pos

                    # Before clicking cube button we can exchange animals
                    # First value represents an animal to exchange, second is equivalent to the number of these animals
                    # and third represents an animal which player wants to get after exchange.

                    a, b = get_clicked_circle(mpos_x, mpos_y)
                    if a != -1 and b != -1:
                        if b >= players[player_turn].animals[util.Animal(a)] and for_exchange[0] is None:
                            py.draw.rect(WINDOW, BLACK, INFO_RECT)
                            alert = font.render("You don't have animals there!", True, WHITE)
                            WINDOW.blit(alert, (INFO_RECT[0], INFO_RECT[1]))
                            py.display.flip()
                            time.delay(1000)
                            py.draw.rect(WINDOW, BLACK, INFO_RECT)
                            break
                        if (for_exchange[0] is None and for_exchange[1] is None
                                and b < players[player_turn].animals[util.Animal(a)]):
                            print("TU: ", for_exchange)
                            # First animal clicked
                            for_exchange[0] = util.Animal(a)
                            start = b
                        elif for_exchange[1] is None and start != -1 and b < players[player_turn].animals[util.Animal(a)]:
                            print("TUU: ", for_exchange)
                            if util.Animal(a) == for_exchange[0]:
                                # Same animal clicked
                                for_exchange[1] = b - start + 1
                            else:
                                # Another animal clicked
                                for_exchange[0] = util.Animal(a)
                                start = b
                        else:
                            print("TUUU: ", for_exchange)
                            if util.Animal(a) == for_exchange[0]:
                                py.draw.rect(WINDOW, BLACK, INFO_RECT)
                                alert = font.render("You can't exchange animal for the same type", True, WHITE)
                                WINDOW.blit(alert, (INFO_RECT[0], INFO_RECT[1]))
                                py.display.flip()
                                time.delay(1000)
                                py.draw.rect(WINDOW, BLACK, INFO_RECT)
                            else:
                                for_exchange[2] = util.Animal(a)
                                print("Just before exchange: ", for_exchange)
                                animals_before = deepcopy(players[player_turn].animals)
                                exchange_result = players[player_turn].exchange_animals(for_exchange[0],
                                                                                    for_exchange[1], for_exchange[2])

                                if not exchange_result:
                                    py.draw.rect(WINDOW, BLACK, INFO_RECT)
                                    alert = font.render("Too few animals to exchange", True, WHITE)
                                    WINDOW.blit(alert, (INFO_RECT[0], INFO_RECT[1]))
                                    py.display.flip()
                                    time.delay(1000)
                                    py.draw.rect(WINDOW, BLACK, INFO_RECT)
                                else:
                                    py.draw.rect(WINDOW, BLACK, INFO_RECT)
                                    alert = font.render("You successfully exchanged your animals!", True, WHITE)
                                    WINDOW.blit(alert, (INFO_RECT[0], INFO_RECT[1]))
                                    py.display.flip()
                                    time.delay(1000)
                                    py.draw.rect(WINDOW, BLACK, INFO_RECT)
                                    board.update_board(WINDOW, players[player_turn], animals_before,
                                                       players[player_turn].animals, CELL_SIZE)
                                start = -1
                                for_exchange = [None, None, None]


                    if is_mouse_over(CUBEBUTTON):
                        py.draw.rect(WINDOW, BLACK, INFO_RECT)
                        py.display.flip()
                        message = ""
                        # print("TUU")
                        FIRSTCOLOR = RED
                        SECONDCOLOR = GREEN
                        drawn_animals = util.rand_animals()

                        animals_before = deepcopy(players[player_turn].animals)

                        res1, res2 = players[player_turn].add_animals(drawn_animals[0], drawn_animals[1])

                        py.draw.rect(WINDOW, BLACK, CUBE_RESULT_MARKING_RECT)
                        Image(CUBERESULT[0][0], CUBERESULT[0][1] - 10, convert_animal_to_img(drawn_animals[0]), 100,
                              100).draw(WINDOW)
                        Image(CUBERESULT[1][0], CUBERESULT[1][1] - 10, convert_animal_to_img(drawn_animals[1]), 100,
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
                        WINDOW.blit(alert, (INFO_RECT[0], INFO_RECT[1]))

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

                    if is_mouse_over(SMALL_DOG_BUTTON):
                        # Small dog icon clicked
                        animals_before = deepcopy(players[player_turn].animals)
                        result = players[player_turn].buy_small_dog()
                        if result == -1:
                            message = "You don't have enough sheep to buy a small dog!"
                        elif result == -2:
                            message = "There are no small dogs left in the bank!"
                        else:
                            message = "You successfully bought a small dog!"

                        py.draw.rect(WINDOW, BLACK, INFO_RECT)
                        alert = font.render(message, True, WHITE)
                        WINDOW.blit(alert, (INFO_RECT[0], INFO_RECT[1]))
                        board.update_board(WINDOW, players[player_turn], animals_before, players[player_turn].animals, CELL_SIZE)
                        py.display.flip()

                    if is_mouse_over(BIG_DOG_BUTTON):
                        # Big dog icon clicked
                        animals_before = deepcopy(players[player_turn].animals)
                        result = players[player_turn].buy_big_dog()
                        if result == -1:
                            message = "You don't have enough cows to buy a big dog!"
                        elif result == -2:
                            message = "There are no big dogs left in the bank!"
                        else:
                            message = "You successfully bought a big dog!"

                        py.draw.rect(WINDOW, BLACK, INFO_RECT)
                        alert = font.render(message, True, WHITE)
                        WINDOW.blit(alert, (INFO_RECT[0], INFO_RECT[1]))
                        board.update_board(WINDOW, players[player_turn], animals_before, players[player_turn].animals, CELL_SIZE)
                        py.display.flip()

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

                    # if 0.7 * WINWIDTH <= mpos_x <= 0.7 * WINWIDTH + 50 and 0.1 * WINHEIGHT <= mpos_y <= 0.1 * WINHEIGHT + 50:
                    #     # Small dog icon clicked
                    #     print("Small dog")
                    #     print(players[player_turn].animals)
                    #     print(players[player_turn].buy_small_dog())
                    #     print(players[player_turn].dogs)
                    # if 0.85 * WINWIDTH <= mpos_x <= 0.85 * WINWIDTH + 50 and 0.1 * WINHEIGHT <= mpos_y <= 0.1 * WINHEIGHT + 50:
                    #     # Big dog icon clicked
                    #     print("Big dog")
                    #     print(players[player_turn].animals)
                    #     print(players[player_turn].buy_big_dog())
                    #     print(players[player_turn].dogs)

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
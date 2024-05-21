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


        def draw_alert(WINDOW, message):
            alert_rect = (0.3*WINWIDTH, 0.3*WINHEIGHT, 500, 300)
            py.draw.rect(WINDOW, WHITE, alert_rect)
            #py.draw.rect(WINDOW, WHITE, alert_rect, 3)

            # alert_text_surface_1 = font.render("How many animals would you like", True, BLACK)
            # alert_text_surface_2 = font.render("                      to exchange?", True, BLACK)
            # #alert_text_rect = alert_text_surface.get_rect(center=alert_rect.center)
            # WINDOW.blit(alert_text_surface_1, (alert_rect[0]+20, alert_rect[1]+20))
            # WINDOW.blit(alert_text_surface_2, (alert_rect[0]+20, alert_rect[1]+50))

            win_text_surface = font.render(message, True, BLACK)
            WINDOW.blit(win_text_surface, (alert_rect[0] + 20, alert_rect[1] + 20))

            OK_BUTTON = (alert_rect[0]+alert_rect[2]/2-50, alert_rect[1]+alert_rect[3]-100, 100, 50)
            py.draw.rect(WINDOW, GREEN, OK_BUTTON)
            ok_text_surface = font.render("OK", True, WHITE)
            WINDOW.blit(ok_text_surface, (OK_BUTTON[0]+27, OK_BUTTON[1]+10))
            return OK_BUTTON

        def check_win(player):
            for animal, count in player.animals.items():
                if count <= 0:
                    print(animal, count)
                    return False
            print("WINWINWIN")
            win[player.id] = True
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
        start = [-1, -1]
        for_exchange = [[None, None, None] for _ in range(len(players))]

        # For alert
        show_alert = False
        ok_button = None

        # Win validator
        win = [False for _ in range(len(players))]

        # Input
        # input_validator = pti.TextInputManager(validator=lambda input_value: isinstance(input_value, int))
        # no_animals_input = pti.TextInputVisualizer(manager=input_validator, font_object=font)
        # no_animals_input.cursor_width = 4
        # no_animals_input.cursor_blink_interval = 400
        # no_animals_input.antialias = False
        # no_animals_input.font_color = GREEN
        # WINDOW.blit(no_animals_input.surface, (0, 0))
        # py.display.update()

        while AppClass.running:
            while all(not val for val in win):
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

                if show_alert:
                    ok_button = draw_alert(WINDOW, "")

                for event in py.event.get():
                    if event.type == QUIT:
                        AppClass.running = False
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            AppClass.running = False

                    if event.type == MOUSEBUTTONDOWN:
                        if show_alert and ok_button is not None and is_mouse_over(ok_button):
                            show_alert = False
                            print(show_alert)

                        #no_animals_input.update(event)
                        # Get the position of the mouse
                        mpos_x, mpos_y = event.pos

                        # Before clicking cube button we can exchange animals
                        # First value represents an animal to exchange, second is equivalent to the number of these animals
                        # and third represents an animal which player wants to get after exchange.

                        a, b = get_clicked_circle(mpos_x, mpos_y)
                        if a != -1 and b != -1:
                            if b > (players[player_turn].animals[util.Animal(a)]-1) // 2 and for_exchange[player_turn][0] is None:
                                py.draw.rect(WINDOW, BLACK, INFO_RECT)
                                alert = font.render("You don't have animals there!", True, WHITE)
                                WINDOW.blit(alert, (INFO_RECT[0], INFO_RECT[1]))
                                py.display.flip()
                                time.delay(1000)
                                py.draw.rect(WINDOW, BLACK, INFO_RECT)
                                break

                            print(for_exchange[player_turn], start[player_turn], b, (players[player_turn].animals[util.Animal(a)]-1) // 2)
                            if (for_exchange[player_turn][0] is None and for_exchange[player_turn][1] is None
                                    and b <= (players[player_turn].animals[util.Animal(a)]-1) // 2):
                                # First animal clicked
                                for_exchange[player_turn][0] = util.Animal(a)
                                start[player_turn] = b*2
                                board.mark_animals_for_exchange(WINDOW, players[player_turn], util.Animal(a),
                                                                             b, b, CELL_SIZE)
                                print("TU: ", for_exchange[player_turn])
                            elif for_exchange[player_turn][1] is None and start[player_turn] != -1:
                                print("TUU: ", for_exchange[player_turn])
                                if (util.Animal(a) == for_exchange[player_turn][0]
                                        and b <= (players[player_turn].animals[util.Animal(a)]-1) // 2):
                                    # Same animal clicked
                                    for_exchange[player_turn][1] = (
                                            min((b+1)*2, players[player_turn].animals[util.Animal(a)]) - start[player_turn])
                                    board.mark_animals_for_exchange(WINDOW, players[player_turn], util.Animal(a),
                                                                                 start[player_turn] // 2, b, CELL_SIZE)
                                    print(for_exchange)
                                elif (util.Animal(a) != for_exchange[player_turn][0]
                                      and b <= (players[player_turn].animals[util.Animal(a)]-1)//2):
                                    # Another animal clicked
                                    print("Another animal")
                                    board.unmark_animals_for_exchange(WINDOW, players[player_turn],
                                                                      for_exchange[player_turn][0], start[player_turn] // 2,
                                                                      start[player_turn] // 2, CELL_SIZE)
                                    for_exchange[player_turn][0] = util.Animal(a)
                                    start[player_turn] = b*2
                                    board.mark_animals_for_exchange(WINDOW, players[player_turn], util.Animal(a),
                                                                                 b, b, CELL_SIZE)
                                    print(for_exchange)
                                print("TUU: ", for_exchange[player_turn])
                            elif for_exchange[player_turn][1] is not None and for_exchange[player_turn][2] is None:
                                print("TUUU: ", for_exchange[player_turn])
                                if util.Animal(a) == for_exchange[player_turn][0]:
                                    py.draw.rect(WINDOW, BLACK, INFO_RECT)
                                    alert = font.render("You can't exchange animal for the same type", True, WHITE)
                                    WINDOW.blit(alert, (INFO_RECT[0], INFO_RECT[1]))
                                    py.display.flip()
                                    time.delay(1000)
                                    py.draw.rect(WINDOW, BLACK, INFO_RECT)
                                else:
                                    for_exchange[player_turn][2] = util.Animal(a)
                                    print("Just before exchange: ", for_exchange[player_turn])
                                    animals_before = deepcopy(players[player_turn].animals)
                                    exchange_result = players[player_turn].exchange_animals(for_exchange[player_turn][0],
                                                                                            for_exchange[player_turn][1],
                                                                                            for_exchange[player_turn][2])

                                    if exchange_result < 0:
                                        py.draw.rect(WINDOW, BLACK, INFO_RECT)
                                        alert = font.render("Too few animals to exchange", True, WHITE)
                                        WINDOW.blit(alert, (INFO_RECT[0], INFO_RECT[1]))
                                        py.display.flip()
                                        time.delay(1000)
                                        board.unmark_animals_for_exchange(WINDOW, players[player_turn], for_exchange[player_turn][0],
                                                                          start[player_turn] // 2,
                                                        (start[player_turn] + for_exchange[player_turn][1] - 1) // 2, CELL_SIZE)
                                        py.draw.rect(WINDOW, BLACK, INFO_RECT)
                                    else:
                                        if exchange_result == 1:
                                            py.draw.rect(WINDOW, BLACK, INFO_RECT)
                                            alert = font.render("You successfully exchanged your animals!", True, WHITE)
                                            WINDOW.blit(alert, (INFO_RECT[0], INFO_RECT[1]))
                                            py.display.flip()
                                            time.delay(1000)
                                            board.unmark_animals_for_exchange(WINDOW, players[player_turn],
                                                                              for_exchange[player_turn][0], start[player_turn] // 2,
                                                                              (start[player_turn] + for_exchange[player_turn][1] - 1) // 2, CELL_SIZE)
                                            py.draw.rect(WINDOW, BLACK, INFO_RECT)
                                            board.update_board(WINDOW, players[player_turn], animals_before,
                                                               players[player_turn].animals, CELL_SIZE)
                                            print("AAAA")
                                            py.display.flip()
                                        else:
                                            py.draw.rect(WINDOW, BLACK, INFO_RECT)
                                            alert = font.render("There are no animals left in the bank for exchange!", True, WHITE)
                                            WINDOW.blit(alert, (INFO_RECT[0], INFO_RECT[1]))
                                            py.display.flip()
                                            time.delay(1000)
                                            board.unmark_animals_for_exchange(WINDOW, players[player_turn],
                                                                              for_exchange[player_turn][0],
                                                                              start[player_turn] // 2,
                                                                              (start[player_turn] +
                                                                               for_exchange[player_turn][1] - 1) // 2, CELL_SIZE)
                                            py.draw.rect(WINDOW, BLACK, INFO_RECT)

                                    start[player_turn] = -1
                                    for_exchange[player_turn] = [None, None, None]
                            check_win(players[player_turn])
                        else:
                            for_exchange[player_turn] = [None, None, None]


                        if is_mouse_over(CUBEBUTTON):
                            py.draw.rect(WINDOW, BLACK, INFO_RECT)
                            py.display.flip()
                            message = ""
                            # print("TUU")
                            FIRSTCOLOR = RED
                            SECONDCOLOR = GREEN
                            for_exchange = [[None, None, None] for _ in range(len(players))]
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

                            check_win(players[player_turn])

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



                py.display.flip()
            draw_alert(WINDOW, "Player " + str(win.index(True)) + " won! Congrats!")
            py.display.flip()
            time.delay(100000)
            CLOCK.tick(60)


    py.quit()
# end class


if __name__ == '__main__':
    players = create_users(2)
    print(players)

    AppClass().play()
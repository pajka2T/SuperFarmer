from copy import deepcopy

import pygame as py
from pygame.locals import *

import util
from board_initializer import BoardInitializer
from exchange_mechanism import ExchangeMechanism
from interaction_actions import (check_win, draw_alert, get_clicked_circle,
                                 is_mouse_over)
from on_change_drawings import draw_dogs, rotate_animation, update_board
from players_data import create_users
from util import Image, convert_animal_to_dice_img


class App:
    def __init__(self, no_players: int = 2) -> None:
        self.players = create_users(no_players)
        App.running = True

    def play(self) -> None:
        player_turn = 0
        py.init()

        WINWIDTH = 1500
        WINHEIGHT = 800
        WINSIZE = (WINWIDTH, WINHEIGHT)

        # Kolory
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        DARKRED = (145, 0, 0)
        BLU = (52, 229, 235)
        BLU2 = (93, 190, 194)
        BLU3 = (38, 125, 128)
        # DARKBLUE = (145, 145, 0)
        DARKGREY = (59, 59, 59)
        GREEN = (0, 255, 0)
        COLORS = [[] for _ in range(2)]
        COLORS[0].append(RED)
        COLORS[0].append(DARKRED)
        COLORS[1].append(BLU2)
        COLORS[1].append(BLU3)

        redarrow = py.image.load("Images/down-arrow.png")
        bluearrow = py.image.load("Images/arrow-left.png")
        bluearrow = py.transform.rotate(bluearrow, 90)

        # Cube buttons
        CUBERESULT = [(650, 380), (750, 380)]
        CUBE_RESULT_MARKING_RECT = (650, 370, 200, 100)

        INFO_RECT = (0.2 * WINWIDTH, 0.05 * WINHEIGHT, 650, 50)

        # Dogs buttons

        RECT_BEHIND_SMALL_DOG_IMAGE = (
            0.7 * WINWIDTH - 5,
            0.05 * WINHEIGHT - 10,
            95,
            100,
        )
        RECT_BEHIND_BIG_DOG_IMAGE = (
            0.85 * WINWIDTH - 5,
            0.05 * WINHEIGHT - 10,
            95,
            100,
        )

        message = ""

        # create the WINDOW and CLOCK
        WINDOW = py.display.set_mode(WINSIZE)
        py.display.set_caption("Super Farmer")
        print("TUTAJ")
        CLOCK = py.time.Clock()
        board = BoardInitializer()
        CELL_SIZE, CUBE_BUTTON, SMALL_DOG_BUTTON, BIG_DOG_BUTTON, font = (
            board.create_board(WINDOW)
        )
        py.display.flip()

        bluefarmer = py.image.load("Images/bluefarmer.png").convert_alpha()
        bluefarmer_width, bluefarmer_height = bluefarmer.get_size()
        redfarmer = py.image.load("Images/redfarmer.png").convert_alpha()
        redfarmer_width, redfarmer_height = redfarmer.get_size()

        small_dog = py.image.load("Images/smalldog.png")
        big_dog = py.image.load("Images/bigdog.png")

        # # Animacja farmera
        # for i in range(10):
        #     Image(WINWIDTH - bluefarmer_width / 4 - i * 5, WINHEIGHT - bluefarmer_height / 3 - i * 5, bluefarmer,
        #           bluefarmer_width / 3 + i * 10, bluefarmer_height / 3 + i * 10).draw(WINDOW)
        #     py.display.update()
        #     CLOCK.tick(40)
        # for i in range(10, -1, -1):
        #     py.draw.rect(WINDOW, BLACK, (WINWIDTH - bluefarmer_width / 4-i*5, WINHEIGHT - bluefarmer_height / 3-i*5,
        #               bluefarmer_width / 3+i*10, bluefarmer_height / 3+i*10))
        #     Image(WINWIDTH - bluefarmer_width / 4 - i * 5, WINHEIGHT - bluefarmer_height / 3 - i * 5, bluefarmer,
        #           bluefarmer_width / 3 + i * 10, bluefarmer_height / 3 + i * 10).draw(WINDOW)
        #     py.display.update()
        #     CLOCK.tick(40)

        # ImageGrid(-redfarmer_width / 10, WINHEIGHT - redfarmer_height / 3, redfarmer, redfarmer_width / 3,
        #          redfarmer_height / 3).draw(WINDOW)

        # WINDOW.blit(cube_button_text_surface, (CUBEBUTTON[0], CUBEBUTTON[1]))
        # WINDOW.blit(cube_button_text_surface, (CUBEBUTTON[0]+20, CUBEBUTTON[1]+10))
        # print(util.Animal(0).value)
        # for i in range(5):
        #     board.drawcircles(WINDOW, BLU, BLU2, BLU3,
        #                       animalBoardCoordinates[0][i][len(animalBoardCoordinates[0][i]) - 1][2],
        #                       animalBoardCoordinates[0][i][len(animalBoardCoordinates[0][i]) - 1][3],
        #                       animalBoardCoordinates[0][i][len(animalBoardCoordinates[0][i]) - 1][1],
        #                       util.convert_animal_to_img(i),
        #                       animalBoardCoordinates[0][i][len(animalBoardCoordinates[0][i]) - 1][4],
        #                       CELL_SIZE)

        # board.drawcircles(WINDOW, BLU, BLU2, BLU3, animalBoardCoordinates[0][0][n-1][2],
        #                  animalBoardCoordinates[0][0][n-1][3], animalBoardCoordinates[0][0][n-1][1],
        #                  util.convert_animal_to_img(0), animalBoardCoordinates[0][0][n-1][4], CELL_SIZE)

        # for i in range(1, 5):
        #     board.draw_animal()(WINDOW, BLU, animalBoardCoordinates[0][0][i][0],
        #                       animalBoardCoordinates[0][0][i][1], CELL_SIZE / 2, 10, util.convert_animal_to_img(0))

        # Dogs bank

        # For exchange
        start = [-1, -1]
        for_exchange = [[None, None, None] for _ in range(len(self.players))]

        # For alert
        show_alert = False
        ok_button = None

        exc_mech = ExchangeMechanism(WINDOW, board)

        # Win validator
        win = [False for _ in range(len(self.players))]

        # Input
        # input_validator = pti.TextInputManager(validator=lambda input_value: isinstance(input_value, int))
        # no_animals_input = pti.TextInputVisualizer(manager=input_validator, font_object=font)
        # no_animals_input.cursor_width = 4
        # no_animals_input.cursor_blink_interval = 400
        # no_animals_input.antialias = False
        # no_animals_input.font_color = GREEN
        # WINDOW.blit(no_animals_input.surface, (0, 0))
        # py.display.update()

        cube_button_text_surface = font.render("Roll the dices", True, (255, 255, 255))

        while App.running:
            for event in py.event.get():
                if event.type == QUIT:
                    App.running = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        App.running = False
            while all(not val for val in win):
                if is_mouse_over(CUBE_BUTTON):
                    py.draw.rect(WINDOW, COLORS[player_turn][1], CUBE_BUTTON)
                    WINDOW.blit(
                        cube_button_text_surface,
                        (CUBE_BUTTON[0] + 20, CUBE_BUTTON[1] + 10),
                    )
                else:
                    py.draw.rect(WINDOW, COLORS[player_turn][0], CUBE_BUTTON)
                    WINDOW.blit(
                        cube_button_text_surface,
                        (CUBE_BUTTON[0] + 20, CUBE_BUTTON[1] + 10),
                    )

                if is_mouse_over(SMALL_DOG_BUTTON):
                    py.draw.rect(WINDOW, DARKGREY, RECT_BEHIND_SMALL_DOG_IMAGE)
                    Image(
                        SMALL_DOG_BUTTON[0],
                        SMALL_DOG_BUTTON[1],
                        small_dog,
                        SMALL_DOG_BUTTON[2],
                        SMALL_DOG_BUTTON[3],
                    ).draw(WINDOW)
                else:
                    py.draw.rect(WINDOW, BLACK, RECT_BEHIND_SMALL_DOG_IMAGE)
                    Image(
                        SMALL_DOG_BUTTON[0],
                        SMALL_DOG_BUTTON[1],
                        small_dog,
                        SMALL_DOG_BUTTON[2],
                        SMALL_DOG_BUTTON[3],
                    ).draw(WINDOW)

                if is_mouse_over(BIG_DOG_BUTTON):
                    py.draw.rect(WINDOW, DARKGREY, RECT_BEHIND_BIG_DOG_IMAGE)
                    Image(
                        BIG_DOG_BUTTON[0],
                        BIG_DOG_BUTTON[1],
                        big_dog,
                        BIG_DOG_BUTTON[2],
                        BIG_DOG_BUTTON[3],
                    ).draw(WINDOW)
                else:
                    py.draw.rect(WINDOW, BLACK, RECT_BEHIND_BIG_DOG_IMAGE)
                    Image(
                        BIG_DOG_BUTTON[0],
                        BIG_DOG_BUTTON[1],
                        big_dog,
                        BIG_DOG_BUTTON[2],
                        BIG_DOG_BUTTON[3],
                    ).draw(WINDOW)

                if show_alert:
                    ok_button = draw_alert(WINDOW, "", font)

                if player_turn == 0:
                    py.draw.rect(WINDOW, BLACK, (1400, 370, 70, 70))
                    Image(30, 370, redarrow, 70, 70).draw(WINDOW)
                elif player_turn == 1:
                    py.draw.rect(WINDOW, BLACK, (30, 370, 70, 70))
                    Image(1400, 370, bluearrow, 70, 70).draw(WINDOW)

                draw_dogs(
                    WINDOW,
                    redfarmer_width / 3 + 40,
                    680,
                    1500 - bluefarmer_width / 3,
                    680,
                    small_dog,
                    big_dog,
                    self.players[0].dogs[util.Defence.SMALLDOG],
                    self.players[0].dogs[util.Defence.BIGDOG],
                    self.players[1].dogs[util.Defence.SMALLDOG],
                    self.players[1].dogs[util.Defence.BIGDOG],
                )

                for event in py.event.get():
                    if event.type == QUIT:
                        App.running = False
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            App.running = False

                    if event.type == MOUSEBUTTONDOWN:
                        if (
                            show_alert
                            and ok_button is not None
                            and is_mouse_over(ok_button)
                        ):
                            show_alert = False
                            print(show_alert)

                        # no_animals_input.update(event)
                        # Get the position of the mouse
                        mpos_x, mpos_y = event.pos

                        # Before clicking cube button we can exchange animals
                        # First value represents an animal to exchange, second is equivalent to the number of these animals
                        # and third represents an animal which player wants to get after exchange.

                        a, b = get_clicked_circle(
                            mpos_x,
                            mpos_y,
                            player_turn,
                            board.animal_board_coordinates,
                            CELL_SIZE,
                        )
                        if a != -1 and b != -1:
                            exc_mech.exchange(
                                a, b, self.players, player_turn, win, INFO_RECT, font
                            )
                        else:
                            exc_mech.reset_for_exchange(self.players[player_turn])

                        if is_mouse_over(CUBE_BUTTON):
                            py.draw.rect(WINDOW, BLACK, INFO_RECT)
                            py.display.flip()
                            message = ""
                            # print("TUU")
                            FIRSTCOLOR = RED
                            SECONDCOLOR = GREEN
                            exc_mech.reset_for_exchange(self.players[player_turn])
                            drawn_animals = util.rand_animals()

                            animals_before = deepcopy(self.players[player_turn].animals)

                            res1, res2 = self.players[player_turn].add_animals(
                                drawn_animals[0], drawn_animals[1]
                            )

                            py.draw.rect(WINDOW, BLACK, CUBE_RESULT_MARKING_RECT)
                            # Image(CUBERESULT[0][0], CUBERESULT[0][1] - 10, convert_animal_to_img(drawn_animals[0]), 100,
                            #      100).draw(WINDOW)
                            # Image(CUBERESULT[1][0], CUBERESULT[1][1] - 10, convert_animal_to_img(drawn_animals[1]), 100,
                            #      100).draw(WINDOW)
                            # py.draw.rect(WINDOW, BLACK, CUBE_RESULT_MARKING_RECT)
                            # Image(CUBERESULT[0][0], CUBERESULT[0][1] - 10, convert_animal_to_dice_img(drawn_animals[0], 1), 100,
                            #       100).draw(WINDOW)
                            # Image(CUBERESULT[1][0], CUBERESULT[1][1] - 10, convert_animal_to_dice_img(drawn_animals[1], 2), 100,
                            #       100).draw(WINDOW)
                            rotate_animation(
                                WINDOW,
                                convert_animal_to_dice_img(drawn_animals[0], 1),
                                convert_animal_to_dice_img(drawn_animals[1], 2),
                                BLACK,
                                CLOCK,
                                CUBERESULT[0][0] + 40,
                                CUBERESULT[0][1] + 40,
                                100,
                            )
                            # board.rotate_animation(WINDOW, convert_animal_to_dice_img(drawn_animals[1], 2), BLACK, CLOCK,
                            #                       CUBERESULT[0][0] + 140, CUBERESULT[0][1] + 40)

                            print(res1, res2)
                            if res1 == util.Predators.FOX:
                                message = f"Oh no, there was a fox attack on player {player_turn+1}!"
                            elif res1 == util.Defence.SMALLDOG:
                                message = f"The small dog saved player {player_turn+1} from fox attack!"
                            if res2 == util.Predators.WOLF:
                                message = f"Oh no, there was a wolf attack on player {player_turn+1}!"
                            elif res2 == util.Defence.BIGDOG:
                                message = f"The big dog saved player {player_turn+1} from wolf attack!"
                            if (
                                res1 == util.Predators.FOX
                                and res2 == util.Predators.WOLF
                            ):
                                message = f"Oh no, there was a fox-and-wolf attack on player {player_turn+1}!"
                            print("AAA")

                            alert = font.render(message, True, WHITE)
                            WINDOW.blit(alert, (INFO_RECT[0], INFO_RECT[1]))

                            update_board(
                                WINDOW,
                                self.players[player_turn],
                                animals_before,
                                self.players[player_turn].animals,
                                board.animal_board_coordinates,
                                CELL_SIZE,
                            )

                            check_win(self.players[player_turn], win)

                            player_turn += 1
                            player_turn %= 2

                        if is_mouse_over(SMALL_DOG_BUTTON):
                            # Small dog icon clicked
                            animals_before = deepcopy(self.players[player_turn].animals)
                            result = self.players[player_turn].buy_small_dog()
                            if result == -1:
                                message = (
                                    "You don't have enough sheep to buy a small dog!"
                                )
                            elif result == -2:
                                message = "There are no small dogs left in the bank!"
                            else:
                                message = "You successfully bought a small dog!"

                            py.draw.rect(WINDOW, BLACK, INFO_RECT)
                            alert = font.render(message, True, WHITE)
                            WINDOW.blit(alert, (INFO_RECT[0], INFO_RECT[1]))
                            update_board(
                                WINDOW,
                                self.players[player_turn],
                                animals_before,
                                self.players[player_turn].animals,
                                board.animal_board_coordinates,
                                CELL_SIZE,
                            )
                            py.display.flip()

                        if is_mouse_over(BIG_DOG_BUTTON):
                            # Big dog icon clicked
                            animals_before = deepcopy(self.players[player_turn].animals)
                            result = self.players[player_turn].buy_big_dog()
                            if result == -1:
                                message = "You don't have enough cows to buy a big dog!"
                            elif result == -2:
                                message = "There are no big dogs left in the bank!"
                            else:
                                message = "You successfully bought a big dog!"

                            py.draw.rect(WINDOW, BLACK, INFO_RECT)
                            alert = font.render(message, True, WHITE)
                            WINDOW.blit(alert, (INFO_RECT[0], INFO_RECT[1]))
                            update_board(
                                WINDOW,
                                self.players[player_turn],
                                animals_before,
                                self.players[player_turn].animals,
                                board.animal_board_coordinates,
                                CELL_SIZE,
                            )
                            py.display.flip()

                py.display.flip()
            draw_alert(
                WINDOW, "Player " + str(win.index(True)) + " won! Congrats!", font
            )
            py.display.flip()
            py.time.delay(100000)
            CLOCK.tick(60)

    py.quit()


# end class

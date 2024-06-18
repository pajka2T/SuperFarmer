from copy import deepcopy

import pygame as py
from pygame import Surface
from pygame.locals import *

import util
from board_initializer import BoardInitializer
from exchange_mechanism import ExchangeMechanism
from interaction_actions import check_win, get_clicked_circle, is_mouse_over
from on_change_drawings import draw_dogs, rotate_animation, update_board
from players_data import Player, create_players
from util import Bank, Image, black, white


class GameLogic:
    """
    Class responsible for tracking all actions happening during gameplay.
    """
    def __init__(
        self,
        window: Surface,
        board: BoardInitializer,
        players: list[Player],
        starting_player_number: int = 0,
    ) -> None:
        self.window = window
        self.board = board
        self.players = players
        self.player_turn = starting_player_number
        self.bank = Bank()
        self.exc_mech = ExchangeMechanism(window, board, self.bank)
        self.clock = py.time.Clock()
        self.win = [False for _ in range(len(players))]
        self.info_rect = None

    def gameplay(self, event) -> bool:
        """
        It is responsible for whole game logic and gameplay.
        Returns True if someone won or False otherwise.
        :param event:
        :return: bool
        """
        someone_won = False
        self.clock.tick(50)
        start_rotation_fps = 100

        small_dog = py.image.load("Images/smalldog.png")
        big_dog = py.image.load("Images/bigdog.png")

        cube_result = [(650, 380), (750, 380)]
        cube_result_marking_rect = (650, 370, 200, 100)

        self.info_rect = (
            0.2 * self.window.get_width(),
            0.05 * self.window.get_height(),
            650,
            50,
        )

        self.check_turn()
        py.display.flip()

        if event.type == MOUSEBUTTONDOWN:
            mpos_x, mpos_y = event.pos

            a, b = get_clicked_circle(
                mpos_x,
                mpos_y,
                self.player_turn,
                self.board.animal_board_coordinates,
                self.board.cell_size,
            )
            if a != -1 and b != -1:
                self.exc_mech.exchange(
                    a,
                    b,
                    self.players,
                    self.player_turn,
                    self.win,
                    self.info_rect,
                    self.board.font,
                )
            else:
                self.exc_mech.reset_for_exchange(self.players[self.player_turn])

            for el in self.win:
                if el:
                    someone_won = True

            if is_mouse_over(self.board.cube_button):
                py.draw.rect(self.window, black, self.info_rect)
                py.display.flip()
                message = ""
                self.exc_mech.reset_for_exchange(self.players[self.player_turn])
                drawn_animals = util.rand_animals()

                animals_before = deepcopy(self.players[self.player_turn].animals)

                res1, res2 = self.players[self.player_turn].add_animals(
                    drawn_animals[0], drawn_animals[1], self.bank
                )

                py.draw.rect(self.window, black, cube_result_marking_rect)

                rotate_animation(
                    self.window,
                    util.convert_animal_to_dice_img(drawn_animals[0], 1),
                    util.convert_animal_to_dice_img(drawn_animals[1], 2),
                    black,
                    self.clock,
                    start_rotation_fps,
                    cube_result[0][0] + 40,
                    cube_result[0][1] + 40,
                    100,
                )

                print(res1, res2)
                if res1 == util.Predators.FOX:
                    message = f"Oh no, there was a fox attack on player {self.player_turn + 1}!"
                elif res1 == util.Defence.SMALLDOG:
                    message = f"The small dog saved player {self.player_turn + 1} from fox attack!"
                if res2 == util.Predators.WOLF:
                    message = f"Oh no, there was a wolf attack on player {self.player_turn + 1}!"
                elif res2 == util.Defence.BIGDOG:
                    message = f"The big dog saved player {self.player_turn + 1} from wolf attack!"
                if res1 == util.Predators.FOX and res2 == util.Predators.WOLF:
                    message = f"Oh no, there was a fox-and-wolf attack on player {self.player_turn + 1}!"
                    print("AAA")

                alert = self.board.font.render(message, True, white)
                self.window.blit(alert, (self.info_rect[0], self.info_rect[1]))

                update_board(
                    self.window,
                    self.players[self.player_turn],
                    animals_before,
                    self.players[self.player_turn].animals,
                    self.board.animal_board_coordinates,
                    self.board.cell_size,
                )

                draw_dogs(
                    self.window,
                    380,
                    self.window.get_width() - 350,
                    680,
                    small_dog,
                    big_dog,
                    self.players[0].dogs[util.Defence.SMALLDOG],
                    self.players[0].dogs[util.Defence.BIGDOG],
                    self.players[1].dogs[util.Defence.SMALLDOG],
                    self.players[1].dogs[util.Defence.BIGDOG],
                )

                someone_won = check_win(self.players[self.player_turn], self.win)

                self.player_turn += 1
                self.player_turn %= 2

            if is_mouse_over(self.board.small_dog_button):
                # Small dog icon clicked
                animals_before = deepcopy(self.players[self.player_turn].animals)
                result = self.players[self.player_turn].buy_small_dog(self.bank)
                if result == -1:
                    message = "You don't have enough sheep to buy a small dog!"
                elif result == -2:
                    message = "There are no small dogs left in the bank!"
                else:
                    message = "You successfully bought a small dog!"

                py.draw.rect(self.window, black, self.info_rect)
                alert = self.board.font.render(message, True, white)
                self.window.blit(alert, (self.info_rect[0], self.info_rect[1]))
                update_board(
                    self.window,
                    self.players[self.player_turn],
                    animals_before,
                    self.players[self.player_turn].animals,
                    self.board.animal_board_coordinates,
                    self.board.cell_size,
                )
                draw_dogs(
                    self.window,
                    380,
                    self.window.get_width() - 350,
                    680,
                    small_dog,
                    big_dog,
                    self.players[0].dogs[util.Defence.SMALLDOG],
                    self.players[0].dogs[util.Defence.BIGDOG],
                    self.players[1].dogs[util.Defence.SMALLDOG],
                    self.players[1].dogs[util.Defence.BIGDOG],
                )
                py.display.flip()

            if is_mouse_over(self.board.big_dog_button):
                # Big dog icon clicked
                animals_before = deepcopy(self.players[self.player_turn].animals)
                result = self.players[self.player_turn].buy_big_dog(self.bank)
                if result == -1:
                    message = "You don't have enough cows to buy a big dog!"
                elif result == -2:
                    message = "There are no big dogs left in the bank!"
                else:
                    message = "You successfully bought a big dog!"

                py.draw.rect(self.window, black, self.info_rect)
                alert = self.board.font.render(message, True, white)
                self.window.blit(alert, (self.info_rect[0], self.info_rect[1]))
                update_board(
                    self.window,
                    self.players[self.player_turn],
                    animals_before,
                    self.players[self.player_turn].animals,
                    self.board.animal_board_coordinates,
                    self.board.cell_size,
                )
                draw_dogs(
                    self.window,
                    380,
                    self.window.get_width() - 350,
                    680,
                    small_dog,
                    big_dog,
                    self.players[0].dogs[util.Defence.SMALLDOG],
                    self.players[0].dogs[util.Defence.BIGDOG],
                    self.players[1].dogs[util.Defence.SMALLDOG],
                    self.players[1].dogs[util.Defence.BIGDOG],
                )
                py.display.flip()
        self.check_turn()
        py.display.flip()
        return someone_won

    # end def

    def check_turn(self) -> None:
        """
        Function responsible for drawing proper arrows according to player turn.
        :return:
        """

        red_arrow = py.image.load("Images/down-arrow.png")
        blue_arrow = py.image.load("Images/arrow-left.png")
        blue_arrow = py.transform.rotate(blue_arrow, 90)

        black = (0, 0, 0)

        if self.player_turn == 0:
            py.draw.rect(self.window, black, (1400, 370, 70, 70))
            Image(30, 370, red_arrow, 70, 70).draw(self.window)
        elif self.player_turn == 1:
            py.draw.rect(self.window, black, (30, 370, 70, 70))
            Image(1400, 370, blue_arrow, 70, 70).draw(self.window)

    # end def

    def restart_game(self, board: BoardInitializer, starting_player_number: int):
        self.board = board
        self.players = create_players(board.no_players)
        self.player_turn = starting_player_number
        self.win = [False for _ in range(board.no_players)]
        self.bank.reset_bank()
        self.exc_mech.bank = self.bank

    # end def

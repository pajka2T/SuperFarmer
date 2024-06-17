from copy import deepcopy

import pygame as py
from pygame import Surface

from board_initializer import BoardInitializer
from interaction_actions import check_win
from on_change_drawings import (mark_animals_for_exchange,
                                unmark_animals_for_exchange, update_board)
from players_data import Player
from util import Animal


class ExchangeMechanism:
    def __init__(
        self, window: Surface, board: BoardInitializer, no_players: int = 2
    ) -> None:
        """
        First value of for_exchange list represents an animal to exchange, second is equivalent to the number
        of these animals and third represents an animal which player wants to get after exchange.
        """
        self.window = window
        self.board = board
        self.no_players = no_players
        self.for_exchange = [[None, None, None] for _ in range(no_players)]
        self.start = [-1 for _ in range(no_players)]

    # end def

    def exchange(
        self,
        a: int,
        b: int,
        players: list[Player],
        player_turn: int,
        win: list[bool],
        info_rect: tuple[float, float, float, float],
        font: py.font.Font,
        white: tuple[int, int, int] = (255, 255, 255),
        black: tuple[int, int, int] = (0, 0, 0),
    ) -> None:
        """
        Before clicking cube button we can exchange animals using this function.
        """

        if (
            b > (players[player_turn].animals[Animal(a)] - 1) // 2
            and self.for_exchange[player_turn][0] is None
        ):
            py.draw.rect(self.window, black, info_rect)
            alert = font.render("You don't have animals there!", True, white)
            self.window.blit(alert, (info_rect[0], info_rect[1]))
            py.display.flip()
            py.time.delay(1000)
            py.draw.rect(self.window, black, info_rect)
            return

        print(
            self.for_exchange[player_turn],
            self.start[player_turn],
            b,
            (players[player_turn].animals[Animal(a)] - 1) // 2,
        )
        if (
            self.for_exchange[player_turn][0] is None
            and self.for_exchange[player_turn][1] is None
            and b <= (players[player_turn].animals[Animal(a)] - 1) // 2
        ):
            # First animal clicked
            self.for_exchange[player_turn][0] = Animal(a)
            self.start[player_turn] = b * 2
            mark_animals_for_exchange(
                self.window,
                players[player_turn],
                Animal(a),
                b,
                b,
                self.board.animal_board_coordinates,
                self.board.cell_size,
            )
            print("TU: ", self.for_exchange[player_turn])
        elif (
            self.for_exchange[player_turn][1] is None and self.start[player_turn] != -1
        ):
            print("TUU: ", self.for_exchange[player_turn], b, self.start[player_turn])
            if (
                Animal(a) == self.for_exchange[player_turn][0]
                and b <= (players[player_turn].animals[Animal(a)] - 1) // 2
            ):
                # Same animal clicked
                print(players[player_turn].animals[Animal(a)])
                print("START, B: ", self.start[player_turn], b)
                if b < self.start[player_turn]:
                    b, self.start[player_turn] = self.start[player_turn] // 2, b
                self.for_exchange[player_turn][1] = abs(
                    min(
                        (b + 1) * 2,
                        players[player_turn].animals[Animal(a)],
                    )
                    - self.start[player_turn]
                )
                print(self.for_exchange[player_turn])
                mark_animals_for_exchange(
                    self.window,
                    players[player_turn],
                    Animal(a),
                    self.start[player_turn] // 2,
                    b,
                    self.board.animal_board_coordinates,
                    self.board.cell_size,
                )
                print(self.for_exchange)
            elif (
                Animal(a) != self.for_exchange[player_turn][0]
                and b <= (players[player_turn].animals[Animal(a)] - 1) // 2
            ):
                # Another animal clicked
                print("Another animal")
                unmark_animals_for_exchange(
                    self.window,
                    players[player_turn],
                    self.for_exchange[player_turn][0],
                    self.start[player_turn] // 2,
                    self.start[player_turn] // 2,
                    self.board.animal_board_coordinates,
                    self.board.cell_size,
                )
                self.for_exchange[player_turn][0] = Animal(a)
                self.start[player_turn] = b * 2
                mark_animals_for_exchange(
                    self.window,
                    players[player_turn],
                    Animal(a),
                    b,
                    b,
                    self.board.animal_board_coordinates,
                    self.board.cell_size,
                )
                print(self.for_exchange)
            print("TUU: ", self.for_exchange[player_turn])
        elif (
            self.for_exchange[player_turn][1] is not None
            and self.for_exchange[player_turn][2] is None
        ):
            print("TUUU: ", self.for_exchange[player_turn])
            if Animal(a) == self.for_exchange[player_turn][0]:
                py.draw.rect(self.window, black, info_rect)
                alert = font.render(
                    "You can't exchange animal for the same type",
                    True,
                    white,
                )
                self.window.blit(alert, (info_rect[0], info_rect[1]))
                py.display.flip()
                py.time.delay(1000)
                py.draw.rect(self.window, black, info_rect)
            else:
                self.for_exchange[player_turn][2] = Animal(a)
                print(
                    "Just before exchange: ",
                    self.for_exchange[player_turn],
                )
                animals_before = deepcopy(players[player_turn].animals)
                exchange_result = players[player_turn].exchange_animals(
                    self.for_exchange[player_turn][0],
                    self.for_exchange[player_turn][1],
                    self.for_exchange[player_turn][2],
                )

                if exchange_result < 0:
                    py.draw.rect(self.window, black, info_rect)
                    alert = font.render("Too few animals to exchange", True, white)
                    self.window.blit(alert, (info_rect[0], info_rect[1]))
                    py.display.flip()
                    py.time.delay(1000)
                    unmark_animals_for_exchange(
                        self.window,
                        players[player_turn],
                        self.for_exchange[player_turn][0],
                        self.start[player_turn] // 2,
                        (
                            self.start[player_turn]
                            + self.for_exchange[player_turn][1]
                            - 1
                        )
                        // 2,
                        self.board.animal_board_coordinates,
                        self.board.cell_size,
                    )
                    py.draw.rect(self.window, black, info_rect)
                else:
                    if exchange_result == 1:
                        py.draw.rect(self.window, black, info_rect)
                        alert = font.render(
                            "You successfully exchanged your animals!",
                            True,
                            white,
                        )
                        self.window.blit(alert, (info_rect[0], info_rect[1]))
                        py.display.flip()
                        py.time.delay(1000)
                        unmark_animals_for_exchange(
                            self.window,
                            players[player_turn],
                            self.for_exchange[player_turn][0],
                            self.start[player_turn] // 2,
                            (
                                self.start[player_turn]
                                + self.for_exchange[player_turn][1]
                                - 1
                            )
                            // 2,
                            self.board.animal_board_coordinates,
                            self.board.cell_size,
                        )
                        py.draw.rect(self.window, black, info_rect)
                        update_board(
                            self.window,
                            players[player_turn],
                            animals_before,
                            players[player_turn].animals,
                            self.board.animal_board_coordinates,
                            self.board.cell_size,
                        )
                        print("AAAA")
                        py.display.flip()
                    else:
                        py.draw.rect(self.window, black, info_rect)
                        alert = font.render(
                            "There are no animals left in the bank for exchange!",
                            True,
                            white,
                        )
                        self.window.blit(alert, (info_rect[0], info_rect[1]))
                        py.display.flip()
                        py.time.delay(1000)
                        unmark_animals_for_exchange(
                            self.window,
                            players[player_turn],
                            self.for_exchange[player_turn][0],
                            self.start[player_turn] // 2,
                            (
                                self.start[player_turn]
                                + self.for_exchange[player_turn][1]
                                - 1
                            )
                            // 2,
                            self.board.animal_board_coordinates,
                            self.board.cell_size,
                        )
                        py.draw.rect(self.window, black, info_rect)

                self.start[player_turn] = -1
                self.for_exchange[player_turn] = [None, None, None]
        check_win(players[player_turn], win)

    # end def

    def reset_for_exchange(self, player: Player):
        if not all(val is None for val in self.for_exchange[player.id]):
            update_board(
                self.window,
                player,
                {
                    Animal.RABBIT: 0,
                    Animal.SHEEP: 0,
                    Animal.PIG: 0,
                    Animal.COW: 0,
                    Animal.HORSE: 0,
                },
                player.animals,
                self.board.animal_board_coordinates,
                self.board.cell_size,
            )
        for i in range(len(self.for_exchange)):
            for j in range(len(self.for_exchange[i])):
                self.for_exchange[i][j] = None

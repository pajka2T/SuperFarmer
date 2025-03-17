from copy import deepcopy

import pygame as py
from pygame import Surface

from board_initializer import BoardInitializer
from interaction_actions import check_win
from on_change_drawings import (mark_animals_for_exchange,
                                unmark_animals_for_exchange, update_board)
from players_data import Player
from util import Animal, Bank, black, white


class ExchangeMechanism:
    """
    Class responsible for creating exchange mechanism.
    """

    def __init__(
        self, window: Surface, board: BoardInitializer, bank: Bank, no_players: int = 2
    ) -> None:
        """
        Initializes exchange drawing mechanism.
        :param window: Application window where the board will be drawn.
        :param board: Game board.
        :param bank: Bank of animals.
        :param no_players: Number of players playing.
        """
        self.window = window
        self.board = board
        self.no_players = no_players
        self.for_exchange = [[None, None, None] for _ in range(no_players)]
        self.start = [-1 for _ in range(no_players)]
        self.bank = bank
        """
        First value of for_exchange list represents an animal to exchange, second is equivalent to the number
        of these animals and third represents an animal which player wants to get after exchange.
        """

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
    ) -> None:
        """
        Function responsible for exchanging animals and drawing result by clicking on animals circles.
        We can use it before clicking cube button, so before player's turn.
        :param a: Row of clicked circle.
        :param b: Column of clicked circle.
        :param players: List of players playing.
        :param player_turn: Current turn.
        :param win: List storing the data about winning the game.
        :param info_rect: Rectangle where all the exchange algorithm messages will be shown.
        :param font: Font with which the messages will be shown.
        :return: (None) Only calculates and draws.
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
        elif (
            self.for_exchange[player_turn][1] is None and self.start[player_turn] != -1
        ):
            if (
                Animal(a) == self.for_exchange[player_turn][0]
                and b <= (players[player_turn].animals[Animal(a)] - 1) // 2
            ):
                if b < self.start[player_turn] // 2:
                    b, self.start[player_turn] = self.start[player_turn] // 2, b * 2
                self.for_exchange[player_turn][1] = abs(
                    min(
                        (b + 1) * 2,
                        players[player_turn].animals[Animal(a)],
                    )
                    - self.start[player_turn]
                )
                mark_animals_for_exchange(
                    self.window,
                    players[player_turn],
                    Animal(a),
                    self.start[player_turn] // 2,
                    b,
                    self.board.animal_board_coordinates,
                    self.board.cell_size,
                )
            elif (
                Animal(a) != self.for_exchange[player_turn][0]
                and b <= (players[player_turn].animals[Animal(a)] - 1) // 2
            ):
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
        elif (
            self.for_exchange[player_turn][1] is not None
            and self.for_exchange[player_turn][2] is None
        ):
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
                animals_before = deepcopy(players[player_turn].animals)
                exchange_result = players[player_turn].exchange_animals(
                    self.for_exchange[player_turn][0],
                    self.for_exchange[player_turn][1],
                    self.for_exchange[player_turn][2],
                    self.bank,
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

    def reset_for_exchange(self, player: Player) -> None:
        """
        Resets for_exchange table when exchange is stopped and properly updates board drawing.
        :param player: Player which for_exchange list should be set to None.
        :return: (None) Only changes value of for_exchange list.
        """
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

    # end def


# end class

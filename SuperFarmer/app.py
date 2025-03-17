import pygame as py
from pygame.locals import *

from board_initializer import BoardInitializer
from game_logic import GameLogic
from hover_drawings import on_hover_game, on_hover_menu
from interaction_actions import draw_alert, is_mouse_over
from menu_initializer import MenuInitializer
from players_data import create_players


class App:
    def __init__(self, no_players: int = 2) -> None:
        """
        Initializes application.
        :param no_players: Number of players playing.
        """
        self.players = create_players(no_players)
        App.running = True
        """
        Attribute running specifies whether the application is still running.
        """

    def play(self) -> None:
        """
        Function responsible for application work.
        It starts the application, shows menu, provide game and allows to restart the game after somebody win.
        :return: (None) Only do its own tasks and supervises work of another classes.
        """
        py.init()

        WINWIDTH = 1500
        WINHEIGHT = 800
        WINSIZE = (WINWIDTH, WINHEIGHT)

        WINDOW = py.display.set_mode(WINSIZE)
        py.display.set_caption("Super Farmer")

        font = py.font.Font("Fonts/BRLNSDB.ttf", 28)

        menu = MenuInitializer(font)

        board = BoardInitializer(font)

        py.display.flip()

        game_end = True
        menu_shown = False

        last_starting_player = -1

        game_logic = GameLogic(WINDOW, board, self.players, last_starting_player)

        while App.running:
            if game_end and not menu_shown:
                menu.create_menu(WINDOW)
                menu_shown = True
            elif game_end:
                on_hover_menu(WINDOW, menu)
                py.display.flip()
            elif not game_end:
                on_hover_game(WINDOW, board, game_logic.player_turn)
                py.display.flip()

            for event in py.event.get():
                if event.type == QUIT:
                    App.running = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        App.running = False
                if event.type == MOUSEBUTTONDOWN:
                    if menu_shown:
                        if is_mouse_over(menu.start_button):
                            menu_shown = False
                            game_end = False
                            board.create_board(WINDOW)
                            starting_player = (
                                last_starting_player + 1
                            ) % board.no_players
                            game_logic.restart_game(board, starting_player)
                if not game_end and not menu_shown and game_logic.gameplay(event):
                    game_end = True
                    draw_alert(
                        WINDOW,
                        "Player " + str(game_logic.win.index(True)) + " won! Congrats!",
                        board.font,
                        game_logic.info_rect,
                    )
                    py.display.flip()
                    py.time.delay(2000)
                    break
            py.display.flip()

        py.quit()

    # end def


# end class

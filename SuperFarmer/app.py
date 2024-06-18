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
        self.players = create_players(no_players)
        App.running = True

    def play(self) -> None:
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

        # For alert
        show_alert = False
        ok_button = None
        game_end = True
        menu_shown = False

        starting_player = 0

        game_logic = GameLogic(WINDOW, board, self.players, starting_player)

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
                    # if (
                    #     show_alert
                    #     and ok_button is not None
                    #     and is_mouse_over(ok_button)
                    # ):
                    #     show_alert = False
                    #     print(show_alert)
                    if menu_shown:
                        if is_mouse_over(menu.start_button):
                            menu_shown = False
                            game_end = False
                            board.create_board(WINDOW)
                            starting_player = (starting_player + 1) % board.no_players
                            print("STARTING PLAYER: ", starting_player)
                            game_logic.restart_game(board, starting_player)
                            print(game_logic.bank.animals)
                            print(game_logic.bank.dogs)
                if not game_end and not menu_shown and game_logic.check(event):
                    print("WIN AAA")
                    game_end = True
                    ok_button = draw_alert(
                        WINDOW,
                        "Player " + str(game_logic.win.index(True)) + " won! Congrats!",
                        board.font,
                    )
                    py.display.flip()
                    py.time.delay(2000)
                    break
            py.display.flip()
        draw_alert(
            WINDOW,
            "Player " + str(game_logic.win.index(True)) + " won! Congrats!",
            board.font,
        )
        py.display.flip()
        py.time.delay(5)

        py.quit()


# end class

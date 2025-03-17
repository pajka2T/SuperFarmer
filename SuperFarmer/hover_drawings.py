import pygame as py
from pygame import Surface

from board_initializer import BoardInitializer
from interaction_actions import is_mouse_over
from menu_initializer import MenuInitializer
from util import Image, black, dark_green, dark_grey, green, white


def on_hover_game(
    window: Surface,
    board: BoardInitializer,
    player_turn: int,
    no_players: int = 2,
    cube_button_font: py.font.Font = None,
    colors_list: list[tuple[int, int, int]] = [
        (255, 0, 0),
        (145, 0, 0),
        (93, 190, 194),
        (38, 125, 128),
    ],
) -> None:
    """
    Function responsible for all on hover drawings during game.
    :param window: Surface
    :param board: BoardInitializer
    :param player_turn: int
    :param no_players: int
    :param cube_button_font: py.font.Font
    :param colors_list: list[tuple[int, int, int]]
    :return:
    """
    colors = [[] for _ in range(no_players)]
    for i in range(no_players):
        for j in range(i * 2, (i + 1) * 2):
            colors[i].append(colors_list[j])

    small_dog = py.image.load("Images/smalldog.png")
    big_dog = py.image.load("Images/bigdog.png")

    cube_button_text_surface = (
        (board.font.render("Roll the dices", True, white))
        if cube_button_font is None
        else cube_button_font.render("Roll the dices", True, white)
    )

    rect_behind_small_dog_button = (
        board.small_dog_button[0] - 10,
        board.small_dog_button[1] - 10,
        board.small_dog_button[2] + 20,
        board.small_dog_button[3] + 20,
    )
    rect_behind_big_dog_button = (
        board.big_dog_button[0] - 10,
        board.big_dog_button[1] - 10,
        board.big_dog_button[2] + 20,
        board.big_dog_button[3] + 20,
    )

    if is_mouse_over(board.cube_button):
        py.draw.rect(window, colors[player_turn][1], board.cube_button)
        window.blit(
            cube_button_text_surface,
            (board.cube_button[0] + 20, board.cube_button[1] + 10),
        )
    else:
        py.draw.rect(window, colors[player_turn][0], board.cube_button)
        window.blit(
            cube_button_text_surface,
            (board.cube_button[0] + 20, board.cube_button[1] + 10),
        )

    if is_mouse_over(board.small_dog_button):
        py.draw.rect(window, dark_grey, rect_behind_small_dog_button)
        Image(
            board.small_dog_button[0],
            board.small_dog_button[1],
            small_dog,
            board.small_dog_button[2],
            board.small_dog_button[3],
        ).draw(window)
    else:
        py.draw.rect(window, black, rect_behind_small_dog_button)
        Image(
            board.small_dog_button[0],
            board.small_dog_button[1],
            small_dog,
            board.small_dog_button[2],
            board.small_dog_button[3],
        ).draw(window)

    if is_mouse_over(board.big_dog_button):
        py.draw.rect(window, dark_grey, rect_behind_big_dog_button)
        Image(
            board.big_dog_button[0],
            board.big_dog_button[1],
            big_dog,
            board.big_dog_button[2],
            board.big_dog_button[3],
        ).draw(window)
    else:
        py.draw.rect(window, black, rect_behind_big_dog_button)
        Image(
            board.big_dog_button[0],
            board.big_dog_button[1],
            big_dog,
            board.big_dog_button[2],
            board.big_dog_button[3],
        ).draw(window)


# end def


def on_hover_menu(window: Surface, menu: MenuInitializer):
    """
    Function responsible for on hover drawing when menu is shown.
    :param window: Surface
    :param menu: MenuInitializer
    :return:
    """
    start_text_surface = menu.font.render("Start new game", True, white)

    if is_mouse_over(menu.start_button):
        py.draw.rect(window, dark_green, menu.start_button)
        window.blit(
            start_text_surface, (menu.start_button[0] + 10, menu.start_button[1] + 40)
        )
    else:
        py.draw.rect(window, green, menu.start_button)
        window.blit(
            start_text_surface, (menu.start_button[0] + 10, menu.start_button[1] + 40)
        )

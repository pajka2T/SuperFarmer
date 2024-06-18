import math

import pygame as py
from pygame import Surface
from pygame.font import Font

from players_data import Player
from util import Animal, black, green, white


def is_mouse_over(rect: tuple[float, float, float, float]) -> bool:
    """
    Function checking whether mouse cursor is hovering over specified rectangle.
    :param rect: tuple[float, float, float, float]
    :return:
    """
    mouse_x, mouse_y = py.mouse.get_pos()
    return (
        rect[0] < mouse_x < rect[0] + rect[2] and rect[1] < mouse_y < rect[1] + rect[3]
    )


# end def


def get_clicked_circle(
    mouse_x,
    mouse_y,
    player_turn: int,
    animal_board_coordinates: list[dict],
    cell_size: float,
) -> (int, int):
    """
    Function returning coordinates of animal's circle clicked by the player.
    :param mouse_x:
    :param mouse_y:
    :param player_turn:
    :param animal_board_coordinates:
    :param cell_size:
    :return:
    """
    a = -1
    b = -1
    for i in range(5):
        if (
            animal_board_coordinates[player_turn][Animal(i)][0][1] + cell_size / 2
            >= mouse_y
            >= animal_board_coordinates[player_turn][Animal(i)][0][1] - cell_size / 2
        ):
            a = i
    if a == -1:
        return -1, -1
    for i in range(len(animal_board_coordinates[0][Animal(a)]) - 1):
        if (
            math.sqrt(
                math.pow(
                    mouse_x - animal_board_coordinates[player_turn][Animal(a)][i][0], 2
                )
                + math.pow(
                    mouse_y - animal_board_coordinates[player_turn][Animal(a)][i][1], 2
                )
            )
            <= cell_size / 2
        ):
            b = i
    return a, b


# end def


def check_win(player: Player, win_list: list[bool]) -> bool:
    """
    Checks whether someone has won (has collected at least one animal of each type).
    :param player:
    :param win_list:
    :return:
    """
    for animal, count in player.animals.items():
        if count <= 0:
            print(animal, count)
            return False
    win_list[player.id] = True
    return True


# end def


def draw_alert(
    window: Surface,
    message: str,
    font: Font,
    info_rect: tuple[float, float, float]
) -> None:
    """
    Function draws winning information.
    :param info_rect:
    :param window:
    :param message:
    :param font:
    :return:
    """
    alert_rect = (0.3 * window.get_width(), 0.3 * window.get_height(), 500, 300)

    win_text_surface = font.render(message, True, white)
    window.blit(win_text_surface, (info_rect[0] + 20, info_rect[1] + 10))
    py.display.flip()


# end def

from copy import deepcopy

import pygame as py
from pygame import Surface

from board_initializer import BoardInitializer
from on_change_drawings import update_board
from players_data import Player
from util import Animal, Image, black, empty_dict


def wolf_attack_animation(
    clock: py.time.Clock,
    frames: int,
    window: Surface,
    player: Player,
    board: BoardInitializer,
    animals_before: dict[Animal, int],
) -> None:
    """
    Function responsible for animating wolf attack.
    :param clock: Clock defining how many frames there should be in a second.
    :param frames: Number of animation frames.
    :param window: Application window where the board will be drawn.
    :param player: Player attacked by the wolf.
    :param board: Game board - it is needed because it has a lot of information about positioning game elements.
    :param animals_before: Dictionary with player's animals before the attack and before adding new animals.
    :return: (None) Only animate.
    """
    wolf_attack = py.image.load("Images/wolfattack.png").convert_alpha()
    wolf_attack_surface = Surface((325, 325), flags=py.SRCALPHA)

    surface_size = wolf_attack_surface.get_size()
    x_val = 145 if player.id == 0 else 900
    y_val = 250

    x1 = surface_size[0] / 2
    y1 = surface_size[1] / 2

    size_change = surface_size[0] / (2 * frames)

    animals_now = deepcopy(animals_before)
    animals_now[Animal.RABBIT] = player.animals[Animal.RABBIT]
    update_board(
        window,
        player,
        animals_before,
        animals_now,
        board.animal_board_coordinates,
        board.cell_size,
    )

    for i in range(frames):
        Image(
            x1 - i * size_change,
            y1 - i * size_change,
            wolf_attack,
            size_change * 2 * i,
            size_change * 2 * i,
        ).draw(wolf_attack_surface)
        window.blit(wolf_attack_surface, (x_val, y_val))
        py.display.flip()
        clock.tick(60)

    py.draw.rect(
        window,
        black,
        (
            x_val,
            y_val,
            wolf_attack_surface.get_width(),
            wolf_attack_surface.get_height(),
        ),
    )
    board.draw_start_animals(window, player.id)
    update_board(
        window,
        player,
        empty_dict,
        player.animals,
        board.animal_board_coordinates,
        board.cell_size,
    )
    py.display.flip()


# end def


def fox_attack_animation(
    clock: py.time.Clock,
    frames: int,
    window: Surface,
    board: BoardInitializer,
    player: Player,
    animals_before: dict[Animal, int],
) -> None:
    """
    Function responsible for animating fox attack.
    :param clock: Clock defining how many frames there should be in a second.
    :param frames: Number of animation frames.
    :param window: Application window where the board will be drawn.
    :param player: Player attacked by the fox.
    :param board: Game board - it is needed because it has a lot of information about positioning game elements.
    :param animals_before: Dictionary with player's animals before the attack and before adding new animals.
    :return: (None) Only animate.
    """
    fox_attack = py.image.load("Images/foxattack.png").convert_alpha()

    x_val = 95 if player.id == 0 else 860
    start_x = x_val + 350
    y = 150
    x_change = 350 / frames

    img_width, img_height = 120, 120

    for i in range(0, frames, 3):
        board.draw_current_animals(window, player, animals_before)
        py.display.flip()
        Image(start_x - i * x_change, y, fox_attack, img_width, img_height).draw(window)

        clock.tick(30)
        py.display.flip()
    board.draw_start_animals(window, player.id)
    update_board(
        window,
        player,
        empty_dict,
        player.animals,
        board.animal_board_coordinates,
        board.cell_size,
    )
    py.display.flip()


# end def


def dog_defence_animation(
    dog: Surface,
    predator: Surface,
    clock: py.time.Clock,
    frames: int,
    window: Surface,
    player: Player,
    img_size: int,
    board: BoardInitializer,
) -> None:
    """
    Function responsible for animating dog's defence against the predator.
    :param dog: Dog image.
    :param predator: Predator image.
    :param clock: Clock defining how many frames there should be in a second.
    :param frames: Number of animation frames.
    :param window: Application window where the board will be drawn.
    :param player: Player attacked by the wolf.
    :param img_size: Size of predator's image.
    :param board: Game board - it is needed because it has a lot of information about positioning game elements.
    :return: (None) Only animate.
    """
    surface_size = dog.get_size()

    x1 = surface_size[0] / 3
    y1 = surface_size[1] / 2 - 50
    x2 = surface_size[0] - img_size - 100

    x_val = 100 if player.id == 0 else 890

    x_change = surface_size[0] / (2 * frames)

    for i in range(int(frames / 4)):
        board.draw_start_animals(window, player.id)
        update_board(
            window,
            player,
            empty_dict,
            player.animals,
            board.animal_board_coordinates,
            board.cell_size,
        )
        py.display.flip()
        Image(
            x1 - i * x_change + x_val,
            y1 - i * x_change,
            dog,
            x_change * 2 * i,
            x_change * 2 * i,
        ).draw(window)
        Image(x2 - i * x_change + x_val, 150, predator, img_size, img_size).draw(window)
        py.display.flip()
        clock.tick(60)
    board.draw_start_animals(window, player.id)
    update_board(
        window,
        player,
        empty_dict,
        player.animals,
        board.animal_board_coordinates,
        board.cell_size,
    )
    py.display.flip()


# end def

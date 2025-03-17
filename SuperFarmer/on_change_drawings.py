from typing import Dict

import pygame as py
from pygame import Surface
from pygame.time import Clock

from players_data import Player
from simple_drawings import (draw_additional_animals, draw_animal,
                             draw_empty_circles)
from util import Animal, Image, black, blue, blue2, blue3, white


def rotate_animation(
    window: Surface,
    image: Surface,
    image2: Surface,
    color: tuple[int, int, int],
    clock: Clock,
    start_fps: int,
    x: float,
    y: float,
    diff: float,
) -> None:
    """
    Function responsible for rotational animation of dices.
    :param window: Application window where the board will be drawn.
    :param image: Blue dice image.
    :param image2: Orange dice image.
    :param color: Color of marking rectangle.
    :param clock: Clock responsible for animating.
    :param start_fps: Frames per second.
    :param x: Horizontal position of blue dice.
    :param y: Vertical position of blue dice.
    :param diff: Difference between orange dice and blue dice horizontal positions.
    :return: (None) Only animates.
    """
    width = image.get_width() / 9
    height = image.get_height() / 9
    for i in range(80, -1, -1):
        rotated_image = py.transform.rotate(image, 9 * (40 - i))
        rotated_image2 = py.transform.rotate(image2, 9 * (40 - i))
        if i > 20:
            clock.tick(i * 15 * start_fps / 100)
        elif i > 10:
            clock.tick(i * 12 * start_fps / 100)
        elif i > 1:
            clock.tick(i * 10 * start_fps / 100)
        else:
            clock.tick(15)

        py.draw.rect(
            window, color, (x - width / 2, y - height / 2, width * 2 + 2, height + 1), 0
        )
        Image(
            x - rotated_image.get_width() / 18,
            y - rotated_image.get_height() / 18,
            rotated_image,
            rotated_image.get_width() / 9,
            rotated_image.get_height() / 9,
        ).draw(window)
        Image(
            x - rotated_image2.get_width() / 18 + diff,
            y - rotated_image2.get_height() / 18,
            rotated_image2,
            rotated_image2.get_width() / 9,
            rotated_image2.get_height() / 9,
        ).draw(window)
        py.display.update()


# end def


def draw_dogs(
    window: Surface,
    x1: float,
    x2: float,
    y1: float,
    smalldog: Surface,
    bigdog: Surface,
    no_small_dogs_player_1: int,
    no_big_dogs_player_1: int,
    no_small_dogs_player_2: int,
    no_big_dogs_player_2: int,
) -> None:
    """
    Function drawing actual number of dogs which every player has, when player buy or lose a dog.
    :param window: Application window where the board will be drawn.
    :param x1: Horizontal position used to define position of player's one dog images.
    :param x2: Horizontal position used to define position of player's two dog images.
    :param y1: Verical position used to define position of players dog images.
    :param smalldog: Image of small dog.
    :param bigdog: Image of big dog.
    :param no_small_dogs_player_1: Number of small dogs which player one has.
    :param no_big_dogs_player_1: Number of big dogs which player one has.
    :param no_small_dogs_player_2: Number of small dogs which player two has.
    :param no_big_dogs_player_2: Number of big dogs which player two has.
    :return: (None) Only animates dices.
    """
    font = py.font.Font("Fonts/BRLNSDB.ttf", 50)
    py.draw.rect(window, black, (x1, y1, 100, 120))
    py.draw.rect(window, black, (x2, y1, 100, 120))
    if no_small_dogs_player_1 > 0:
        textsurface = font.render(f"{no_small_dogs_player_1}", True, white)
        window.blit(textsurface, (x1 + 10, y1 + 10))
        Image(x1 + 35, y1 + 10, smalldog, 50, 50).draw(window)
    if no_small_dogs_player_2 > 0:
        textsurface = font.render(f"{no_small_dogs_player_2}", True, white)
        window.blit(textsurface, (x2 + 10, y1 + 10))
        Image(x2 + 35, y1 + 10, smalldog, 50, 50).draw(window)
    if no_big_dogs_player_1 > 0:
        textsurface = font.render(f"{no_big_dogs_player_1}", True, white)
        window.blit(textsurface, (x1 + 10, y1 + 70))
        Image(x1 + 35, y1 + 70, bigdog, 50, 50).draw(window)
    if no_big_dogs_player_2 > 0:
        textsurface = font.render(f"{no_big_dogs_player_2}", True, white)
        window.blit(textsurface, (x2 + 10, y1 + 70))
        Image(x2 + 35, y1 + 70, bigdog, 50, 50).draw(window)


# end def


def update_board(
    window: Surface,
    player: Player,
    animals_before: Dict[Animal, int],
    animals_now: dict[Animal:int],
    animal_board_coordinates: list[dict],
    cell_size: float,
) -> None:
    """
    Function which updates the board when there is a change in player's animals dictionary.
    :param window: Application window where the board will be drawn.
    :param player: Player whose animals will be drawn.
    :param animals_before: Animals which player had before the change
    :param animals_now: Animals which player has after the change
    :param animal_board_coordinates: Coordinates of animals circles.
    :param cell_size: Size of animals circle.
    :return: (None) Only draws.
    """
    player_no = player.id
    for animal in animals_now:
        no_animals_before = animals_before[animal]
        no_animals_now = animals_now[animal]

        black_marking_square = (
            animal_board_coordinates[player_no][animal][5 - animal.value - 1][0]
            + cell_size / 2,
            animal_board_coordinates[player_no][animal][5 - animal.value - 1][1]
            - cell_size / 2,
            cell_size + 15,
            cell_size + 5,
        )

        number_destination = (
            black_marking_square[0] + cell_size * 3 / 5,
            black_marking_square[1] + cell_size * 3 / 4,
        )

        if no_animals_before < no_animals_now:
            if no_animals_before % 2 == 1 and no_animals_before < 10 - animal.value * 2:
                draw_animal(
                    window,
                    blue,
                    animal_board_coordinates[player_no][animal][
                        (no_animals_before - 1) // 2
                    ][0],
                    animal_board_coordinates[player_no][animal][
                        (no_animals_before - 1) // 2
                    ][1],
                    cell_size,
                    10,
                    animal.value,
                    255,
                )
                no_animals_before += 1
            for i in range(
                no_animals_before, min(no_animals_now - 1, 10 - animal.value * 2), 2
            ):
                draw_animal(
                    window,
                    blue,
                    animal_board_coordinates[player_no][animal][i // 2][0],
                    animal_board_coordinates[player_no][animal][i // 2][1],
                    cell_size,
                    10,
                    animal.value,
                    255,
                )
            if no_animals_now % 2 == 1 and no_animals_now < 10 - animal.value * 2:
                draw_animal(
                    window,
                    blue,
                    animal_board_coordinates[player_no][animal][no_animals_now // 2][0],
                    animal_board_coordinates[player_no][animal][no_animals_now // 2][1],
                    cell_size,
                    10,
                    animal,
                    255,
                )
            if no_animals_now > 10 - animal.value * 2:
                py.draw.rect(window, black, black_marking_square)
                draw_additional_animals(
                    window,
                    blue,
                    blue2,
                    blue3,
                    animal_board_coordinates[player_no][animal][
                        len(animal_board_coordinates[player_no][animal]) - 1
                    ][2],
                    animal_board_coordinates[player_no][animal][
                        len(animal_board_coordinates[player_no][animal]) - 1
                    ][3],
                    animal_board_coordinates[player_no][animal][
                        len(animal_board_coordinates[player_no][animal]) - 1
                    ][1],
                    animal,
                    animal_board_coordinates[player_no][animal][
                        len(animal_board_coordinates[player_no][animal]) - 1
                    ][4],
                    cell_size,
                )
                font2 = py.font.Font("Fonts/BRLNSDB.ttf", 32)
                text = "+" + str(no_animals_now - (10 - animal.value * 2))
                text_surface = font2.render(text, True, white)
                window.blit(text_surface, number_destination)

        elif no_animals_now < no_animals_before:
            for i in range(
                max(no_animals_now + 1, 0),
                min(no_animals_before + 1, 10 - animal.value * 2),
                2,
            ):
                print(no_animals_now, no_animals_before, i, i // 2)
                draw_empty_circles(
                    window,
                    blue,
                    black,
                    animal_board_coordinates[player_no][animal][i // 2][0],
                    animal_board_coordinates[player_no][animal][i // 2][1],
                    cell_size,
                )
            if no_animals_now == 0:
                draw_animal(
                    window,
                    blue,
                    animal_board_coordinates[player_no][animal][0][0],
                    animal_board_coordinates[player_no][animal][0][1],
                    cell_size,
                    10,
                    animal,
                    128,
                )
            elif no_animals_now % 2 == 1 and no_animals_now < 10 - animal.value * 2:
                draw_animal(
                    window,
                    blue,
                    animal_board_coordinates[player_no][animal][no_animals_now // 2][0],
                    animal_board_coordinates[player_no][animal][no_animals_now // 2][1],
                    cell_size,
                    10,
                    animal,
                    255,
                )
            elif no_animals_now % 2 == 0 and no_animals_now < 10 - animal.value * 2:
                draw_animal(
                    window,
                    blue,
                    animal_board_coordinates[player_no][animal][
                        no_animals_now // 2 - 1
                    ][0],
                    animal_board_coordinates[player_no][animal][
                        no_animals_now // 2 - 1
                    ][1],
                    cell_size,
                    10,
                    animal.value,
                    255,
                )
            py.draw.rect(window, black, black_marking_square)
            if no_animals_now > 10 - animal.value * 2:
                draw_additional_animals(
                    window,
                    blue,
                    blue2,
                    blue3,
                    animal_board_coordinates[player_no][animal][
                        len(animal_board_coordinates[player_no][animal]) - 1
                    ][2],
                    animal_board_coordinates[player_no][animal][
                        len(animal_board_coordinates[player_no][animal]) - 1
                    ][3],
                    animal_board_coordinates[player_no][animal][
                        len(animal_board_coordinates[player_no][animal]) - 1
                    ][1],
                    animal,
                    animal_board_coordinates[player_no][animal][
                        len(animal_board_coordinates[player_no][animal]) - 1
                    ][4],
                    cell_size,
                )
                font2 = py.font.Font("Fonts/BRLNSDB.ttf", 32)
                text = "+" + str(no_animals_now - (10 - animal.value * 2))
                text_surface = font2.render(text, True, white)
                window.blit(text_surface, number_destination)
    print(animals_now)
    py.display.flip()


# end def


def mark_animals_for_exchange(
    window: Surface,
    player: Player,
    animal: Animal,
    first_animal: int,
    last_animal: int,
    animal_board_coordinates: list[dict],
    cell_size: float,
    color: tuple[int, int, int] = blue3,
) -> None:
    """
    Function marking animals which are going to be exchanged.
    :param window: Application window where the board will be drawn.
    :param player: Player whose animals will be marked.
    :param animal: Type of animal to be marked.
    :param first_animal: Number of first animal to be unmerked.
    :param last_animal: Number of first animal to be unmarked.
    :param animal_board_coordinates: Coordinates of animals circles.
    :param cell_size: Size of animals circle.
    :param color: Color of marking the circle.
    :return: (None) Only marks animals circles.
    """
    player_no = player.id
    print(animal, player.animals)
    for i in range(
        min(first_animal, last_animal), max(first_animal + 1, last_animal + 1)
    ):
        print(player_no, animal, i)
        if i * 2 + 1 == player.animals[animal]:
            animal_to_draw = animal
        else:
            animal_to_draw = animal.value
        draw_animal(
            window,
            color,
            animal_board_coordinates[player_no][animal][i][0],
            animal_board_coordinates[player_no][animal][i][1],
            cell_size,
            10,
            animal_to_draw,
            255,
        )
    py.display.flip()


# end def


def unmark_animals_for_exchange(
    window: Surface,
    player: Player,
    animal: Animal,
    first_animal: int,
    no_exchanged_animals: int,
    animal_board_coordinates: list[dict],
    cell_size: float,
):
    """
    Function unmarking animals which were supposed to be exchanged, but the exchanged was stopped.
    :param window: Application window where the board will be drawn.
    :param player: Player whose animals will be unmarked.
    :param animal: Type of animal to be unmarked.
    :param first_animal: Number of first animal to be unmarked.
    :param no_exchanged_animals: Number of animals to be exchanged.
    :param animal_board_coordinates: Coordinates of animals circles.
    :param cell_size: Size of animals circle.
    :return: (None) Only unmarks animals circles.
    """
    mark_animals_for_exchange(
        window,
        player,
        animal,
        first_animal,
        no_exchanged_animals,
        animal_board_coordinates,
        cell_size,
        blue,
    )


# end def

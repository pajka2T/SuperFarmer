from typing import Dict

import pygame as py
from pygame import Surface
from pygame.time import Clock

from players_data import Player
from simple_drawings import (draw_additional_animals, draw_animal,
                             draw_empty_circles)
from util import Animal, Image

BLUE = (52, 229, 235)
BLUE2 = (93, 190, 194)
BLUE3 = (38, 125, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def rotate_animation(
    window: Surface,
    image: Surface,
    image2: Surface,
    color: tuple[int, int, int],
    clock: Clock,
    x: float,
    y: float,
    diff: float,
) -> None:
    width = image.get_width() / 9
    height = image.get_height() / 9
    for i in range(80, -1, -1):
        rotated_image = py.transform.rotate(image, 9 * (40 - i))
        rotated_image2 = py.transform.rotate(image2, 9 * (40 - i))
        if i > 20:
            clock.tick(i * 15)
        elif i > 10:
            clock.tick(i * 12)
        elif i > 1:
            clock.tick(i * 10)
        else:
            clock.tick(15)

        # a = abs(width*math.sin(4.5*(10-i)))
        # b = abs(width*math.cos(4.5*(10-i)))
        # x2 = x-(a+b-width)/2
        # y2 = y-(a+b-height)/2
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


def draw_dogs(
    window: Surface,
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    smalldog: Surface,
    bigdog: Surface,
    no_small_dogs_player_1: int,
    no_big_dogs_player_1: int,
    no_small_dogs_player_2: int,
    no_big_dogs_player_2: int,
) -> None:
    font = py.font.Font("Fonts/BRLNSDB.ttf", 50)
    py.draw.rect(window, BLACK, (x1, y1, 100, 120))
    py.draw.rect(window, BLACK, (x2, y2, 100, 120))
    if no_small_dogs_player_1 > 0:
        textsurface = font.render(f"{no_small_dogs_player_1}", True, WHITE)
        window.blit(textsurface, (x1 + 10, y1 + 10))
        Image(x1 + 35, y1 + 10, smalldog, 50, 50).draw(window)
    if no_small_dogs_player_2 > 0:
        textsurface = font.render(f"{no_small_dogs_player_2}", True, WHITE)
        window.blit(textsurface, (x2 + 10, y2 + 10))
        Image(x2 + 35, y2 + 10, smalldog, 50, 50).draw(window)
    if no_big_dogs_player_1 > 0:
        textsurface = font.render(f"{no_big_dogs_player_1}", True, WHITE)
        window.blit(textsurface, (x1 + 10, y1 + 70))
        Image(x1 + 35, y1 + 70, bigdog, 50, 50).draw(window)
    if no_big_dogs_player_2 > 0:
        textsurface = font.render(f"{no_big_dogs_player_2}", True, WHITE)
        window.blit(textsurface, (x2 + 10, y2 + 70))
        Image(x2 + 35, y2 + 70, bigdog, 50, 50).draw(window)


def update_board(
    window: Surface,
    player: Player,
    animals_before: Dict[Animal, int],
    animals_now: dict[Animal:int],
    animal_board_coordinates: list[dict],
    cell_size: float,
) -> None:
    player_no = player.id
    for animal in animals_now:
        no_animals_before = animals_before[animal]
        no_animals_now = animals_now[animal]
        # Adding new animals
        if no_animals_before < no_animals_now:
            print("Drawing new animals which values are ", animal.value)
            # There are places for animals
            # for i in range(no_animals_before, min(no_animals_now, 5-animal.value)):
            #     draw_animal(window, BLUE, animal_board_coordinates[player_no][animal.value][i][0],
            #                 animal_board_coordinates[player_no][animal.value][i][1], cell_size, 10, animal, 255)
            # There are places for animals and we'll have new pair
            if no_animals_before % 2 == 1 and no_animals_before < 10 - animal.value * 2:
                draw_animal(
                    window,
                    BLUE,
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
                    BLUE,
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
                    BLUE,
                    animal_board_coordinates[player_no][animal][no_animals_now // 2][0],
                    animal_board_coordinates[player_no][animal][no_animals_now // 2][1],
                    cell_size,
                    10,
                    animal,
                    255,
                )
            # Drawing additional animals
            if no_animals_now > 10 - animal.value * 2:
                py.draw.rect(
                    window,
                    BLACK,
                    (
                        animal_board_coordinates[player_no][animal][
                            len(animal_board_coordinates[player_no][animal]) - 1
                        ][0],
                        animal_board_coordinates[player_no][animal][
                            len(animal_board_coordinates[player_no][animal]) - 1
                        ][1],
                        cell_size,
                        cell_size,
                    ),
                )
                draw_additional_animals(
                    window,
                    BLUE,
                    BLUE2,
                    BLUE3,
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
                text_surface = font2.render(text, True, WHITE)
                window.blit(
                    text_surface,
                    (
                        animal_board_coordinates[player_no][animal][
                            len(animal_board_coordinates[player_no][animal]) - 1
                        ][0]
                        + cell_size / 2,
                        animal_board_coordinates[player_no][animal][
                            len(animal_board_coordinates[player_no][animal]) - 1
                        ][1]
                        + cell_size / 2,
                    ),
                )
        # Removing some animals
        elif no_animals_now < no_animals_before:
            print("Removing animals which values are ", animal.value)
            for i in range(
                max(no_animals_now + 1, 0),
                min(no_animals_before + 1, 10 - animal.value * 2),
                2,
            ):
                print(no_animals_now, no_animals_before, i, i // 2)
                draw_empty_circles(
                    window,
                    BLUE,
                    BLACK,
                    animal_board_coordinates[player_no][animal][i // 2][0],
                    animal_board_coordinates[player_no][animal][i // 2][1],
                    cell_size,
                )
            # Ifs for easier problem-solving
            if no_animals_now == 0:
                print("TU: 0")
                draw_animal(
                    window,
                    BLUE,
                    animal_board_coordinates[player_no][animal][0][0],
                    animal_board_coordinates[player_no][animal][0][1],
                    cell_size,
                    10,
                    animal,
                    128,
                )
            elif no_animals_now == 1:
                print("TU: 1")
                draw_animal(
                    window,
                    BLUE,
                    animal_board_coordinates[player_no][animal][0][0],
                    animal_board_coordinates[player_no][animal][0][1],
                    cell_size,
                    10,
                    animal,
                    255,
                )
            elif no_animals_now == 2:
                print("TU: 2")
                draw_animal(
                    window,
                    BLUE,
                    animal_board_coordinates[player_no][animal][0][0],
                    animal_board_coordinates[player_no][animal][0][1],
                    cell_size,
                    10,
                    animal.value,
                    255,
                )
            if no_animals_now <= 10 - animal.value * 2 < no_animals_before:
                print("AAAAAAAA")
                # Removing additional animals
                BLACK_MARKING_SQUARE = (
                    animal_board_coordinates[player_no][animal][5 - animal.value - 1][0]
                    + cell_size / 2,
                    animal_board_coordinates[player_no][animal][5 - animal.value - 1][1]
                    - cell_size / 2,
                    cell_size + 10,
                    cell_size,
                )
                py.draw.rect(window, BLACK, BLACK_MARKING_SQUARE)
            elif no_animals_now > 10 - animal.value * 2:
                print("TUUUUUUU")
                # Changing value of additional animals printed number
                font2 = py.font.Font("Fonts/BRLNSDB.ttf", 32)
                text = "+" + str(no_animals_now - (10 - animal.value * 2))
                text_surface = font2.render(text, True, WHITE)
                window.blit(
                    text_surface,
                    (
                        animal_board_coordinates[player_no][animal][
                            len(animal_board_coordinates[player_no][animal]) - 1
                        ][0]
                        + cell_size / 2,
                        animal_board_coordinates[player_no][animal][
                            len(animal_board_coordinates[player_no][animal]) - 1
                        ][1]
                        + cell_size / 2,
                    ),
                )
    print(animals_now)
    py.display.flip()


def mark_animals_for_exchange(
    window: Surface,
    player: Player,
    animal: Animal,
    first_animal: int,
    last_animal: int,
    animal_board_coordinates: list[dict],
    cell_size: float,
    color: tuple[int, int, int] = BLUE3,
) -> None:
    player_no = player.id
    print(animal, player.animals)
    for i in range(
        min(first_animal, last_animal), max(first_animal + 1, last_animal + 1)
    ):
        print(player_no, animal, i)
        animal_to_draw = None
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


def unmark_animals_for_exchange(
    window: Surface,
    player: Player,
    animal: Animal,
    first_animal: int,
    no_exchanged_animals: int,
    animal_board_coordinates: list[dict],
    cell_size: float,
):
    mark_animals_for_exchange(
        window,
        player,
        animal,
        first_animal,
        no_exchanged_animals,
        animal_board_coordinates,
        cell_size,
        BLUE,
    )

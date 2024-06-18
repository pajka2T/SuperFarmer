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
    x2: float,
    y1: float,
    smalldog: Surface,
    bigdog: Surface,
    no_small_dogs_player_1: int,
    no_big_dogs_player_1: int,
    no_small_dogs_player_2: int,
    no_big_dogs_player_2: int,
) -> None:
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
        blue,
    )

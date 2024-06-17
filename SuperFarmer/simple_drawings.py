import pygame as py
from pygame import Surface

from util import Animal, Image, convert_animal_to_img


def draw_animal(
    window: Surface,
    color1: tuple[int, int, int],
    center_x: float,
    center_y: float,
    cell_size: float,
    size: float,
    animal: Animal,
    alpha: int,
) -> None:
    py.draw.circle(window, color1, (center_x, center_y), cell_size / 2)
    img = convert_animal_to_img(animal)
    img.set_alpha(alpha)
    Image(
        center_x - cell_size / 2 + cell_size / size,
        center_y - cell_size / 2 + cell_size / size,
        img,
        (1 - 2 / size) * cell_size,
        (1 - 2 / size) * cell_size,
    ).draw(window)


def draw_empty_circles(
    window: Surface,
    color1: tuple[int, int, int],
    color2: tuple[int, int, int],
    x: float,
    y: float,
    cell_size: float,
) -> None:
    py.draw.circle(window, color1, (x, y), cell_size / 2)
    py.draw.circle(window, color2, (x, y), cell_size / 2.2)


def draw_additional_animals(
    window: Surface,
    color1: tuple[int, int, int],
    color2: tuple[int, int, int],
    color3: tuple[int, int, int],
    x: float,
    x2: float,
    y: float,
    animal: Animal,
    size: float,
    cell_size: float,
) -> None:
    py.draw.circle(
        window, color3, (x + cell_size / 1.8, y + cell_size / 1.8), cell_size / 2.4
    )
    py.draw.circle(
        window,
        color2,
        (x2 + cell_size + cell_size / 2, y + cell_size / 1.7),
        cell_size / 2.4,
    )
    py.draw.circle(
        window,
        color1,
        (x2 + cell_size + cell_size / 1.8, y + cell_size / 2.4),
        cell_size / 2.4,
    )
    Image(
        x2 + cell_size + cell_size / 1.8 + cell_size / 12 - cell_size / 2.4,
        y + cell_size / 2.4 + cell_size / 12 - cell_size / 2.4,
        convert_animal_to_img(animal),
        cell_size * size,
        cell_size * size,
    ).draw(window)

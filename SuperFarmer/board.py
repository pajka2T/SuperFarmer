import math

import pygame as py

from util import Animal, Image, convert_animal_to_img

BLUE = (52, 229, 235)
BLUE2 = (93, 190, 194)
BLUE3 = (38, 125, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def rotate_animation(window, image, image2, color, clock, x, y, diff):
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


def draw_additional_animals(
    window, color1, color2, color3, x, x2, y, animal, size, CELL_SIZE
):
    py.draw.circle(
        window, color3, (x + CELL_SIZE / 1.8, y + CELL_SIZE / 1.8), CELL_SIZE / 2.4
    )
    py.draw.circle(
        window,
        color2,
        (x2 + CELL_SIZE + CELL_SIZE / 2, y + CELL_SIZE / 1.7),
        CELL_SIZE / 2.4,
    )
    py.draw.circle(
        window,
        color1,
        (x2 + CELL_SIZE + CELL_SIZE / 1.8, y + CELL_SIZE / 2.4),
        CELL_SIZE / 2.4,
    )
    # print(y, " ", y+(CELL_SIZE/1.7)*2)
    Image(
        x2 + CELL_SIZE + CELL_SIZE / 1.8 + CELL_SIZE / 12 - CELL_SIZE / 2.4,
        y + CELL_SIZE / 2.4 + CELL_SIZE / 12 - CELL_SIZE / 2.4,
        convert_animal_to_img(animal),
        CELL_SIZE * size,
        CELL_SIZE * size,
    ).draw(window)

    # print(animalBoardCoordinates[player][animalnumber][5-animalnumber])


def draw_empty_circles(window, color1, color2, x, y, CELL_SIZE):
    py.draw.circle(window, color1, (x, y), CELL_SIZE / 2)
    py.draw.circle(window, color2, (x, y), CELL_SIZE / 2.2)


def draw_animal(window, color1, center_x, center_y, CELL_SIZE, size, animal, alpha):
    py.draw.circle(window, color1, (center_x, center_y), CELL_SIZE / 2)
    img = convert_animal_to_img(animal)
    img.set_alpha(alpha)
    Image(
        center_x - CELL_SIZE / 2 + CELL_SIZE / size,
        center_y - CELL_SIZE / 2 + CELL_SIZE / size,
        img,
        (1 - 2 / size) * CELL_SIZE,
        (1 - 2 / size) * CELL_SIZE,
    ).draw(window)


def draw_dogs(window, x1, y1, x2, y2, smalldog, bigdog, sd1, bd1, sd2, bd2):
    font = py.font.Font("Fonts/BRLNSDB.ttf", 50)
    py.draw.rect(window, BLACK, (x1, y1, 100, 120))
    py.draw.rect(window, BLACK, (x2, y2, 100, 120))
    if sd1 > 0:
        textsurface = font.render(f"{sd1}", True, WHITE)
        window.blit(textsurface, (x1 + 10, y1 + 10))
        Image(x1 + 35, y1 + 10, smalldog, 50, 50).draw(window)
    if sd2 > 0:
        textsurface = font.render(f"{sd2}", True, WHITE)
        window.blit(textsurface, (x2 + 10, y2 + 10))
        Image(x2 + 35, y2 + 10, smalldog, 50, 50).draw(window)
    if bd1 > 0:
        textsurface = font.render(f"{bd1}", True, WHITE)
        window.blit(textsurface, (x1 + 10, y1 + 70))
        Image(x1 + 35, y1 + 70, bigdog, 50, 50).draw(window)
    if bd2 > 0:
        textsurface = font.render(f"{bd2}", True, WHITE)
        window.blit(textsurface, (x2 + 10, y2 + 70))
        Image(x2 + 35, y2 + 70, bigdog, 50, 50).draw(window)


players = 2
animalBoardCoordinates = [[[] for j in range(5)] for k in range(players)]


def create_board(WINDOW):
    # players = int(input("Gracze"))

    py.init()
    # WINDOW = py.display.set_mode((0, 0), py.FULLSCREEN)
    # WINDOW = py.display.set_mode((1500, 800))
    # py.display.set_caption("SuperFarmer")
    logo2 = py.image.load("Images/Logo2.png").convert_alpha()
    # py.display.set_icon(logo2)

    screeninfo = py.display.Info()
    SCREENWIDTH = screeninfo.current_w
    SCREENHEIGHT = screeninfo.current_h
    print(SCREENWIDTH, SCREENHEIGHT)

    CELL_SIZE = math.floor(SCREENHEIGHT / 8)

    # BOARD_MARGIN_TOP = SCREENHEIGHT/2 - CELL_SIZE*2
    BOARD_MARGIN_TOP = SCREENHEIGHT / 2 - CELL_SIZE * 2.5
    BUNNY_MARGIN_SIDE = SCREENWIDTH / 2 - CELL_SIZE * 7
    BETWEEN_CELLS = 7
    # BUNNY_MARGIN_SIDE_TWO = BUNNY_MARGIN_SIDE + CELL_SIZE*6 + BETWEEN_CELLS*8
    BUNNY_MARGIN_SIDE_TWO = (
        SCREENWIDTH - BUNNY_MARGIN_SIDE - CELL_SIZE * 6 - BETWEEN_CELLS * 6
    )

    cell_size_and_space_between = BETWEEN_CELLS + CELL_SIZE
    half_cell_size_and_space_between = BETWEEN_CELLS + CELL_SIZE / 2

    bunny = convert_animal_to_img(Animal.RABBIT)
    py.display.set_icon(bunny)

    # barrier = py.image.load('Images/barrier.png').convert_alpha()
    fence = py.image.load("Images/fence2.png").convert_alpha()
    bluefarmer = py.image.load("Images/bluefarmer.png").convert_alpha()
    bluefarmer_width, bluefarmer_height = bluefarmer.get_size()
    # print(bluefarmer_width, bluefarmer_height)
    redfarmer = py.image.load("Images/redfarmer.png").convert_alpha()
    redfarmer_width, redfarmer_height = redfarmer.get_size()
    tablica1 = py.image.load("Images/tablica1.png")
    tablica2 = py.image.load("Images/tablica2.png")
    naglowek = py.image.load("Images/Naglowek.png")

    buda1 = py.image.load("Images/doghouse.png")
    buda2 = py.image.load("Images/dog-house.png")

    Image(redfarmer_width / 3 + 150, 618, tablica1, 250, 172).draw(WINDOW)
    Image(redfarmer_width / 3 + 140 + 272, 618, tablica2, 272, 190).draw(WINDOW)
    Image(redfarmer_width / 3 + 270, 540, naglowek, 255, 108).draw(WINDOW)

    Image(redfarmer_width / 3 - 90, 680, buda1, 120, 120).draw(WINDOW)
    Image(SCREENWIDTH - bluefarmer_width / 3 - 120, 690, buda2, 120, 120).draw(WINDOW)

    Image(
        SCREENWIDTH - bluefarmer_width / 4,
        SCREENHEIGHT - bluefarmer_height / 3,
        bluefarmer,
        bluefarmer_width / 3,
        bluefarmer_height / 3,
    ).draw(WINDOW)
    Image(
        -redfarmer_width / 10,
        SCREENHEIGHT - redfarmer_height / 3,
        redfarmer,
        redfarmer_width / 3,
        redfarmer_height / 3,
    ).draw(WINDOW)

    player_board_width = CELL_SIZE * 5 + BETWEEN_CELLS * 4

    # Player's one board
    for i in range(8):
        Image(
            BUNNY_MARGIN_SIDE + player_board_width / 8 * i,
            BOARD_MARGIN_TOP - player_board_width / 12,
            fence,
            player_board_width / 8,
            player_board_width / 12,
        ).draw(WINDOW)

    py.draw.polygon(
        WINDOW,
        (255, 255, 255),
        [
            (BUNNY_MARGIN_SIDE, BOARD_MARGIN_TOP),
            (BUNNY_MARGIN_SIDE + player_board_width, BOARD_MARGIN_TOP),
            (
                BUNNY_MARGIN_SIDE + player_board_width / 2,
                BOARD_MARGIN_TOP + CELL_SIZE * 5,
            ),
        ],
        0,
    )

    for i in range(5):

        # ImageGrid(BUNNY_MARGIN_SIDE+cell_size_and_space_between*i, BOARD_MARGIN_TOP, bunny, CELL_SIZE, CELL_SIZE).draw(WINDOW)
        # Rabbits
        if i == 0:
            draw_animal(
                WINDOW,
                BLUE,
                BUNNY_MARGIN_SIDE
                + CELL_SIZE / 2 * (i + 1)
                + half_cell_size_and_space_between * i,
                BOARD_MARGIN_TOP + CELL_SIZE / 2,
                CELL_SIZE,
                10,
                Animal.RABBIT,
                128,
            )
        if i > 0:
            draw_empty_circles(
                WINDOW,
                BLUE,
                BLACK,
                BUNNY_MARGIN_SIDE
                + CELL_SIZE / 2 * (i + 1)
                + half_cell_size_and_space_between * i,
                BOARD_MARGIN_TOP + CELL_SIZE / 2,
                CELL_SIZE,
            )
        animalBoardCoordinates[0][0].append(
            (
                BUNNY_MARGIN_SIDE
                + CELL_SIZE / 2 * (i + 1)
                + half_cell_size_and_space_between * i,
                BOARD_MARGIN_TOP + CELL_SIZE / 2,
            )
        )
        # Sheeps
        if i < 4:
            if i == 0:
                draw_animal(
                    WINDOW,
                    BLUE,
                    BUNNY_MARGIN_SIDE + CELL_SIZE + cell_size_and_space_between * i,
                    BOARD_MARGIN_TOP + CELL_SIZE * 1.5 + BETWEEN_CELLS / 2,
                    CELL_SIZE,
                    10,
                    Animal.SHEEP,
                    128,
                )
            if i > 0:
                draw_empty_circles(
                    WINDOW,
                    BLUE,
                    BLACK,
                    BUNNY_MARGIN_SIDE + CELL_SIZE + cell_size_and_space_between * i,
                    BOARD_MARGIN_TOP + CELL_SIZE * 1.5 + BETWEEN_CELLS / 2,
                    CELL_SIZE,
                )
            animalBoardCoordinates[0][1].append(
                (
                    BUNNY_MARGIN_SIDE + CELL_SIZE + cell_size_and_space_between * i,
                    BOARD_MARGIN_TOP + CELL_SIZE + CELL_SIZE / 2 + BETWEEN_CELLS / 2,
                )
            )
        # Pigs
        if i < 3:
            if i == 0:
                draw_animal(
                    WINDOW,
                    BLUE,
                    BUNNY_MARGIN_SIDE
                    + cell_size_and_space_between
                    + CELL_SIZE / 2 * (i + 1)
                    + half_cell_size_and_space_between * i,
                    BOARD_MARGIN_TOP + CELL_SIZE * 2.5 + BETWEEN_CELLS,
                    CELL_SIZE,
                    10,
                    Animal.PIG,
                    128,
                )
            if i > 0:
                draw_empty_circles(
                    WINDOW,
                    BLUE,
                    BLACK,
                    BUNNY_MARGIN_SIDE
                    + cell_size_and_space_between
                    + CELL_SIZE / 2 * (i + 1)
                    + half_cell_size_and_space_between * i,
                    BOARD_MARGIN_TOP + CELL_SIZE * 2.5 + BETWEEN_CELLS,
                    CELL_SIZE,
                )
            animalBoardCoordinates[0][2].append(
                (
                    BUNNY_MARGIN_SIDE
                    + cell_size_and_space_between
                    + CELL_SIZE / 2 * (i + 1)
                    + half_cell_size_and_space_between * i,
                    BOARD_MARGIN_TOP + CELL_SIZE * 2.5 + BETWEEN_CELLS,
                )
            )
        # Cows
        if i < 2:
            if i == 0:
                draw_animal(
                    WINDOW,
                    BLUE,
                    BUNNY_MARGIN_SIDE
                    + CELL_SIZE * 2
                    + BETWEEN_CELLS
                    + cell_size_and_space_between * i,
                    BOARD_MARGIN_TOP + CELL_SIZE * 3.5 + BETWEEN_CELLS * 1.5,
                    CELL_SIZE,
                    10,
                    Animal.COW,
                    128,
                )
            if i > 0:
                draw_empty_circles(
                    WINDOW,
                    BLUE,
                    BLACK,
                    BUNNY_MARGIN_SIDE
                    + CELL_SIZE * 2
                    + BETWEEN_CELLS
                    + cell_size_and_space_between * i,
                    BOARD_MARGIN_TOP + CELL_SIZE * 3.5 + BETWEEN_CELLS * 1.5,
                    CELL_SIZE,
                )
            animalBoardCoordinates[0][3].append(
                (
                    BUNNY_MARGIN_SIDE
                    + CELL_SIZE * 2
                    + BETWEEN_CELLS
                    + cell_size_and_space_between * i,
                    BOARD_MARGIN_TOP + CELL_SIZE * 3.5 + BETWEEN_CELLS * 1.5,
                )
            )
    draw_animal(
        WINDOW,
        BLUE,
        BUNNY_MARGIN_SIDE + cell_size_and_space_between * 2 + CELL_SIZE / 2,
        BOARD_MARGIN_TOP + CELL_SIZE * 4.5 + BETWEEN_CELLS * 2,
        CELL_SIZE,
        10,
        Animal.HORSE,
        128,
    )

    animalBoardCoordinates[0][4].append(
        (
            BUNNY_MARGIN_SIDE + cell_size_and_space_between * 2 + CELL_SIZE / 2,
            BOARD_MARGIN_TOP + CELL_SIZE * 4.5 + BETWEEN_CELLS * 2,
        )
    )

    # Additional animals
    # animalBoardCoordinates[player][animal][len] = (x lewy narożnik, y margines od góry, x1 do drawcircles, x2 do drawcircles)
    # żeby mieć x2 do drawcircles trzeba od x odjąć CELL_SIZE + CELL_SIZE / 2 - CELL_SIZE / 2.4

    animalBoardCoordinates[0][0].append(
        (
            BUNNY_MARGIN_SIDE
            + cell_size_and_space_between * 4
            + CELL_SIZE
            + CELL_SIZE / 2
            - CELL_SIZE / 2.4,
            BOARD_MARGIN_TOP,
            BUNNY_MARGIN_SIDE + cell_size_and_space_between * 5,
            BUNNY_MARGIN_SIDE + cell_size_and_space_between * 4,
            2 / 3,
        )
    )

    animalBoardCoordinates[0][1].append(
        (
            BUNNY_MARGIN_SIDE
            + cell_size_and_space_between * 3
            + CELL_SIZE / 2
            + CELL_SIZE
            + CELL_SIZE / 2
            - CELL_SIZE / 2.4,
            BOARD_MARGIN_TOP + CELL_SIZE + BETWEEN_CELLS / 2,
            BUNNY_MARGIN_SIDE + cell_size_and_space_between * 4 + CELL_SIZE / 2,
            BUNNY_MARGIN_SIDE + cell_size_and_space_between * 3 + CELL_SIZE / 2,
            2 / 3,
        )
    )

    animalBoardCoordinates[0][2].append(
        (
            BUNNY_MARGIN_SIDE
            + cell_size_and_space_between * 3
            + CELL_SIZE
            + CELL_SIZE / 2
            - CELL_SIZE / 2.4,
            BOARD_MARGIN_TOP + CELL_SIZE * 2 + BETWEEN_CELLS,
            BUNNY_MARGIN_SIDE + cell_size_and_space_between * 4,
            BUNNY_MARGIN_SIDE + cell_size_and_space_between * 3,
            7 / 12,
        )
    )

    animalBoardCoordinates[0][3].append(
        (
            BUNNY_MARGIN_SIDE
            + cell_size_and_space_between * 2
            + CELL_SIZE / 2
            + CELL_SIZE
            + CELL_SIZE / 2
            - CELL_SIZE / 2.4,
            BOARD_MARGIN_TOP + CELL_SIZE * 3 + BETWEEN_CELLS * 1.5,
            BUNNY_MARGIN_SIDE + cell_size_and_space_between * 3 + CELL_SIZE / 2,
            BUNNY_MARGIN_SIDE + cell_size_and_space_between * 2 + CELL_SIZE / 2,
            2 / 3,
        )
    )

    animalBoardCoordinates[0][4].append(
        (
            BUNNY_MARGIN_SIDE
            + cell_size_and_space_between * 2
            + CELL_SIZE
            + CELL_SIZE / 2
            - CELL_SIZE / 2.4,
            BOARD_MARGIN_TOP + CELL_SIZE * 4 + BETWEEN_CELLS * 2,
            BUNNY_MARGIN_SIDE + cell_size_and_space_between * 3,
            BUNNY_MARGIN_SIDE + cell_size_and_space_between * 2,
            7 / 12,
        )
    )

    # Player two
    BUNNY_MARGIN_SIDE = BUNNY_MARGIN_SIDE_TWO

    for i in range(5):
        # Rabbits
        if i == 0:
            draw_animal(
                WINDOW,
                BLUE,
                BUNNY_MARGIN_SIDE
                + CELL_SIZE / 2 * (i + 1)
                + half_cell_size_and_space_between * i,
                BOARD_MARGIN_TOP + CELL_SIZE / 2,
                CELL_SIZE,
                10,
                Animal.RABBIT,
                128,
            )
        if i > 0:
            draw_empty_circles(
                WINDOW,
                BLUE,
                BLACK,
                BUNNY_MARGIN_SIDE
                + CELL_SIZE / 2 * (i + 1)
                + half_cell_size_and_space_between * i,
                BOARD_MARGIN_TOP + CELL_SIZE / 2,
                CELL_SIZE,
            )

        animalBoardCoordinates[1][0].append(
            (
                BUNNY_MARGIN_SIDE
                + CELL_SIZE / 2 * (i + 1)
                + half_cell_size_and_space_between * i,
                BOARD_MARGIN_TOP + CELL_SIZE / 2,
            )
        )

        # Sheeps
        if i < 4:
            if i == 0:
                draw_animal(
                    WINDOW,
                    BLUE,
                    BUNNY_MARGIN_SIDE + CELL_SIZE + cell_size_and_space_between * i,
                    BOARD_MARGIN_TOP + CELL_SIZE * 1.5 + BETWEEN_CELLS / 2,
                    CELL_SIZE,
                    10,
                    Animal.SHEEP,
                    128,
                )
            if i > 0:
                draw_empty_circles(
                    WINDOW,
                    BLUE,
                    BLACK,
                    BUNNY_MARGIN_SIDE + CELL_SIZE + cell_size_and_space_between * i,
                    BOARD_MARGIN_TOP + CELL_SIZE * 1.5 + BETWEEN_CELLS / 2,
                    CELL_SIZE,
                )
        animalBoardCoordinates[1][1].append(
            (
                BUNNY_MARGIN_SIDE + CELL_SIZE + cell_size_and_space_between * i,
                BOARD_MARGIN_TOP + CELL_SIZE + CELL_SIZE / 2 + BETWEEN_CELLS / 2,
            )
        )

        # Pigs
        if i < 3:
            if i == 0:
                draw_animal(
                    WINDOW,
                    BLUE,
                    BUNNY_MARGIN_SIDE
                    + cell_size_and_space_between
                    + CELL_SIZE / 2 * (i + 1)
                    + half_cell_size_and_space_between * i,
                    BOARD_MARGIN_TOP + CELL_SIZE * 2.5 + BETWEEN_CELLS,
                    CELL_SIZE,
                    10,
                    Animal.PIG,
                    128,
                )
            if i > 0:
                draw_empty_circles(
                    WINDOW,
                    BLUE,
                    BLACK,
                    BUNNY_MARGIN_SIDE
                    + cell_size_and_space_between
                    + CELL_SIZE / 2 * (i + 1)
                    + half_cell_size_and_space_between * i,
                    BOARD_MARGIN_TOP + CELL_SIZE * 2.5 + BETWEEN_CELLS,
                    CELL_SIZE,
                )
            animalBoardCoordinates[1][2].append(
                (
                    BUNNY_MARGIN_SIDE
                    + cell_size_and_space_between
                    + CELL_SIZE / 2 * (i + 1)
                    + half_cell_size_and_space_between * i,
                    BOARD_MARGIN_TOP + CELL_SIZE * 2.5 + BETWEEN_CELLS,
                )
            )

        # Cows
        if i < 2:
            if i == 0:
                draw_animal(
                    WINDOW,
                    BLUE,
                    BUNNY_MARGIN_SIDE
                    + CELL_SIZE * 2
                    + BETWEEN_CELLS
                    + cell_size_and_space_between * i,
                    BOARD_MARGIN_TOP + CELL_SIZE * 3.5 + BETWEEN_CELLS * 1.5,
                    CELL_SIZE,
                    10,
                    Animal.COW,
                    128,
                )
            if i > 0:
                draw_empty_circles(
                    WINDOW,
                    BLUE,
                    BLACK,
                    BUNNY_MARGIN_SIDE
                    + CELL_SIZE * 2
                    + BETWEEN_CELLS
                    + cell_size_and_space_between * i,
                    BOARD_MARGIN_TOP + CELL_SIZE * 3.5 + BETWEEN_CELLS * 1.5,
                    CELL_SIZE,
                )
            animalBoardCoordinates[1][3].append(
                (
                    BUNNY_MARGIN_SIDE
                    + CELL_SIZE * 2
                    + BETWEEN_CELLS
                    + cell_size_and_space_between * i,
                    BOARD_MARGIN_TOP + CELL_SIZE * 3.5 + BETWEEN_CELLS * 1.5,
                )
            )
    draw_animal(
        WINDOW,
        BLUE,
        BUNNY_MARGIN_SIDE + cell_size_and_space_between * 2 + CELL_SIZE / 2,
        BOARD_MARGIN_TOP + CELL_SIZE * 4.5 + BETWEEN_CELLS * 2,
        CELL_SIZE,
        10,
        Animal.HORSE,
        128,
    )

    animalBoardCoordinates[1][4].append(
        (
            BUNNY_MARGIN_SIDE + cell_size_and_space_between * 2 + CELL_SIZE / 2,
            BOARD_MARGIN_TOP + CELL_SIZE * 4.5 + BETWEEN_CELLS * 2,
        )
    )

    # Additional animals
    animalBoardCoordinates[1][0].append(
        (
            BUNNY_MARGIN_SIDE
            + cell_size_and_space_between * 4
            + CELL_SIZE
            + CELL_SIZE / 2
            - CELL_SIZE / 2.4,
            BOARD_MARGIN_TOP,
            BUNNY_MARGIN_SIDE + cell_size_and_space_between * 5,
            BUNNY_MARGIN_SIDE + cell_size_and_space_between * 4,
            2 / 3,
        )
    )

    animalBoardCoordinates[1][1].append(
        (
            BUNNY_MARGIN_SIDE
            + cell_size_and_space_between * 3
            + CELL_SIZE / 2
            + CELL_SIZE
            + CELL_SIZE / 2
            - CELL_SIZE / 2.4,
            BOARD_MARGIN_TOP + CELL_SIZE + BETWEEN_CELLS / 2,
            BUNNY_MARGIN_SIDE + cell_size_and_space_between * 4 + CELL_SIZE / 2,
            BUNNY_MARGIN_SIDE + cell_size_and_space_between * 3 + CELL_SIZE / 2,
            2 / 3,
        )
    )

    animalBoardCoordinates[1][2].append(
        (
            BUNNY_MARGIN_SIDE
            + cell_size_and_space_between * 3
            + CELL_SIZE
            + CELL_SIZE / 2
            - CELL_SIZE / 2.4,
            BOARD_MARGIN_TOP + CELL_SIZE * 2 + BETWEEN_CELLS,
            BUNNY_MARGIN_SIDE + cell_size_and_space_between * 4,
            BUNNY_MARGIN_SIDE + cell_size_and_space_between * 3,
            7 / 12,
        )
    )

    animalBoardCoordinates[1][3].append(
        (
            BUNNY_MARGIN_SIDE
            + cell_size_and_space_between * 2
            + CELL_SIZE / 2
            + CELL_SIZE
            + CELL_SIZE / 2
            - CELL_SIZE / 2.4,
            BOARD_MARGIN_TOP + CELL_SIZE * 3 + BETWEEN_CELLS * 1.5,
            BUNNY_MARGIN_SIDE + cell_size_and_space_between * 3 + CELL_SIZE / 2,
            BUNNY_MARGIN_SIDE + cell_size_and_space_between * 2 + CELL_SIZE / 2,
            2 / 3,
        )
    )

    animalBoardCoordinates[1][4].append(
        (
            BUNNY_MARGIN_SIDE
            + cell_size_and_space_between * 2
            + CELL_SIZE
            + CELL_SIZE / 2
            - CELL_SIZE / 2.4,
            BOARD_MARGIN_TOP + CELL_SIZE * 4 + BETWEEN_CELLS * 2,
            BUNNY_MARGIN_SIDE + cell_size_and_space_between * 3,
            BUNNY_MARGIN_SIDE + cell_size_and_space_between * 2,
            7 / 12,
        )
    )

    print(animalBoardCoordinates)

    py.display.flip()

    return CELL_SIZE


def update_board(WINDOW, player, animals_before, animals_now, CELL_SIZE):
    player_no = player.id
    for animal in animals_now:
        no_animals_before = animals_before[animal]
        no_animals_now = animals_now[animal]
        # Adding new animals
        if no_animals_before < no_animals_now:
            print("Drawing new animals which values are ", animal.value)
            # There are places for animals
            # for i in range(no_animals_before, min(no_animals_now, 5-animal.value)):
            #     draw_animal(WINDOW, BLUE, animalBoardCoordinates[player_no][animal.value][i][0],
            #                 animalBoardCoordinates[player_no][animal.value][i][1], CELL_SIZE, 10, animal, 255)
            # There are places for animals and we'll have new pair
            if no_animals_before % 2 == 1 and no_animals_before < 10 - animal.value * 2:
                draw_animal(
                    WINDOW,
                    BLUE,
                    animalBoardCoordinates[player_no][animal.value][
                        (no_animals_before - 1) // 2
                    ][0],
                    animalBoardCoordinates[player_no][animal.value][
                        (no_animals_before - 1) // 2
                    ][1],
                    CELL_SIZE,
                    10,
                    animal.value,
                    255,
                )
                no_animals_before += 1
            for i in range(
                no_animals_before, min(no_animals_now - 1, 10 - animal.value * 2), 2
            ):
                draw_animal(
                    WINDOW,
                    BLUE,
                    animalBoardCoordinates[player_no][animal.value][i // 2][0],
                    animalBoardCoordinates[player_no][animal.value][i // 2][1],
                    CELL_SIZE,
                    10,
                    animal.value,
                    255,
                )
            if no_animals_now % 2 == 1 and no_animals_now < 10 - animal.value * 2:
                draw_animal(
                    WINDOW,
                    BLUE,
                    animalBoardCoordinates[player_no][animal.value][
                        no_animals_now // 2
                    ][0],
                    animalBoardCoordinates[player_no][animal.value][
                        no_animals_now // 2
                    ][1],
                    CELL_SIZE,
                    10,
                    animal,
                    255,
                )
            # Drawing additional animals
            if no_animals_now > 10 - animal.value * 2:
                py.draw.rect(
                    WINDOW,
                    BLACK,
                    (
                        animalBoardCoordinates[player_no][animal.value][
                            len(animalBoardCoordinates[player_no][animal.value]) - 1
                        ][0],
                        animalBoardCoordinates[player_no][animal.value][
                            len(animalBoardCoordinates[player_no][animal.value]) - 1
                        ][1],
                        CELL_SIZE,
                        CELL_SIZE,
                    ),
                )
                draw_additional_animals(
                    WINDOW,
                    BLUE,
                    BLUE2,
                    BLUE3,
                    animalBoardCoordinates[player_no][animal.value][
                        len(animalBoardCoordinates[player_no][animal.value]) - 1
                    ][2],
                    animalBoardCoordinates[player_no][animal.value][
                        len(animalBoardCoordinates[player_no][animal.value]) - 1
                    ][3],
                    animalBoardCoordinates[player_no][animal.value][
                        len(animalBoardCoordinates[player_no][animal.value]) - 1
                    ][1],
                    animal,
                    animalBoardCoordinates[player_no][animal.value][
                        len(animalBoardCoordinates[player_no][animal.value]) - 1
                    ][4],
                    CELL_SIZE,
                )
                font2 = py.font.Font("Fonts/BRLNSDB.ttf", 32)
                text = "+" + str(no_animals_now - (10 - animal.value * 2))
                text_surface = font2.render(text, True, WHITE)
                WINDOW.blit(
                    text_surface,
                    (
                        animalBoardCoordinates[player_no][animal.value][
                            len(animalBoardCoordinates[player_no][animal.value]) - 1
                        ][0]
                        + CELL_SIZE / 2,
                        animalBoardCoordinates[player_no][animal.value][
                            len(animalBoardCoordinates[player_no][animal.value]) - 1
                        ][1]
                        + CELL_SIZE / 2,
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
                    WINDOW,
                    BLUE,
                    BLACK,
                    animalBoardCoordinates[player_no][animal.value][i // 2][0],
                    animalBoardCoordinates[player_no][animal.value][i // 2][1],
                    CELL_SIZE,
                )
            # Ifs for easier problem solving
            if no_animals_now == 0:
                print("TU: 0")
                draw_animal(
                    WINDOW,
                    BLUE,
                    animalBoardCoordinates[player_no][animal.value][0][0],
                    animalBoardCoordinates[player_no][animal.value][0][1],
                    CELL_SIZE,
                    10,
                    animal,
                    128,
                )
            elif no_animals_now == 1:
                print("TU: 1")
                draw_animal(
                    WINDOW,
                    BLUE,
                    animalBoardCoordinates[player_no][animal.value][0][0],
                    animalBoardCoordinates[player_no][animal.value][0][1],
                    CELL_SIZE,
                    10,
                    animal,
                    255,
                )
            elif no_animals_now == 2:
                print("TU: 2")
                draw_animal(
                    WINDOW,
                    BLUE,
                    animalBoardCoordinates[player_no][animal.value][0][0],
                    animalBoardCoordinates[player_no][animal.value][0][1],
                    CELL_SIZE,
                    10,
                    animal.value,
                    255,
                )
            if no_animals_now <= 10 - animal.value * 2 < no_animals_before:
                print("AAAAAAAA")
                # Removing additional animals
                BLACK_MARKING_SQUARE = (
                    animalBoardCoordinates[player_no][animal.value][
                        5 - animal.value - 1
                    ][0]
                    + CELL_SIZE / 2,
                    animalBoardCoordinates[player_no][animal.value][
                        5 - animal.value - 1
                    ][1]
                    - CELL_SIZE / 2,
                    CELL_SIZE + 10,
                    CELL_SIZE,
                )
                py.draw.rect(WINDOW, BLACK, BLACK_MARKING_SQUARE)
            elif no_animals_now > 10 - animal.value * 2:
                print("TUUUUUUU")
                # Changing value of additional animals printed number
                font2 = py.font.Font("Fonts/BRLNSDB.ttf", 32)
                text = "+" + str(no_animals_now - (10 - animal.value * 2))
                text_surface = font2.render(text, True, WHITE)
                WINDOW.blit(
                    text_surface,
                    (
                        animalBoardCoordinates[player_no][animal.value][
                            len(animalBoardCoordinates[player_no][animal.value]) - 1
                        ][0]
                        + CELL_SIZE / 2,
                        animalBoardCoordinates[player_no][animal.value][
                            len(animalBoardCoordinates[player_no][animal.value]) - 1
                        ][1]
                        + CELL_SIZE / 2,
                    ),
                )
    print(animals_now)
    py.display.flip()


def mark_animals_for_exchange(
    WINDOW, player, animal, first_animal, last_animal, CELL_SIZE, color=BLUE3
):
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
            WINDOW,
            color,
            animalBoardCoordinates[player_no][animal.value][i][0],
            animalBoardCoordinates[player_no][animal.value][i][1],
            CELL_SIZE,
            10,
            animal_to_draw,
            255,
        )
    py.display.flip()


def unmark_animals_for_exchange(
    WINDOW, player, animal, first_animal, no_exchanged_animals, CELL_SIZE
):
    print("ALO")
    mark_animals_for_exchange(
        WINDOW, player, animal, first_animal, no_exchanged_animals, CELL_SIZE, BLUE
    )

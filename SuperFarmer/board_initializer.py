import math

from on_change_drawings import update_board
from players_data import Player
from simple_drawings import *
from util import black, blue, empty_dict, grass_color, red, white


class BoardInitializer:
    """
    Class responsible for creating and storing all board data, especially positions of its elements.
    """

    def __init__(self, font: py.font.Font, no_players: int = 2):
        """
        Initializes game board.
        :param font: Specifies font used to show messages throughout the game.
        :param no_players: Number of players playing.
        """
        self.no_players = no_players
        self.animal_board_coordinates = None
        self.cell_size = None
        self.player_board_width = None
        self.cube_button = None
        self.small_dog_button = None
        self.big_dog_button = None
        self.font = font
        """
        All these attributes are created in create_board method and are used by different modules and classes to work properly.
        """

    def create_board(self, window: Surface) -> None:
        """
        Creates new board for game containing everything required to play - players' boards, buttons, images.
        :param window: Application window where the board will be drawn.
        :return: (None): Only draws board.
        """
        window.fill((0, 0, 0, 0))

        screeninfo = py.display.Info()
        SCREENWIDTH = screeninfo.current_w
        SCREENHEIGHT = screeninfo.current_h
        print(SCREENWIDTH, SCREENHEIGHT)

        self.cell_size = math.floor(SCREENHEIGHT / 8)

        BOARD_MARGIN_TOP = SCREENHEIGHT / 2 - self.cell_size * 2.5
        BUNNY_MARGIN_SIDE = SCREENWIDTH / 2 - self.cell_size * 7
        BETWEEN_CELLS = 7
        BUNNY_MARGIN_SIDE_TWO = (
            SCREENWIDTH - BUNNY_MARGIN_SIDE - self.cell_size * 6 - BETWEEN_CELLS * 6
        )

        self.small_dog_button = (
            0.7 * window.get_width(),
            0.05 * window.get_height(),
            80,
            80,
        )
        self.big_dog_button = (
            0.85 * window.get_width(),
            0.05 * window.get_height(),
            80,
            80,
        )

        bunny = convert_animal_to_img(Animal.RABBIT)
        py.display.set_icon(bunny)

        fence = py.image.load("Images/fence2.png").convert_alpha()
        bluefarmer = py.image.load("Images/bluefarmer.png").convert_alpha()
        bluefarmer_width, bluefarmer_height = bluefarmer.get_size()

        redfarmer = py.image.load("Images/redfarmer.png").convert_alpha()
        redfarmer_width, redfarmer_height = redfarmer.get_size()
        first_table = py.image.load("Images/tablica1.png")
        second_table = py.image.load("Images/tablica2.png")
        naglowek = py.image.load("Images/Naglowek.png")

        dob_house1 = py.image.load("Images/doghouse.png")
        dob_house2 = py.image.load("Images/dog-house.png")

        Image(redfarmer_width / 3 + 150, 618, first_table, 250, 172).draw(window)
        Image(redfarmer_width / 3 + 140 + 272, 618, second_table, 272, 190).draw(window)
        Image(redfarmer_width / 3 + 270, 540, naglowek, 255, 108).draw(window)

        Image(redfarmer_width / 3 - 90, 680, dob_house1, 120, 120).draw(window)
        Image(SCREENWIDTH - bluefarmer_width / 3 - 140, 680, dob_house2, 120, 120).draw(
            window
        )

        Image(
            SCREENWIDTH - bluefarmer_width / 4,
            SCREENHEIGHT - bluefarmer_height / 3,
            bluefarmer,
            bluefarmer_width / 3,
            bluefarmer_height / 3,
        ).draw(window)
        Image(
            -redfarmer_width / 10,
            SCREENHEIGHT - redfarmer_height / 3,
            redfarmer,
            redfarmer_width / 3,
            redfarmer_height / 3,
        ).draw(window)

        self.__draw_dogs_shop(window, self.small_dog_button, self.big_dog_button)

        self.player_board_width = self.cell_size * 5 + BETWEEN_CELLS * 4

        for i in range(8):
            Image(
                BUNNY_MARGIN_SIDE + self.player_board_width / 8 * i,
                BOARD_MARGIN_TOP - self.player_board_width / 12,
                fence,
                self.player_board_width / 8,
                self.player_board_width / 12,
            ).draw(window)

        self.__create_coordinates(
            [BUNNY_MARGIN_SIDE, BUNNY_MARGIN_SIDE_TWO],
            BETWEEN_CELLS,
            BOARD_MARGIN_TOP,
        )

        for player_number in range(self.no_players):
            self.draw_start_animals(window, player_number)

        print(self.animal_board_coordinates)

        self.cube_button = (650, 480, 200, 50)
        cube_button_text_surface = self.font.render("Roll the dices", True, white)
        py.draw.rect(window, red, self.cube_button)
        window.blit(
            cube_button_text_surface,
            (self.cube_button[0] + 20, self.cube_button[1] + 10),
        )

        py.display.flip()

    # end def

    def __create_coordinates(
        self,
        bunny_margin_sides: list[float],
        between_cells: float,
        board_margin_top: float,
    ) -> None:
        """
        Private method for calculating values of animals coordinates on the board
        :param bunny_margin_sides (float): Represents the value of player's board's left edge.
        :param between_cells (float): Represents the value of space between animals cells.
        :param board_margin_top (float): Represents the value of top margin of the board.
        :return: (None): It saves coordinates to board attribue.
        """
        animal_board_coordinates = [
            {
                Animal.RABBIT: [],
                Animal.SHEEP: [],
                Animal.PIG: [],
                Animal.COW: [],
                Animal.HORSE: [],
            }
            for _ in range(self.no_players)
        ]

        half_cell_size_and_space_between = self.cell_size / 2 + between_cells
        self.cell_size_and_space_between = self.cell_size + between_cells

        for player_number in range(self.no_players):
            for circle_number in range(5):
                animal_board_coordinates[player_number][Animal.RABBIT].append(
                    (
                        bunny_margin_sides[player_number]
                        + self.cell_size / 2 * (circle_number + 1)
                        + half_cell_size_and_space_between * circle_number,
                        board_margin_top + self.cell_size / 2,
                    )
                )

                if circle_number < 5 - Animal.SHEEP.value:
                    animal_board_coordinates[player_number][Animal.SHEEP].append(
                        (
                            bunny_margin_sides[player_number]
                            + self.cell_size
                            + self.cell_size_and_space_between * circle_number,
                            board_margin_top
                            + self.cell_size
                            + self.cell_size / 2
                            + between_cells / 2,
                        )
                    )

                if circle_number < 5 - Animal.PIG.value:
                    animal_board_coordinates[player_number][Animal.PIG].append(
                        (
                            bunny_margin_sides[player_number]
                            + self.cell_size_and_space_between
                            + self.cell_size / 2 * (circle_number + 1)
                            + half_cell_size_and_space_between * circle_number,
                            board_margin_top + self.cell_size * 2.5 + between_cells,
                        )
                    )

                if circle_number < 5 - Animal.COW.value:
                    animal_board_coordinates[player_number][Animal.COW].append(
                        (
                            bunny_margin_sides[player_number]
                            + self.cell_size * 2
                            + between_cells
                            + self.cell_size_and_space_between * circle_number,
                            board_margin_top
                            + self.cell_size * 3.5
                            + between_cells * 1.5,
                        )
                    )

                if circle_number < 5 - Animal.HORSE.value:
                    animal_board_coordinates[player_number][Animal.HORSE].append(
                        (
                            bunny_margin_sides[player_number]
                            + self.cell_size_and_space_between * 2
                            + self.cell_size / 2,
                            board_margin_top + self.cell_size * 4.5 + between_cells * 2,
                        )
                    )

            for animal_number in range(5):
                animal_board_coordinates[player_number][Animal(animal_number)].append(
                    (
                        bunny_margin_sides[player_number]
                        + self.cell_size_and_space_between * 4
                        + (self.cell_size / 2) * (animal_number % 2)
                        + self.cell_size
                        + self.cell_size / 2
                        - self.cell_size / 2.4,
                        board_margin_top
                        + (self.cell_size + between_cells / 2) * animal_number,
                        bunny_margin_sides[player_number]
                        + self.cell_size_and_space_between
                        * (5 - (animal_number + 1) // 2)
                        + (self.cell_size / 2) * (animal_number % 2),
                        bunny_margin_sides[player_number]
                        + self.cell_size_and_space_between
                        * (4 - (animal_number + 1) // 2)
                        + (self.cell_size / 2) * (animal_number % 2),
                        2 / 3,
                    )
                )

        self.animal_board_coordinates = animal_board_coordinates

    # end def

    def draw_start_animals(
        self,
        window: Surface,
        player_id: int,
        color: tuple[int, int, int] = blue,
        size: float = 10,
    ) -> None:
        """
        Draws starting player board with background, where there are no animals.
        :param window: Application window where the board will be drawn.
        :param player_id: Player's identification.
        :param color: Color of animals circles.
        :param size: Size of animal in the circle.
        :return: (None) Only draws animals.
        """

        self.__polygon(window, player_id)

        for animal, fields in self.animal_board_coordinates[player_id].items():
            for field_number in range(len(fields) - 1):
                if field_number == 0:
                    draw_animal(
                        window,
                        color,
                        fields[field_number][0],
                        fields[field_number][1],
                        self.cell_size,
                        size,
                        animal,
                        128,
                    )
                else:
                    draw_empty_circles(
                        window,
                        color,
                        black,
                        fields[field_number][0],
                        fields[field_number][1],
                        self.cell_size,
                    )

    # end def

    def draw_current_animals(
        self, window: Surface, player: Player, current_animals: dict[Animal, int]
    ) -> None:
        """
        Draws board with current status of player's animals, with background.
        :param window: Application window where the board will be drawn.
        :param player: Player which animals will be drawn.
        :param current_animals: Animals now.
        :return: (None) Only draws.
        """

        self.draw_start_animals(window, player.id)
        update_board(
            window,
            player,
            empty_dict,
            current_animals,
            self.animal_board_coordinates,
            self.cell_size,
        )

    def __draw_dogs_shop(
        self,
        window: Surface,
        small_dog_button: tuple[float, float, float, float],
        big_dog_button: tuple[float, float, float, float],
    ) -> None:
        """
        Draws dog shop in the top-right corner of the application window.
        :param window: Application window where the board will be drawn.
        :param small_dog_button: Button responsible for buying small dogs.
        :param big_dog_button: Button responsible for buying big dogs.
        :return: (None) Only draws
        """
        small_dog = py.image.load("Images/smalldog.png")
        Image(
            small_dog_button[0],
            small_dog_button[1],
            small_dog,
            small_dog_button[2],
            small_dog_button[3],
        ).draw(window)
        big_dog = py.image.load("Images/bigdog.png")
        Image(
            big_dog_button[0],
            big_dog_button[1],
            big_dog,
            big_dog_button[2],
            big_dog_button[3],
        ).draw(window)

        font = py.font.Font("Fonts/BRLNSDB.ttf", 28)

        dog_cost = font.render("Cost:", True, white)
        window.blit(dog_cost, (small_dog_button[0] - 70, small_dog_button[1]))
        window.blit(
            dog_cost, (big_dog_button[0] + big_dog_button[2] + 20, big_dog_button[1])
        )

        draw_animal(
            window,
            blue,
            small_dog_button[0] - 40,
            small_dog_button[1] + 50,
            50,
            10,
            Animal.SHEEP,
            255,
        )
        draw_animal(
            window,
            blue,
            big_dog_button[0] + big_dog_button[2] + 50,
            big_dog_button[1] + 50,
            50,
            10,
            Animal.COW,
            255,
        )

        dog_info_1 = font.render("Buy them", True, white)
        dog_info_2 = font.render("       by", True, white)
        dog_info_3 = font.render("  clicking", True, white)
        window.blit(
            dog_info_1,
            (small_dog_button[0] + small_dog_button[2] + 10, small_dog_button[1]),
        )
        window.blit(
            dog_info_2,
            (small_dog_button[0] + small_dog_button[2] + 10, small_dog_button[1] + 28),
        )
        window.blit(
            dog_info_3,
            (small_dog_button[0] + small_dog_button[2] + 10, small_dog_button[1] + 56),
        )

    # end def

    def __polygon(
        self,
        window: Surface,
        player_id: int,
        color: tuple[int, int, int] = grass_color,
    ) -> None:
        """
        Function drawing polygon which is a background to player's board.
        :param window: Button responsible for buying small dogs.
        :param player_id: Player's identification.
        :param color: Color of polygon
        :return: (None) Only draws.
        """

        bunny_margin_side = self.animal_board_coordinates[player_id][Animal.RABBIT][0][0] - self.cell_size / 2
        board_margin_top = self.animal_board_coordinates[player_id][Animal.RABBIT][0][1] - self.cell_size / 2

        py.draw.polygon(
            window,
            color,
            [
                (bunny_margin_side, board_margin_top),
                (bunny_margin_side + self.player_board_width, board_margin_top),
                (
                    bunny_margin_side + self.player_board_width / 2,
                    board_margin_top + self.cell_size * 5,
                ),
            ],
            0,
        )

    # end def


# end class

import random
from enum import Enum

import pygame as py
from pygame import Surface


class Image:
    """
    Class responsible for creating and drawing images.
    """

    def __init__(
        self, x: float, y: float, image: Surface, width: float, height: float
    ) -> None:
        """
        Creates an image object.
        :param x: Horizontal position of an image.
        :param y: Vertical position of an image.
        :param image: File converted to image using py.image.load function.
        :param width: Expected width of image.
        :param height: Expected height of an image.
        """
        self.image = py.transform.scale(image, (width, height))
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, window: Surface) -> None:
        """
        Draws image on specified place.
        :param window: Application window where the board will be drawn.
        :return: (None) Only draws an image on the window.
        """
        window.blit(self.image, self.rect)


class Bank:
    """
    Class representing bank of animals and dogs.
    """

    def __init__(self) -> None:
        """
        Initializes the bank.
        """
        self.animals = {
            Animal.RABBIT: 60,
            Animal.SHEEP: 24,
            Animal.PIG: 20,
            Animal.COW: 12,
            Animal.HORSE: 6,
        }
        self.dogs = {
            Defence.SMALLDOG: 4,
            Defence.BIGDOG: 2,
        }

    # end def

    def reset_bank(self) -> None:
        """
        Resets bank for restarting the game - sets it to initial values.
        :return: (None) Only resets bank.
        """
        self.animals = {
            Animal.RABBIT: 60,
            Animal.SHEEP: 24,
            Animal.PIG: 20,
            Animal.COW: 12,
            Animal.HORSE: 6,
        }
        self.dogs = {
            Defence.SMALLDOG: 4,
            Defence.BIGDOG: 2,
        }


class Animal(Enum):
    """
    Possible animals to keep.
    """

    RABBIT = 0
    SHEEP = 1
    PIG = 2
    COW = 3
    HORSE = 4


# end enum


class Defence(Enum):
    """
    Possible dogs to buy for defence from predators.
    """

    SMALLDOG = 6
    BIGDOG = 7


# end enum


class Predators(Enum):
    """
    Possible predators which can attack farm.
    """

    FOX = 10
    WOLF = 11


# end enum

"""Dictionary representing cost of exchanging animals."""
exchange_cost = {
    Animal.RABBIT: {Animal.SHEEP: 6, Animal.PIG: 12, Animal.COW: 36, Animal.HORSE: 72},
    Animal.SHEEP: {Animal.PIG: 2, Animal.COW: 6, Animal.HORSE: 12},
    Animal.PIG: {Animal.COW: 3, Animal.HORSE: 6},
    Animal.COW: {Animal.HORSE: 2},
    Animal.HORSE: {},
}

empty_dict = {
    Animal.RABBIT: 0,
    Animal.SHEEP: 0,
    Animal.PIG: 0,
    Animal.COW: 0,
    Animal.HORSE: 0,
}

"""Animals which can be drawn on orange dice."""
animals1 = [
    Animal.RABBIT,
    Animal.RABBIT,
    Animal.RABBIT,
    Animal.RABBIT,
    Animal.SHEEP,
    Animal.SHEEP,
    Animal.SHEEP,
    Animal.PIG,
    Animal.PIG,
    Animal.PIG,
    Animal.HORSE,
    Predators.FOX,
]

"""Animals which can be drawn on blue dice."""
animals2 = [
    Animal.RABBIT,
    Animal.RABBIT,
    Animal.RABBIT,
    Animal.RABBIT,
    Animal.SHEEP,
    Animal.SHEEP,
    Animal.SHEEP,
    Animal.PIG,
    Animal.PIG,
    Animal.PIG,
    Animal.COW,
    Predators.WOLF,
]


"""Colors of elements used in the game"""
blue = (52, 229, 235)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
dark_grey = (59, 59, 59)
green = (0, 255, 0)
grass_color = (124, 252, 0)
dark_green = (0, 125, 0)
blue2 = (93, 190, 194)
blue3 = (38, 125, 128)
light_yellow = (238, 255, 125)


def rand_animals() -> tuple[Animal, Animal]:
    """
    Function drawing animals from dices.
    :return: (tuple[Animal, Animal]) Tuple of drawn animals.
    """
    rand1 = random.randint(0, 11)
    rand2 = random.randint(0, 11)

    return animals2[rand1], animals1[rand2]


# end def


def convert_animal_to_img(animal: Animal) -> Surface:
    """
    Converts animal to image.
    :param animal: Specifies the animal to be converted.
    :return: Animal image.
    """
    img = None
    if not isinstance(animal, Animal) and not isinstance(animal, Predators):
        print("Nie zwierzę ", animal)
        if animal == Animal.RABBIT.value:
            img = py.image.load("Images/bunnypair.png")
        if animal == Animal.SHEEP.value:
            img = py.image.load("Images/sheeppair.png")
        if animal == Animal.PIG.value:
            img = py.image.load("Images/pigpair.png")
        if animal == Animal.COW.value:
            img = py.image.load("Images/cowpair.png")
        if animal == Animal.HORSE.value:
            img = py.image.load("Images/horsepair.png")
        return img
    if animal.value == Animal.RABBIT.value:
        img = py.image.load("Images/bunny.png")
    if animal.value == Animal.SHEEP.value:
        img = py.image.load("Images/sheep.png")
    if animal.value == Animal.PIG.value:
        img = py.image.load("Images/pig.png")
    if animal.value == Animal.COW.value:
        img = py.image.load("Images/cow.png")
    if animal.value == Animal.HORSE.value:
        img = py.image.load("Images/horse.png")
    if animal.value == Predators.FOX.value:
        img = py.image.load("Images/horse.png")
    if animal.value == Predators.WOLF.value:
        img = py.image.load("Images/horse.png")
    return img


# end def


def convert_animal_to_dice_img(animal: Animal, dice_number: int) -> Surface:
    """
    Converts animal to dice image.
    :param animal: Animal to be converted.
    :param dice_number: Number of dice - 1 for blue dice and 2 for orange dice.
    :return:
    """
    img = None
    if animal.value == Animal.RABBIT.value:
        if dice_number == 1:
            img = py.image.load("Images/bunnydice.png")
        elif dice_number == 2:
            img = py.image.load("Images/bunnydice2.png")
    if animal.value == Animal.SHEEP.value:
        if dice_number == 1:
            img = py.image.load("Images/sheepdice.png")
        elif dice_number == 2:
            img = py.image.load("Images/sheepdice2.png")
    if animal.value == Animal.PIG.value:
        if dice_number == 1:
            img = py.image.load("Images/pigdice.png")
        elif dice_number == 2:
            img = py.image.load("Images/pigdice2.png")
    if animal.value == Animal.COW.value and dice_number == 1:
        img = py.image.load("Images/cowdice2.png")
    if animal.value == Animal.HORSE.value and dice_number == 2:
        img = py.image.load("Images/horsedice.png")
    if animal.value == Predators.FOX.value and dice_number == 2:
        img = py.image.load("Images/Foxdice.png")
    if animal.value == Predators.WOLF.value and dice_number == 1:
        img = py.image.load("Images/wolfdice.png")
    return img


# end def

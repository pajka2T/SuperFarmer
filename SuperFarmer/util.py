import random
from enum import Enum
import pygame as py


class Animal(Enum):
    RABBIT = 0
    SHEEP = 1
    PIG = 2
    COW = 3
    HORSE = 4
# end enum


class Defence(Enum):
    SMALLDOG = 6
    BIGDOG = 7
# end enum


class Predators(Enum):
    FOX = 10
    WOLF = 11
# end enum


bank = {Animal.RABBIT: 60, Animal.SHEEP: 24, Animal.PIG: 20, Animal.COW: 12, Animal.HORSE: 6,
        Defence.SMALLDOG: 4, Defence.BIGDOG: 2}

exchange_cost = {Animal.RABBIT: {Animal.SHEEP: 6, Animal.PIG: 12, Animal.COW: 36, Animal.HORSE: 72},
                 Animal.SHEEP: {Animal.PIG: 2, Animal.COW: 6, Animal.HORSE: 12},
                 Animal.PIG: {Animal.COW: 3, Animal.HORSE: 6},
                 Animal.COW: {Animal.HORSE: 2},
                 Animal.HORSE: {}}

animals1 = [Animal.RABBIT, Animal.RABBIT, Animal.RABBIT, Animal.RABBIT,
            Animal.SHEEP, Animal.SHEEP, Animal.SHEEP,
            Animal.PIG, Animal.PIG, Animal.PIG,
            Animal.HORSE,
            Predators.FOX]

animals2 = [Animal.RABBIT, Animal.RABBIT, Animal.RABBIT, Animal.RABBIT,
            Animal.SHEEP, Animal.SHEEP, Animal.SHEEP,
            Animal.PIG, Animal.PIG, Animal.PIG,
            Animal.COW,
            Predators.WOLF]


def rand_animals():
    rand1 = random.randint(0, 11)
    rand2 = random.randint(0, 11)

    return animals1[rand1], animals2[rand2]
# end def


def convert_animal_to_img(animal_number):
    img = None
    if animal_number == Animal.RABBIT.value:
        img = py.image.load("Images/bunny.png")
    if animal_number == Animal.SHEEP.value:
        img = py.image.load("Images/sheep.png")
    if animal_number == Animal.PIG.value:
        img = py.image.load("Images/pig.png")
    if animal_number == Animal.COW.value:
        img = py.image.load("Images/cow.png")
    if animal_number == Animal.HORSE.value:
        img = py.image.load("Images/horse.png")
    return img
# end def

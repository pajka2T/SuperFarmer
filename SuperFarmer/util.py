import random
from enum import Enum


class Animal(Enum):
    RABBIT = 1
    SHEEP = 2
    PIG = 3
    COW = 4
    HORSE = 5
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


def convert_animal_to_img(animal):
    if animal == Animal.RABBIT:
        return "rabbit.jpg"
    if animal == Animal.SHEEP:
        return "sheep.jpg"
    if animal == Animal.PIG:
        return "pig.jpg"
    if animal == Animal.COW:
        return "cow.jpg"
    if animal == Animal.HORSE:
        return "horse.jpg"
    return
# end def

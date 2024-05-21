import random
from enum import Enum

import pygame as py


class Image:

    def __init__(self, x, y, image, width, height):
        self.image = py.transform.scale(image, (width, height))
        self.rect = image.get_rect()  # copy the image dimensions
        # print("UUU")
        self.rect.x = x
        self.rect.y = y  # move to location

    def draw(self, window):
        window.blit(self.image, self.rect)  # paint it


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


bank = {
    Animal.RABBIT: 60,
    Animal.SHEEP: 24,
    Animal.PIG: 20,
    Animal.COW: 12,
    Animal.HORSE: 6,
    Defence.SMALLDOG: 4,
    Defence.BIGDOG: 2,
}

exchange_cost = {
    Animal.RABBIT: {Animal.SHEEP: 6, Animal.PIG: 12, Animal.COW: 36, Animal.HORSE: 72},
    Animal.SHEEP: {Animal.PIG: 2, Animal.COW: 6, Animal.HORSE: 12},
    Animal.PIG: {Animal.COW: 3, Animal.HORSE: 6},
    Animal.COW: {Animal.HORSE: 2},
    Animal.HORSE: {},
}

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


def rand_animals():
    rand1 = random.randint(0, 11)
    rand2 = random.randint(0, 11)

    return animals2[rand1], animals1[rand2]


# end def


def convert_animal_to_img(animal):
    img = None
    if not isinstance(animal, Animal) and not isinstance(animal, Predators):
        print("Nie zwierzę ", animal)
        # We have a pair of animals
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
    # We have one animal
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


def convert_animal_to_dice_img(animal, k):
    img = None
    if animal.value == Animal.RABBIT.value:
        if k == 1:
            img = py.image.load("Images/bunnydice.png")
        elif k == 2:
            img = py.image.load("Images/bunnydice2.png")
    if animal.value == Animal.SHEEP.value:
        if k == 1:
            img = py.image.load("Images/sheepdice.png")
        elif k == 2:
            img = py.image.load("Images/sheepdice2.png")
    if animal.value == Animal.PIG.value:
        if k == 1:
            img = py.image.load("Images/pigdice.png")
        elif k == 2:
            img = py.image.load("Images/pigdice2.png")
    if animal.value == Animal.COW.value and k == 1:
        img = py.image.load("Images/cowdice2.png")
    if animal.value == Animal.HORSE.value and k == 2:
        img = py.image.load("Images/horsedice.png")
    if animal.value == Predators.FOX.value and k == 2:
        img = py.image.load("Images/Foxdice.png")
    if animal.value == Predators.WOLF.value and k == 1:
        img = py.image.load("Images/wolfdice.png")
    return img

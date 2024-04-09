import random

bank = dict(rabbits=60, sheep=24, pigs=20, cows=12, horses=6, small_dogs=4, big_dogs=2)

animals1 = ["rabbits", "rabbits", "rabbits", "rabbits",
            "sheep", "sheep", "sheep",
            "pigs", "pigs", "pigs",
            "horses",
            "fox"]

animals2 = ["rabbits", "rabbits", "rabbits", "rabbits",
            "sheep", "sheep", "sheep",
            "pigs", "pigs", "pigs",
            "cows",
            "wolf"]


def rand_animals():
    rand1 = random.randint(0, 11)
    rand2 = random.randint(0, 11)

    return animals1[rand1], animals2[rand2]
# end def

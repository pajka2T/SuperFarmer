import random

animals = ["rabbits", "rabbits", "rabbits", "rabbits", "rabbits",
           "sheep", "sheep", "sheep",
           "pigs", "pigs",
           "cows",
           "horses"]


def rand_animals():
    rand1 = random.randint(0, 11)
    rand2 = random.randint(0, 11)

    return animals[rand1], animals[rand2]
# end def

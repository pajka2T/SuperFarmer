import pygame as py
from pygame.locals import *

import players_data as pd
import util


class AppClass:
    def __init__(self):
        py.init()
        AppClass.screen = py.display.set_mode((800, 450))
        AppClass.running = True

    def play(self):
        while AppClass.running:
            for event in py.event.get():
                if event.type == QUIT:
                    AppClass.running = False
        py.quit()
# end class


if __name__ == '__main__':
    # AppClass().play()
    data = pd.create_users(2)
    data[0]["rabbits"] = 0
    data[0]["sheep"] = 0
    for i in range(20):
        res1, res2 = util.rand_animals()
        print(res1, res2)
        pd.add_animals(0, res1, res2)
        print(data[0])
        print(util.bank)

    print(data)

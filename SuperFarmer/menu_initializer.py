import pygame as py
from pygame import Surface

from util import black, green, light_yellow, white


class MenuInitializer:
    def __init__(self, font: py.font.Font) -> None:
        self.start_button = None
        self.font = font
        self.start_button = None

    def create_menu(self, window: Surface) -> None:
        whole_menu = (
            window.get_width() / 4,
            window.get_height() / 4,
            window.get_width() / 2,
            window.get_height() / 2,
        )
        py.draw.rect(window, light_yellow, whole_menu)

        menu_text_surface = self.font.render("MENU", True, black)
        window.blit(
            menu_text_surface,
            (whole_menu[0] + whole_menu[2] / 2 - 20, whole_menu[1] + 20),
        )

        self.start_button = (
            window.get_width() / 2 - 100,
            window.get_height() / 2 - 50,
            200,
            100,
        )
        py.draw.rect(window, green, self.start_button)
        start_text_surface = self.font.render("Start game", True, white)
        window.blit(
            start_text_surface, (self.start_button[0] + 10, self.start_button[1] + 10)
        )

        py.display.flip()

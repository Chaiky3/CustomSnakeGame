import pygame
import random

from typing import Tuple
from pygame import Surface

from consts import display, MAX_FOOD_WIDTH, MAX_FOOD_HEIGHT, FOOD_OPTIONS


class Food:
    def __init__(self) -> None:
        """
        ::
            Constructor for Food. Food helps snake to grow.
        """
        self.position: Tuple[int, int] = self.get_random_point()
        self.sticker: Surface = self.get_random_sticker()
        #  representing_rect helps in colllision detecting
        self.representing_rect = pygame.Rect(
            self.position[0], self.position[1], MAX_FOOD_WIDTH, MAX_FOOD_HEIGHT)

    def get_random_point(self) -> Tuple[int, int]:
        """
        ::
            Generates a point in the display space.

        Return:
            (Tuple[int, int]):  Random point.
        """
        return random.randrange(
            0, display.get_width() - MAX_FOOD_WIDTH), random.randrange(0, display.get_height() - MAX_FOOD_HEIGHT)

    def get_random_sticker(self) -> Surface:
        """
        ::
            Randomly chooses a stiker to use as food.

        Return:
            (Surface):          Sticker with transperent background.
        """
        return pygame.image.load(random.choice(FOOD_OPTIONS)).convert_alpha()

    def draw(self) -> None:
        """
        ::
            Drawer for Food.
        """
        display.blit(self.sticker, self.position)

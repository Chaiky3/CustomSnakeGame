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
        width_bound = display.get_width() - MAX_FOOD_WIDTH
        height_bound = display.get_height() - MAX_FOOD_HEIGHT
        
        # Ensure we don't random range with <= 0 values
        x = random.randrange(0, max(1, width_bound))
        y = random.randrange(0, max(1, height_bound))
        return (x, y)

    def get_random_sticker(self) -> Surface:
        """
        ::
            Randomly chooses a sticker to use as food. If no image options
            are found, falls back to a dynamically generated red apple drawing.

        Return:
            (Surface):          Sticker with transparent background.
        """
        if FOOD_OPTIONS:
            try:
                img_path = random.choice(FOOD_OPTIONS)
                return pygame.image.load(img_path).convert_alpha()
            except Exception:
                pass

        # Fallback vector-drawn generic apple asset
        surf = Surface((MAX_FOOD_WIDTH, MAX_FOOD_HEIGHT), pygame.SRCALPHA)
        # Red apple body
        pygame.draw.ellipse(surf, (220, 20, 60), (0, 10, MAX_FOOD_WIDTH, MAX_FOOD_HEIGHT - 10))
        # Green leaf
        pygame.draw.ellipse(surf, (34, 139, 34), (MAX_FOOD_WIDTH // 2, 0, 15, 15))
        return surf

    def draw(self) -> None:
        """
        ::
            Drawer for Food.
        """
        display.blit(self.sticker, self.position)

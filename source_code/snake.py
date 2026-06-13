import random
import pygame

from time import sleep
from typing import Tuple
from pygame import K_RIGHT, K_LEFT, K_UP, K_DOWN

from smartQeue import SmartQeue
from food import Food
from consts import display, background, clock, EAT_SOUND, SNAKE_SPEED, SNAKE_COLOR, SNAKE_THICKNESS, NODE_LENGTH, SPEED_GROWTH_CONST, TEXT_FONT, WHITE


class Snake:
    def __init__(self, speed: int = SNAKE_SPEED, color: Tuple[int, int, int] = SNAKE_COLOR, thickness: int = SNAKE_THICKNESS) -> None:
        """
        ::
            Constructor for Snake. Using SmartQeue to manage snake's nodes.

        Parameters:
            (int) speed:                    Clocks ticks between moves (milliseconds).
            (Tuple[int, int, int]) color:   Snake color (r,g,b).
            (int) thickness:                Thickness of snake.  
        """
        self.nodes = SmartQeue()
        first_point, second_point, self.direction = Snake.get_random_snake_state()
        self.nodes.append(first_point)
        self.nodes.append(second_point)

        self.speed = speed
        self.color = color
        self.thickness = thickness

    @staticmethod
    def get_random_snake_state() -> Tuple[Tuple[int, int], Tuple[int, int], int]:
        """
        ::
            Randomly generates starting position for snake.

        Return:
            (Tuple[Tuple[int, int], Tuple[int, int], int]):        First point, Second point, direction.
        """
        point_a = None
        #  Initiating invalid point to enter while loop
        point_b = (-1, -1)
        direction = None

        while Snake.point_out_of_limits(point_b):

            point_a = random.randrange(
                0, display.get_width()), random.randrange(0, display.get_height())

            direction = random.choice([K_RIGHT, K_LEFT, K_UP, K_DOWN])

            point_b = Snake.determine_next_point(point_a, direction)

        return point_a, point_b, direction

    @staticmethod
    def determine_next_point(current_point: Tuple[int, int], direction: int) -> Tuple[int, int]:
        """
        ::
            Find next point position given starting point and direction.

        Return:
            (Tuple[int, int]):      Next point.
        """

        current_x, current_y = current_point

        if direction == K_RIGHT:
            return current_x + NODE_LENGTH, current_y

        elif direction == K_LEFT:
            return current_x - NODE_LENGTH, current_y

        elif direction == K_UP:
            return current_x, current_y - NODE_LENGTH

        elif direction == K_DOWN:
            return current_x, current_y + NODE_LENGTH

    @staticmethod
    def point_out_of_limits(point: Tuple[int, int]) -> bool:
        """
        ::
            Checks if point is out of display limits.

        Parameters:
            (Tuple[int, int]) point:        Given point.
        Return:
            (bool):                         Point out of limits.
        """
        point_x, point_y = point

        return point_x < 0 or point_x > display.get_width() or point_y < 0 or point_y > display.get_height()

    def draw(self) -> None:
        """
        ::
            Drawer for snake.
        """
        pygame.draw.lines(display, SNAKE_COLOR, False,
                          self.nodes.qeue, self.thickness)

    def is_opposite_direction(self, new_direction: int) -> bool:
        """
        ::
            Checks if new direction is vertical to current one.

        Parameters:
            (int) new_direction:    New direction.  
        Return:
            (bool):                 Directions are vertical.
        """

        if sorted([self.direction, new_direction]) == sorted([K_UP, K_DOWN]):
            return True

        if sorted([self.direction, new_direction]) == sorted([K_RIGHT, K_LEFT]):
            return True

        return False

    def increase_speed(self) -> None:
        """
        ::
            Increases snake's speed (exponential).
        """
        self.speed *= SPEED_GROWTH_CONST

    def did_self_eat(self) -> bool:
        """
        ::
            Checks if snake ate itself.
            Doing it by comparing the head point with all other points.

        Return:
            (bool)      Snake ate itself.
        """

        snake_head = self.nodes.get_head_point()
        rest_of_body = self.nodes.qeue[2:]

        return any([snake_head == point for point in rest_of_body])

    def did_eat_food(self, food: Food) -> bool:
        """
        ::
            Checks if snake ate the food.

        Parameters:
            (Food) food:        The food that is located on the display.
        Return:
            (bool):             Snake ate food.
        """

        (point_a_x, point_a_y), (point_b_x, point_b_y) = self.nodes.get_head_node()

        try:
            return food.representing_rect.clipline(point_a_x, point_a_y, point_b_x, point_b_y)
        except AttributeError:  # If food is None, an exception will be raised.
            return False

    def move(self, direction: int, food: Food = None, grow: bool = False) -> bool:
        """
        ::
            This function manages snake's movement:
                - Gets the next point
                - Verifies that it's in limits
                - Increases snake's length if needed
                - Checks if snake ate food
                - Checks if snake ate itself

        Parameters:
            (int) direction:        Direction to which snake moves.
            (Food) food:            The food that's located on the display.
            (bool) grow:            Whether or not snake needs to grow.
        Return:
            (bool):                 Snake ate food.
        """

        self.direction = direction

        next_point = self.determine_next_point(
            self.nodes.get_head_point(), direction)

        if Snake.point_out_of_limits(next_point):
            self.end_game()

        if grow:
            self.nodes.append(next_point)

        else:
            self.nodes.push(next_point)

        display.blit(background, (0, 0))
        self.draw()

        if self.did_self_eat():
            self.end_game()

        if self.did_eat_food(food):
            pygame.mixer.Sound.play(EAT_SOUND)
            pygame.mixer.music.stop()

            self.increase_speed()

            clock.tick(self.speed)
            self.move(direction, grow=True)

            return True

    def get_length(self) -> int:
        """
        Return:
            (int):                  Length of snake in nodes.
        """
        return len(self.nodes.qeue) - 1

    def show_score(self) -> None:
        """
        ::
            Writes user's score on the left upper corner.
        """

        font = pygame.font.Font(TEXT_FONT, 70)
        text = font.render(f"{self.get_length()}", True, WHITE)

        text_rect = text.get_rect()

        text_rect.center = (display.get_width() // 10,
                            display.get_height() // 8)

        display.blit(text, text_rect)

    def end_game(self) -> None:
        """
        ::
            Ends game and closes window.
            Called in 3 cases:
                - User exits game.
                - Snake has gotten to edge.
                - Snake ate itself.

            Prints a "Game Over" message and quits.
        """

        font = pygame.font.Font(TEXT_FONT, 100)
        text = font.render('Game Over', True, WHITE)

        text_rect = text.get_rect()

        text_rect.center = (display.get_width() // 2,
                            display.get_height() // 4)

        self.show_score()
        display.blit(text, text_rect)
        pygame.display.update()

        sleep(2)

        pygame.quit()
        quit()

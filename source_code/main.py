import pygame

from pygame import QUIT, KEYDOWN, K_ESCAPE, K_RIGHT, K_LEFT, K_UP, K_DOWN\

from snake import Snake
from food import Food
from consts import clock, NEW_FOOD_EVENT, FOOD_APPEAR_SOUND


def run_game_loop() -> None:
    """
    ::
        Game loop. On charge of:
            - Responding to events.
            - Showing objects.
            - Running the clock ticks.
    """

    snake = Snake()
    food = None

    while True:

        changed_direction = False

        for event in pygame.event.get():

            if event.type == QUIT:  # user clicked exit button
                snake.end_game()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    snake.end_game()

                if event.key == K_RIGHT or event.key == K_LEFT or event.key == K_UP or event.key == K_DOWN:
                    if event.key != snake.direction and not snake.is_opposite_direction(event.key):
                        changed_direction = True
                        snake.direction = event.key
                        if snake.move(snake.direction, food=food):
                            food = None

            # adds food every FOOD_TIME_INTERVAL if there is not any
            elif event.type == NEW_FOOD_EVENT and not food:
                if FOOD_APPEAR_SOUND:
                    pygame.mixer.Sound.play(FOOD_APPEAR_SOUND)
                    pygame.mixer.music.stop()
                food = Food()

        if not changed_direction and snake.move(snake.direction, food=food):
            food = None

        if food:
            food.draw()

        snake.show_score()
        pygame.display.update()

        clock.tick(snake.speed)


if __name__ == '__main__':

    run_game_loop()

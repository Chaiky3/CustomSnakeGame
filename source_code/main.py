import os
import pygame

from pygame import QUIT, KEYDOWN, K_ESCAPE, K_RIGHT, K_LEFT, K_UP, K_DOWN\

from snake import Snake, GameOverException
from food import Food
from consts import (
    clock,
    NEW_FOOD_EVENT,
    FOOD_APPEAR_SOUND,
    TEXT_FONT,
    WHITE,
    display,
    background
)

HIGH_SCORE_FILE = "highscore.txt"


def get_high_score() -> int:
    """Loads the high score from highscore.txt."""
    if os.path.exists(HIGH_SCORE_FILE):
        try:
            with open(HIGH_SCORE_FILE, "r") as f:
                return int(f.read().strip())
        except Exception:
            return 0
    return 0


def save_high_score(score: int) -> None:
    """Saves the high score to highscore.txt."""
    try:
        with open(HIGH_SCORE_FILE, "w") as f:
            f.write(str(score))
    except Exception:
        pass


def show_start_screen() -> None:
    """Displays a retro Start Screen and blocks until Space is pressed or Quit."""
    font_large = pygame.font.Font(TEXT_FONT, 60)
    font_small = pygame.font.Font(TEXT_FONT, 30)

    while True:
        display.blit(background, (0, 0))

        title_text = font_large.render("CUSTOM SNAKE GAME", True, WHITE)
        instruction_text = font_small.render("Press SPACE to Play or ESC to Quit", True, WHITE)

        title_rect = title_text.get_rect(center=(display.get_width() // 2, display.get_height() // 3))
        instruction_rect = instruction_text.get_rect(center=(display.get_width() // 2, display.get_height() // 2))

        display.blit(title_text, title_rect)
        display.blit(instruction_text, instruction_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_SPACE:
                    return
        clock.tick(15)


def show_game_over_screen(score: int) -> bool:
    """Displays Game Over screen with score and options to restart or quit."""
    high_score = get_high_score()
    is_new_high = score > high_score

    if is_new_high:
        save_high_score(score)
        high_score = score

    font_large = pygame.font.Font(TEXT_FONT, 70)
    font_medium = pygame.font.Font(TEXT_FONT, 40)
    font_small = pygame.font.Font(TEXT_FONT, 25)

    while True:
        display.blit(background, (0, 0))

        go_text = font_large.render("Game Over", True, WHITE)

        if is_new_high:
            score_text = font_medium.render(f"NEW High Score: {score}!", True, (255, 215, 0))
        else:
            score_text = font_medium.render(f"Score: {score} | High Score: {high_score}", True, WHITE)

        restart_text = font_small.render("Press R to Restart or ESC to Quit", True, WHITE)

        go_rect = go_text.get_rect(center=(display.get_width() // 2, display.get_height() // 4))
        score_rect = score_text.get_rect(center=(display.get_width() // 2, display.get_height() // 2))
        restart_rect = restart_text.get_rect(center=(display.get_width() // 2, display.get_height() // 1.5))

        display.blit(go_text, go_rect)
        display.blit(score_text, score_rect)
        display.blit(restart_text, restart_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return False
                elif event.key == pygame.K_r:
                    return True
        clock.tick(15)


if __name__ == '__main__':
    show_start_screen()
    
    keep_playing = True
    while keep_playing:
        snake = Snake()
        food = None
        score = 0
        
        try:
            while True:
                changed_direction = False

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        quit()

                    elif event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            raise GameOverException()

                        if event.key in (K_RIGHT, K_LEFT, K_UP, K_DOWN):
                            if event.key != snake.direction and not snake.is_opposite_direction(event.key):
                                changed_direction = True
                                snake.direction = event.key
                                if snake.move(snake.direction, food=food):
                                    food = None

                    elif event.type == NEW_FOOD_EVENT and not food:
                        pygame.mixer.Sound.play(FOOD_APPEAR_SOUND)
                        pygame.mixer.music.stop()
                        food = Food()

                if not changed_direction and snake.move(snake.direction, food=food):
                    food = None

                if food:
                    food.draw()

                # Live high score display on top right
                high_score = get_high_score()
                font_live = pygame.font.Font(TEXT_FONT, 30)
                hs_text = font_live.render(f"HI: {max(high_score, snake.get_length())}", True, WHITE)
                hs_rect = hs_text.get_rect()
                hs_rect.topright = (display.get_width() - 20, 20)
                display.blit(hs_text, hs_rect)

                snake.show_score()
                pygame.display.update()

                clock.tick(snake.speed)
                score = snake.get_length()

        except GameOverException:
            keep_playing = show_game_over_screen(score)

    pygame.quit()

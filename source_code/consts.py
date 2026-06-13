import pygame

from PIL import Image


BACKGROUND_IMG = "./resources/background.jpg"
WINDOW_WIDTH, WINDOW_HEIGHT = Image.open(BACKGROUND_IMG).size

WHITE = (255, 255, 255)

SNAKE_COLOR = (255, 153, 51)
SNAKE_THICKNESS = 20
SNAKE_SPEED = 7
SPEED_GROWTH_CONST = 1.01
NODE_LENGTH = 40

NEW_FOOD_EVENT = pygame.USEREVENT + 1
MAX_FOOD_WIDTH = 60
MAX_FOOD_HEIGHT = 80
FOOD_TIME_INTERVAL = 800
FOOD_OPTIONS = ["./resources/chaike.png", "./resources/eitan.png",
                "./resources/eitan2.png", "./resources/lazer.png",
                "./resources/lazer2.png", "./resources/ron.png", "./resources/shumi.png"]

TEXT_FONT = 'freesansbold.ttf'

pygame.init()

display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.time.set_timer(NEW_FOOD_EVENT, FOOD_TIME_INTERVAL)
background = pygame.image.load(BACKGROUND_IMG)

clock = pygame.time.Clock()

EAT_SOUND = pygame.mixer.Sound("./resources/eat.wav")
FOOD_APPEAR_SOUND = pygame.mixer.Sound("./resources/mew.wav")

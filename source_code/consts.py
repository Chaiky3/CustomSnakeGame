import os
import pygame
from PIL import Image

# Directories and paths
RESOURCES_DIR = "./resources"
BACKGROUND_IMG = os.path.join(RESOURCES_DIR, "background.jpg")

# Default window dimensions if background is missing
DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600

if os.path.exists(BACKGROUND_IMG):
    try:
        WINDOW_WIDTH, WINDOW_HEIGHT = Image.open(BACKGROUND_IMG).size
    except Exception:
        WINDOW_WIDTH, WINDOW_HEIGHT = DEFAULT_WIDTH, DEFAULT_HEIGHT
else:
    WINDOW_WIDTH, WINDOW_HEIGHT = DEFAULT_WIDTH, DEFAULT_HEIGHT

# Colors
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

# Dynamically scan resources folder for food images (.png, .jpg, .jpeg), excluding background
FOOD_OPTIONS = []
if os.path.exists(RESOURCES_DIR):
    for filename in os.listdir(RESOURCES_DIR):
        file_path = os.path.join(RESOURCES_DIR, filename)
        if os.path.isfile(file_path):
            lower_name = filename.lower()
            if lower_name.endswith(('.png', '.jpg', '.jpeg')) and lower_name != "background.jpg":
                FOOD_OPTIONS.append(file_path)

TEXT_FONT = 'freesansbold.ttf'

pygame.init()

display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.time.set_timer(NEW_FOOD_EVENT, FOOD_TIME_INTERVAL)

# Background image setup with fallback
if os.path.exists(BACKGROUND_IMG):
    try:
        background = pygame.image.load(BACKGROUND_IMG)
    except Exception:
        background = None
else:
    background = None

clock = pygame.time.Clock()

# Sound assets with fallback
EAT_SOUND_PATH = os.path.join(RESOURCES_DIR, "eat.wav")
if os.path.exists(EAT_SOUND_PATH):
    try:
        EAT_SOUND = pygame.mixer.Sound(EAT_SOUND_PATH)
    except Exception:
        EAT_SOUND = None
else:
    EAT_SOUND = None

FOOD_APPEAR_SOUND_PATH = os.path.join(RESOURCES_DIR, "mew.wav")
if os.path.exists(FOOD_APPEAR_SOUND_PATH):
    try:
        FOOD_APPEAR_SOUND = pygame.mixer.Sound(FOOD_APPEAR_SOUND_PATH)
    except Exception:
        FOOD_APPEAR_SOUND = None
else:
    FOOD_APPEAR_SOUND = None

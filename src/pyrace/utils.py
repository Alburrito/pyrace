import os

# Get the absolute path to the `resources` directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_PATH = os.path.join(BASE_DIR, "resources", "img")
SOUND_PATH = os.path.join(BASE_DIR, "resources", "sound")

TITLE = "TURTLES RACE!"
SCREENWIDTH = 800
SCREENHEIGHT = 600

COLORS = ["red", "blue", "green", "yellow"]


def get_next_color():
    index = 0
    while True:
        yield COLORS[index]
        index = (index + 1) % len(COLORS)

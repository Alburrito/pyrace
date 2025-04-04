TITLE = "TURTLES RACE!"
SCREENWIDTH = 800
SCREENHEIGHT = 600

IMG_PATH = "resources/img"
SOUND_PATH = "resources/sound"

COLORS = ["red", "blue", "green", "yellow"]


def get_next_color():
    index = 0
    while True:
        yield COLORS[index]
        index = (index + 1) % len(COLORS)

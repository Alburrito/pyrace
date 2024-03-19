import colorama
colorama.init()

TITLE = "TURTLES RACE!"
SCREENWIDTH = 800
SCREENHEIGHT = 600

IMG_PATH = "resources/img"
SOUND_PATH = "resources/sound"

COLORS = ['red', 'blue', 'green', 'yellow']

def move_cursor(x, y):
    print("\x1b[{};{}H".format(y+1, x+1))


def clear():
    print("\x1b[2J")


def full_clear():
    clear()
    move_cursor(0, 0)


def get_next_color():
    index = 0
    while True:
        yield COLORS[index]
        index = (index + 1) % len(COLORS)

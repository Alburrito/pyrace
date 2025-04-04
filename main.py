##########################################################################
#                                pyrace                                  #
##########################################################################
#                                                                        #
#   Version: 0.1                                                         #
#                                                                        #
#   github: @Alburrito                                                   #
#   mail: almarlop.dev@gmail.com                                         #
#                                                                        #
##########################################################################

import signal
from typing import List
import getopt
from random import randint
import sys
import time
import turtle
from music_player import MusicPlayer

from runners import Runner, TurtleRunner
from utils import get_next_color, TITLE, IMG_PATH, SCREENWIDTH, SCREENHEIGHT

##########################################################################


class Race:

    def __init__(self, num_runners: int, race_length: int):
        """
        Initializes the class

        Args:
            (num_runners : int) The number of runners in the race
            (race_length : int) The length in meters of the race
        """
        # Race parameters
        self.num_runners: int = num_runners
        self.runners: List[Runner] = []
        self.positions: List[Runner] = []
        self.finished: bool = False

        # Right-Left and Top-Down margins. (Distances)
        self.rl_margin: int = SCREENWIDTH - race_length
        self.td_margin: int = 150
        # Track dimensions
        self.track_width: int = race_length
        self.track_height: int = SCREENHEIGHT - self.td_margin
        self.space_between_runners: int = int(
            self.track_height / (self.num_runners - 1)
        )
        # Track coordinates
        self.track_start: int = int(-self.track_width / 2)
        self.track_end: int = int(self.track_width / 2)

        # Screen
        self.screen = turtle.Screen()
        self.screen.setup(SCREENWIDTH, SCREENHEIGHT)
        # Screen settings
        self.screen.title(TITLE)
        self.screen.bgcolor("black")
        self.screen.bgpic(f"{IMG_PATH}/bg_shells.png")

        # Countdown images
        self.screen.register_shape(f"{IMG_PATH}/3.gif")
        self.screen.register_shape(f"{IMG_PATH}/2.gif")
        self.screen.register_shape(f"{IMG_PATH}/1.gif")
        self.screen.register_shape(f"{IMG_PATH}/go.gif")
        # Turtle images
        self.screen.register_shape(f"{IMG_PATH}/turtle_red.gif")
        self.screen.register_shape(f"{IMG_PATH}/turtle_yellow.gif")
        self.screen.register_shape(f"{IMG_PATH}/turtle_green.gif")
        self.screen.register_shape(f"{IMG_PATH}/turtle_blue.gif")

    def __start_countdown(self):
        """ """
        turtle.penup()
        turtle.goto(0, 0)
        # Play countdown music
        MusicPlayer.play_start_music()
        # Countdown animation
        for i in range(3, 0, -1):
            turtle.shape(f"{IMG_PATH}/{i}.gif")
            time.sleep(1)
            turtle.shape("blank")
        turtle.shape(f"{IMG_PATH}/go.gif")
        time.sleep(0.5)
        turtle.shape("blank")
        turtle.penup()

    def start(self):
        """ """
        # Define starting point
        x_start = self.track_start
        y_start = self.track_height / 2
        y = y_start

        # Create runners
        color_generator = get_next_color()
        for runner_id in range(1, self.num_runners + 1):
            runner_color = next(color_generator)
            runner = TurtleRunner(runner_id, color=runner_color, speed=5)
            runner.restart(x_start, y)
            y = y - self.space_between_runners
            self.runners.append(runner)

        # Create finish line
        turtle.penup()
        turtle.goto(self.track_end, self.track_height / 2)
        turtle.setheading(270)
        turtle.pendown()
        turtle.forward(self.track_height)
        turtle.penup()

        # Start countdown
        self.__start_countdown()

        # Start
        MusicPlayer.play_race_sound()
        while not self.finished:
            for runner in self.runners:
                # If the runner has not finished, advance randomly
                if not runner.finished:
                    #advance = randint(1, 5)
                    advance = randint(10, 15)
                    runner.advance(advance)
                    # If the runner is at the end of the track, finish
                    if runner.get_x() >= self.track_end:
                        runner.finished = True
                        self.positions.append(runner)
                        print(f"Runner {runner.runner_id} has finished!")
            self.finished = all(runner.finished for runner in self.runners)

        # Wait for all runners to finish
        MusicPlayer.stop_music()

        # Clear the screen but keep the turtles
        turtle.clear()
        for runner in self.runners:
            runner.runner.clear()
            runner.runner.penup()

        # Display "And the winner is..."
        turtle.goto(0, 0)
        turtle.setheading(0)
        turtle.pendown()
        turtle.color("black")
        turtle.write(
            "And the winner is...",
            align="center",
            font=("Arial", 24, "bold"),
        )

        # Play finish music
        MusicPlayer.play_finish_music()
        time.sleep(2.5)

        # Erase the winner message
        turtle.clear()

        # Display winner in the center of the screen
        self.winner = self.positions[0]
        self.winner.runner.goto(0, 0)
        # Display message a little above the winner
        turtle.penup()
        turtle.goto(0, 50)
        turtle.setheading(0)
        turtle.pendown()
        turtle.color("black")
        turtle.write(
            f"Runner {self.winner.runner_id}!",
            align="center",
            font=("Arial", 24, "bold"),
        )

        if len(self.positions) > 1:
            # Horizontal space between runners
            spacing = 400 // (len(self.positions) - 1)
            # X coordinate to start the runners, depending on the number of runners
            start_x = -200 + (len(self.positions) - 1) * spacing / 2
            # Y coorinate below the winner
            y_pos = -200 
            # Move the runners in order of finish
            for i, runner in enumerate(self.positions[1:]):
                x_pos = start_x + (i - 1) * spacing
                runner.runner.goto(x_pos, y_pos)
                turtle.penup()
                turtle.goto(x_pos, y_pos)

        # Play the crowd cheer sound
        MusicPlayer.play_crowd_cheer()
        turtle.done()


def handle_exit_signal(signum, frame):
    """
    Handles the CTRL+C signal to cleanly exit the program.
    """
    print("\nExiting program...")
    # Stop any playing music
    MusicPlayer.stop_music()
    # Close the Turtle graphics window
    turtle.bye()
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, handle_exit_signal)


def main(argv):
    # Default parameters
    num_runners = 4
    track_size = 700

    race = Race(num_runners, track_size)
    race.start()


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        handle_exit_signal(None, None)

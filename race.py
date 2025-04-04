import time
import turtle
from random import randint
from typing import List
from music_player import MusicPlayer
from runners import TurtleRunner
from utils import get_next_color, TITLE, IMG_PATH, SCREENWIDTH, SCREENHEIGHT


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
        self.runners: List[TurtleRunner] = []
        self.positions: List[TurtleRunner] = []
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
        self.screen.title(TITLE)
        self.screen.bgcolor("black")
        self.screen.bgpic(f"{IMG_PATH}/bg_shells.png")

        turtle.hideturtle()

        # Countdown images
        self.__register_images()

    def __register_images(self):
        """Registers the images used in the race."""
        self.screen.register_shape(f"{IMG_PATH}/3.gif")
        self.screen.register_shape(f"{IMG_PATH}/2.gif")
        self.screen.register_shape(f"{IMG_PATH}/1.gif")
        self.screen.register_shape(f"{IMG_PATH}/go.gif")
        self.screen.register_shape(f"{IMG_PATH}/turtle_red.gif")
        self.screen.register_shape(f"{IMG_PATH}/turtle_yellow.gif")
        self.screen.register_shape(f"{IMG_PATH}/turtle_green.gif")
        self.screen.register_shape(f"{IMG_PATH}/turtle_blue.gif")

    def __start_countdown(self):
        """Displays the countdown before the race starts."""
        turtle.showturtle()
        turtle.penup()
        turtle.goto(0, 0)
        MusicPlayer.play_start_music()
        for i in range(3, 0, -1):
            turtle.shape(f"{IMG_PATH}/{i}.gif")
            time.sleep(1)
            turtle.shape("blank")
        turtle.shape(f"{IMG_PATH}/go.gif")
        time.sleep(1)
        turtle.shape("blank")
        turtle.penup()
        turtle.hideturtle()

    def __create_runners(self):
        """Creates the runners and positions them at the starting line."""
        x_start = self.track_start
        y_start = self.track_height / 2
        y = y_start

        color_generator = get_next_color()
        for runner_id in range(1, self.num_runners + 1):
            runner_color = next(color_generator)
            runner = TurtleRunner(runner_id, color=runner_color, speed=5)
            runner.restart(x_start, y)
            y -= self.space_between_runners
            self.runners.append(runner)

    def __create_finish_line(self):
        """Draws the finish line on the track."""
        turtle.penup()
        turtle.goto(self.track_end, self.track_height / 2)
        turtle.setheading(270)
        turtle.pendown()
        turtle.forward(self.track_height)
        turtle.penup()

    def __run_race(self):
        """Runs the race until all runners finish."""
        MusicPlayer.play_race_sound()
        while not self.finished:
            for runner in self.runners:
                if not runner.finished:
                    advance = randint(1, 5)
                    runner.advance(advance)
                    if runner.get_x() >= self.track_end:
                        runner.finished = True
                        self.positions.append(runner)
                        print(f"Runner {runner.runner_id} has finished!")
            self.finished = all(runner.finished for runner in self.runners)
        MusicPlayer.stop_music()

    def __display_positions(self):
        """Displays the winner and the rest of the runners in order."""
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
        turtle.hideturtle()

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
        time.sleep(20)

    def start(self):
        """Starts the race."""
        self.__create_runners()
        # self.__create_finish_line()
        self.__start_countdown()
        self.__run_race()
        self.__display_positions()
        # Close the turtle graphics window
        self.screen.bye()
        # Close the music player
        MusicPlayer.stop_music()

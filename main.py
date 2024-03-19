##########################################################################
#                                pyrace                                  #
##########################################################################
#                                                                        #
#   Version: 0.1                                                         #
#                                                                        #
#   github: @Alburrito                                                   #
#   mail: almarlop98@gmail.com                                           #
#                                                                        #
##########################################################################
#                                                                        #
#   TODO:                                                                #
#       · Background                                                     #
#       · Personalized turtles                                           #
#       · Basic working                                                  #
#       · resources.py                                                   #
#                                                                        #
##########################################################################

from typing import List
import getopt
from random import randint
import sys
import time
import turtle

from runners import Runner, TurtleRunner
from utils import get_next_color, TITLE, IMG_PATH, SOUND_PATH, SCREENWIDTH, SCREENHEIGHT

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
        self.finished: bool = False

        # Right-Left and Top-Down margins. (Distances)
        self.rl_margin: int = SCREENWIDTH - race_length
        self.td_margin: int = 150
        # Track dimensions
        self.track_width: int = race_length
        self.track_height: int = SCREENHEIGHT - self.td_margin
        self.space_between_runners: int = int(self.track_height / (self.num_runners - 1))
        # Track coordinates
        self.track_start: int = int(-self.track_width/2)
        self.track_end:int = int(self.track_width/2)

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
        """
        """
        for i in range(3, 0, -1):
            turtle.shape(f"{IMG_PATH}/{i}.gif")
            time.sleep(1)
            turtle.shape("blank")
        turtle.shape(f"{IMG_PATH}/go.gif")
        time.sleep(0.5)
        turtle.shape("blank")

    def start(self):
        """
        """
        # Define starting point
        x_start = self.track_start
        y_start = self.track_height/2
        y = y_start

        # Create runners
        color_generator = get_next_color()
        for runner_id in range(1, self.num_runners+1):
            runner_color = next(color_generator)
            runner = TurtleRunner(runner_id, color=runner_color)
            runner.restart(x_start, y)
            y = y - self.space_between_runners
            self.runners.append(runner)
        
        time.sleep(1)
        
        # Start countdown
        self.__start_countdown()

        # Start
        while not self.finished:
            for runner in self.runners:
                # If the runner has not finished, advance randomly
                if not runner.finished:
                    advance = randint(1, 5)
                    runner.advance(advance)
                    # If the runner is at the end of the track, finish
                    if runner.get_x() >= self.track_end:
                        runner.finished = True
                        print(f"Runner {runner.runner_id} has finished!")
            self.finished = all(runner.finished for runner in self.runners)

        turtle.done()

def main(argv):
    # Default parameters
    num_runners = 4
    track_size = 700

    try:
        opts, _ = getopt.getopt(argv, "n:t:")

        for opt, arg in opts:
            if opt in ("-n"):  # num_runners
                num_runners = int(arg)
            elif opt in ("-t"):  # track_size
                track_size = int(arg)
    except Exception:
        print("Something went wrong handling arguments")
        exit(0)

    race = Race(num_runners, track_size)
    race.start()

if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt as err:
        print("\nProgram interrupted by user. Exiting...\n")
        exit(0)

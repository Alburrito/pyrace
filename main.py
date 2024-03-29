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
from random import choice, randint
import sys
import time
import turtle

from constants import COLORS
from runners import Runner

##########################################################################


class Race:

    SCREENWIDTH = 800
    SCREENHEIGTH = 600
    TITLE = "TURTLES RACE!"
    BG_IMG_PATH = "resources/bg_no_shells.png"
   
    def __init__(self, num_runners: int, race_length: int):
        """
        Initializes the class

        Args:
            (num_runners : int) The number of runners in the race
            (race_length : int) The length in meters of the race
        """
        self.num_runners: int = num_runners
        self.runners: List[Runner] = []
        self.finished: bool = False

        # Right-Left and Top-Down margins. (Distances)
        self.rl_margin: int = self.SCREENWIDTH - race_length
        self.td_margin: int = 150
        # Track dimensions
        self.track_width: int = race_length
        self.track_height: int = self.SCREENHEIGTH - self.td_margin
        self.space_between_runners: int = int(self.track_height / (self.num_runners - 1))
        # Track coordinates
        self.track_start: int = int(-self.track_width/2)
        self.track_end:int = int(self.track_width/2)
        
    def __create_screen(self):
        """
        """
        self.screen = turtle.Screen()
        self.screen.setup(self.SCREENWIDTH, self.SCREENHEIGTH)
        # Countdown images
        self.screen.register_shape("resources/3.gif")
        self.screen.register_shape("resources/2.gif")
        self.screen.register_shape("resources/1.gif")
        self.screen.register_shape("resources/go.gif")
        # Screen settings
        self.screen.title(self.TITLE)
        self.screen.bgcolor("black")
        self.screen.bgpic(self.BG_IMG_PATH)
    
    def __start_countdown(self):
        """
        """
        for i in range(3, 0, -1):
            print(i)
            turtle.shape(f"resources/{i}.gif")
            time.sleep(1)
            turtle.shape("blank")
        turtle.shape(f"resources/go.gif")
        print("GO!")
        time.sleep(0.5)
        turtle.shape("blank")

    def start(self):
        """
        """
        self.__create_screen()

        x_start = self.track_start
        y_start = self.track_height/2
        y = y_start

        # Create runners
        for runner_id in range(1, self.num_runners+1):
            runner_color = choice(COLORS)
            runner = Runner(runner_id, color=runner_color)
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

        turtle.mainloop()

def main(argv):
    # Default parameters
    num_runners = 5
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

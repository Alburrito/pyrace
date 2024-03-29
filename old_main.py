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



from random import randint, choice
from signal import signal, SIGINT
import sys
from sys import exit
import getopt
from os import path
import time

import turtle

from runners import *
from constants import *


SCREENWIDTH = 2000
SCREENHEIGTH = 700

##########################################################################


class Race:
   
    def __init__(self, num_runners, race_length, results_path, loop):
        """
        Initializes the class

        Args:
            (num_runners : int) The number of runners in the race
            (race_length : int) The length in meters of the race
            (results_path : str) Path to the file where we want to
                                store the results
            (loop : bool) True if endless races.
        """
        self.num_runners = int(num_runners)
        self.race_length = int(race_length)
        self.results_path = results_path
        self.loop = loop

        self.runners = []

        self.finished = 0
        self.results = []

    def __create_screen(self):
        """

        """
        self.screen = turtle.Screen()
        self.screen.setup(SCREENWIDTH, SCREENHEIGTH)
       # self.screen.cv.__rootwindow.resizable(False,False)
        self.screen.bgcolor("black")
        # NOTA: Creo que hay una ventana y dentro un canvas
        self.screen.bgpic("resources/conConchas.png")

    def __restart(self, x_start):
        """

        """
        self.finished = 0
        time.sleep(1)
        self.screen.clear()

        for runner in self.runners:
            runner.restart(x_start, runner.get_y())

    def start(self):
        """

        """
        positions = []
        times = []
        start_time = time.time()

        self.__create_screen()

        x_start = -self.screen.screensize()[0]
        y_start = self.screen.screensize()[1]
        y = y_start


        # Create runners
        for i in range(1,self.num_runners+1):
            runner_color = choice(COLORS)
            runner = Runner(i, color=runner_color) # speed=, color=
            runner.restart(x_start, y)
            y = y - (self.screen.screensize()[1]*2)/(self.num_runners - 1)
            self.runners.append(runner)

        time.sleep(3)

        while self.finished < self.num_runners:
            # Get random id and advance randomly
            runner_id = randint(0,self.num_runners-1)
            if self.runners[runner_id].finished:
                continue
            else:
                self.runners[runner_id].advance(randint(1,3))
                if self.runners[runner_id].get_x() >= self.screen.screensize()[0]: # Finished runner
                    self.runners[runner_id].finished = True
                    self.finished += 1
                
                if self.finished == self.num_runners: # Finished race
                    if self.loop:
                        self.__restart(x_start)
            
    def handler(self, signal_received, frame):
        """
        Handles what the program should do when it receives SIGINT (ctrl+C)
        """
        utils.full_clear()
        if len(self.results) != 0:
            if self.results_path != "":
                try:
                    self.__save_results()
                except Exception:
                    print("""\nERROR:{} Wrong path to results file. Could not
                          save results file.""".format(self.results_path))
        print("\nSEE YOU SOON!\n")
        exit(0)

def main(argv):
    # Default parameters
    num_runners = 5
    track_size = 100
    loop = False
    save_path = ""

    try:
        opts, args = getopt.getopt(argv, "n:t:ls:f")

        for opt, arg in opts:
            if opt in ("-l"):  # loop
                loop = True
            elif opt in ("-n"):  # num_runners
                num_runners = arg
            elif opt in ("-t"):  # track_size
                track_size = arg
            elif opt in ("-s"):  # Save results
                save_path = arg
            elif opt in ("-f"):  # Fast start (testing comfort)
                loop = True
                # TODO: check path dir
                #save_path = "results/fast_results.txt"

    except Exception:
        print("Something went wrong handling arguments")
        exit(0)

    race = Race(num_runners, track_size, save_path, loop)
   # signal(SIGINT, race.handler)
    race.start()

if __name__ == '__main__':
    main(sys.argv[1:])

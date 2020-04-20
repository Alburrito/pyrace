from random import randint
import time
from signal import signal, SIGINT
import sys, getopt
from sys import exit
from os import path

from runners import Runner
import utils


class Race:
    
    def __init__(self, num_runners, race_length, results_path, loop):
        """
        Initializes the class
        
        Args:
            (num_runners : int) The number of runners in the race
            (race_length : int) The length in meters of the race
            (results_path : str) Path to the file where we want to store the results
            (loop : bool) True if endless races.
        """
        self.num_runners = int(num_runners)
        self.race_length = int(race_length)
        self.results_path = results_path
        self.loop = loop
        
        self.runners = []
        self.tracks = []
        
        self.finished = 0
        self.results = []
        

    def __create_race(self):
        """
        Restart the runners and their respective tracks
        """
        for runner in range(0, self.num_runners):
            self.runners.append(Runner(runner, self.race_length))
            self.tracks.append([])
            # View
            for i in range(0,self.race_length):
                self.tracks[runner].append("_")
                
    def __print_track(self,track):
        """
        Shows the status of the track provided as an argument
        
        Args:
            (track : list) The list that makes the visual representation of the track
        """
        for i in track:
            print(i, end='')
        print("")
    
    def __start_race(self):
        """
        A race that lasts until all the runners reach the finish begins 
        """
        positions = []
        times = []
        start_time = time.time()
        
        while (self.finished < self.num_runners):
            randID = randint(0, self.num_runners-1)
            progress = self.runners[randID].advance()
            self.tracks[randID][progress-1] = "#"
            
            if progress == self.race_length:
                positions.append(randID)
                times.append(time.time()-start_time)
                self.finished += 1
            else:
                #VISTA
                utils.full_clear()
                for track in self.tracks:
                    self.__print_track(track)
             
            time.sleep(0.05)
        
        #VISTA
        utils.full_clear()
        for track in self.tracks:
            self.__print_track(track)

        
        result = {
            'positions' : positions,
            'times' : times
        }
        
        self.results.append(result)
            
    def __save_results(self):
        """
        Saves the results of all races on the specified route
        """
        print("\nSaving results in: " + self.results_path + "\n")
        
        with open(self.results_path, 'w') as results_file:
            num_carrera = 0
            for result in self.results:
                num_carrera += 1
                pos = 0
                results_file.write("           RACE " + str(num_carrera)+" ("+ str(self.race_length)+"m)"+"\n")
                results_file.write("------------------------\n")
                results_file.write("POSITION".ljust(10) + "RUNNER".ljust(9) + "TIME\n")
                for p,t in zip(result['positions'], result['times']):
                    pos += 1
                    results_file.write((str(pos)+"º").center(7) + str(p).center(12) + str(t)[:5] + "\n")
                results_file.write("\n\n")
                

    def __restart(self):
        """
        Restarts the race
        """
        self.finished = 0
        for runner in self.runners:
            runner.restart()
            #View
            self.tracks[runner.id] = []
            for i in range(0,self.race_length):
                self.tracks[runner.id].append("_")
        self.__start_race()
        
    def start(self):
        """
        
        """
        self.__create_race()
        self.__start_race()
        
        if self.loop == True:
            while True:
                self.__restart()
        else:
            utils.full_clear()
            if self.results_path != "":
                try:
                    self.__save_results()
                except:
                    print("ERROR: Wrong path to results file. Could not save results file.")
            
    def handler(self,signal_received, frame):
        """
        Handles what the program should do when it receives SIGINT (ctrl+C)
        """
        utils.full_clear()
        if len(self.results) != 0:
            if self.results_path != "":
                try:
                    self.__save_results()
                except:
                    print("\nERROR:{} Wrong path to results file. Could not save results file.".format(self.results_path))
        print("\nSEE YOU SOON!\n")
        exit(0)



def main(argv):
    # Default parameters
    num_runners = 3
    track_size = 100
    loop = False
    path = ""
    
    try: 
        opts, args = getopt.getopt(argv,"n:t:ls:f")
        
        for opt, arg in opts:
            if opt in ("-l"): # loop
                loop = True
            elif opt in ("-n"): # num_runners
                num_runners = arg
            elif opt in ("-t"): # track_size
                track_size = arg
            elif opt in ("-s"): # Save results
                path = arg
            elif opt in ("-f"): # Fast start (testing comfort)
                track_size = 25
                loop = True
                path = "results/fast_results.txt"
                
    except:
        print("Something went wrong handling arguments")
        exit(0)
        
    race = Race(num_runners, track_size, path, loop)
    signal(SIGINT, race.handler)
    race.start()
    
if __name__ == '__main__':
    main(sys.argv[1:])
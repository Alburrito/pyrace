from random import randint
import time
from signal import signal, SIGINT
from sys import exit

from runners import Runner


class Race:
    
    def __init__(self, num_runners, race_length):
        """
        Initializes the class
        
        Args:
            (num_runners : int) The number of runners in the race
            (race_length : int) The length in meters of the race
        """
        self.num_runners = num_runners
        self.race_length = race_length
        
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
                for track in self.tracks:
                    self.__print_track(track)
                print("\n\n\n\n")
             
            time.sleep(0.05)
        
        result = {
            'positions' : positions,
            'times' : times
        }
        
        self.results.append(result)
            
    def __save_results(self, path):
        """
        Saves the results of all races on the specified route
        
        Args:
            (path : str) Indicates the file path where you want to save the results. Needs a file name
        """
        with open(path, 'w') as results_file:
            num_carrera = 0
            for result in self.results:
                num_carrera += 1
                pos = 0
                results_file.write("           RACE " + str(num_carrera)+"\n")
                results_file.write("------------------------\n")
                results_file.write("POSITION".ljust(10) + "RUNNER".ljust(9) + "TIME\n")
                for p,t in zip(result['positions'], result['times']):
                    pos += 1
                    results_file.write((str(pos)+"º").center(7) + str(p).center(12) + str(t)[:5] + "\n")
                results_file.write("\n\n")
                

    def restart(self):
        """
        Restarts the race
        """
        self.finished = 0
        self.runners = []
        self.tracks = []
        self.__create_race()
        self.__start_race()
        
    def handler(self,signal_received, frame):
        """
        Handles what the program should do when it receives SIGINT (ctrl+C)
        """
        self.__save_results('results.txt')
        print("\nSEE YOU SOON!\n")
        exit(0)



def main():
    race = Race(3, 20)
    signal(SIGINT, race.handler)
    while(True):
        race.restart()
    
    
    
if __name__ == '__main__':
    main()
from random import randint
import time

from runners import Runner


class Race:
    
    def __init__(self, num_runners, race_length):
        self.num_runners = num_runners
        self.race_length = race_length
        self.runners = []
        self.finished = 0
        #Tiempos

    def start(self):
        
        array1 = []
        array2 = []
        array3 = []
        for i in range(0,self.race_length):
            array1.append("_")
            array2.append("_")
            array3.append("_")
        
        # Create runners
        for i in range(0, self.num_runners):
            self.runners.append(Runner(i, self.race_length))

        # RUN
        while (self.finished < self.num_runners):
            randID = randint(0, self.num_runners-1)
            progress = self.runners[randID].advance()
            
            if progress == self.race_length:
                self.finished += 1
                
            # Actualizar vista  
            if randID == 0:
                print(randID, progress-1)
                array1[progress-1]= "#"
            elif randID == 1:
                print(randID, progress-1)
                array2[progress-1]= "#"
            else:
                print(randID, progress-1)
                array3[progress-1]= "#"
            pistadebug(array1)
            pistadebug(array2)
            pistadebug(array3)
                    
            print("\n\n\n\n")
                
            time.sleep(0.05)
            

    def restart(self):
        self.finished = 0
        #tiempos
        

def pistadebug(array):
    for i in array:
        print(i, end='')
    print("")

def main():
    
    race = Race(3, 100)
    race.start()
    
    
    
    
    
if __name__ == '__main__':
    main()
class Runner:
    
    def __init__(self, id, race_length, speed = 0, color = 0):
        
        self.id = id
        self.race_length = race_length
        self.speed = speed
        self.color = color
        self.progress = 0
        self.finished = False
    
    def advance(self):
        if self.progress < self.race_length:    
            self.progress += 1
            if self.progress == self.race_length:
                self.finished = True
            return self.progress
        else:
            if self.finished == True:
                return -1
            
    def restart(self):
        self.progress = 0
        
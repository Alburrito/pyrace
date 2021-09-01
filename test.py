import time
from random import randint 
runners = 5


class Father():

    def __init__(self, p1):
        self.p1 = p1
        self.test = "testeo"


class Child(Father):
    def __init__(self,p1):
        super()
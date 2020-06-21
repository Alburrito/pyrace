from turtle import Turtle

class Runner:

    def __init__(self, runner_id, speed=0, color='black'):
        self.runner_id = runner_id
        self.runner= Turtle()
        self.runner.speed(speed)
        self.runner.color = color

    def advance(self, length):
        self.runner.forward(length)

    def restart(self, x, y):
        self.runner.goto(x,y)

    def get_x(self):
        return self.runner.xcor()
    
    def get_y(self):
        return self.runner.ycor()

    
from turtle import Turtle
from .utils import IMG_PATH


class Runner:

    def __init__(self, runner_id: int, speed=0, color="black"):
        self.runner_id = runner_id
        self.finished = False
        self.runner = Turtle()
        self.runner.speed(speed)
        self.runner.color(color)
        self.runner.shape("turtle")

    def advance(self, length: int):
        self.runner.forward(length)

    def restart(self, x, y):
        self.finished = False
        self.runner.penup()
        self.runner.goto(x, y)
        self.runner.pendown()

    def get_x(self):
        return self.runner.xcor()

    def get_y(self):
        return self.runner.ycor()


class TurtleRunner(Runner):

    def __init__(self, runner_id, speed=0, color="red"):
        super().__init__(runner_id, speed, color)
        self.runner.shape(f"{IMG_PATH}/turtle_{color}.gif")

import time
import turtle
from turtle import Turtle
from random import randint

window = turtle.Screen()
window.title = "Carrera de tortugas"

t1 =  Turtle()
t1.speed(0)
t1.color("red")
t1.shape("turtle")
t1.penup()
t1.goto(-250,100)  
t1.pendown()

t2 =  Turtle()
t2.speed(0)
t2.color("blue")
t2.shape("turtle")
t2.penup()
t2.goto(-250,50)  
t2.pendown()

t3 =  Turtle()
t3.speed(0)
t3.color("green")
t3.shape("turtle")
t3.penup()
t3.goto(-250,0)  
t3.pendown()

time.sleep(1)

for _ in range(145):
    t1.forward(randint(1,5))
    t2.forward(randint(1,5))
    t3.forward(randint(1,5))
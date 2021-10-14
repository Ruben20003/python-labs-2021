import turtle
import random

turtle.speed(0)

while True:
    a= random.random() * 30
    b= random.random() * 360
    turtle.forward(a)
    turtle.left(b)



import turtle as t
import math


def draw_half_circ(a):
    a = a * 0.01
    n = 60
    phi = 360 / n
    for i in range(n//2):
        t.forward(a)
        t.left(phi)


t.penup()
t.backward(200)
t.pendown()

t.right(90)

while True:
    draw_half_circ(500)
    draw_half_circ(200)

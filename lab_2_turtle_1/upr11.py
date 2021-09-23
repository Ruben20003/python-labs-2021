import turtle as t
import math


def draw_circ(a):
    a = a * 0.01
    n = 60
    phi = 360 / n
    for i in range(n):
        t.forward(a)
        t.left(phi)


r = 300
dr = 100
while True:
    draw_circ(r)
    t.left(180)
    draw_circ(r)
    t.left(180)
    r += dr

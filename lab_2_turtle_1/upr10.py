import turtle as t
import math

t.speed(200000)

def draw_circ(a):
    a = a * 0.01
    n = 60
    phi = 360 / n
    for i in range(n):
        t.forward(a)
        t.left(phi)

N = 12

for i in range(N):
    draw_circ(1000)
    t.left(360/N)

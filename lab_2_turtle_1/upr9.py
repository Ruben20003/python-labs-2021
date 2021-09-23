import turtle as t
import math

def draw_poly(n, r):

    b = math.pi * (1 - 2 / n) / 2

    a = 2 * r * math.sin(math.pi / n)
    phi = 360 / n

    t.penup()
    t.goto(-r * math.cos(b), -r * math.sin(b))

    t.pendown()


    for i in range(n):
        t.forward(a)
        t.left(phi)

for i in range(1, 11):
    draw_poly(i + 2, i * 20)

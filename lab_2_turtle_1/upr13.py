import turtle as t
import math

def draw_circ(r):
    n = 60
    phi = 360 / n
    a = 2 * r * math.sin(math.pi / n)

    for i in range(n):
        t.forward(a)
        t.left(phi)

def draw_half_circ(r):
    n = 60
    phi = 360 / n
    a = 2 * r * math.sin(math.pi / n)

    for i in range(n//2):
        t.forward(a)
        t.left(phi)

t.speed(25)

t.penup()
t.goto(0, -200)
t.pendown()
t.begin_fill()
draw_circ(200)
t.color("#ffff00")
t.end_fill()

t.penup()
t.goto(100, 70)
t.pendown()
t.color("#000000")
t.begin_fill()
draw_circ(20)
t.color("#00ff00")
t.end_fill()

t.penup()
t.goto(-90, 70)
t.pendown()
t.color("#000000")
t.begin_fill()
draw_circ(20)
t.color("#00ff00")
t.end_fill()

t.penup()
t.goto(-90, -30)
t.pendown()
t.right(90)
t.color("#ff0000")
t.width(30)
draw_half_circ(100)

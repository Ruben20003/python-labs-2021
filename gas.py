import random as r
import turtle as t

N = 10
T = 0.2


pool = [t.Turtle(shape='circle') for _ in range(N)]
vx = [r.random() * 100 - 50 for _ in range(N)]
vy = [r.random() * 100 - 50 for _ in range(N)]
x = [r.randint(-400, 400)  for _ in range(N)]
y = [r.randint(-400, 400)  for _ in range(N)]

t.penup()
t.speed(0)
t.goto(-400, -400)
t.pendown()
t.goto(-400, 400)
t.goto(400, 400)
t.goto(400, -400)
t.goto(-400, -400)


for i, unit in enumerate(pool):
    unit.penup()
    unit.speed(0)
    unit.goto(x[i], y[i])


while True:
    for i in range(N):
        x[i] += vx[i] * T
        y[i] += vy[i] * T

        if x[i] >= 400 or x[i] <= -400:
            x[i] = 800 * (x[i] >= 400) - 400
            vx[i] *= -1

        if y[i] >= 400 or y[i] <= -400:
            y[i] = 800 * (y[i] >= 400) - 400
            vy[i] *= -1

        pool[i].goto(x[i], y[i])

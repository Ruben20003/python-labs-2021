import turtle

x = 0
y = 0
vx = 40
vy = 20
g = 10
dt = 0.01
t = 0

while True:
    vy -= g * dt
    t += dt
    x += vx * dt
    y += vy * dt - g * (dt ** 2) /2

    turtle.goto(x,y)
    if vy <= -20:
        vy = -1 * vy



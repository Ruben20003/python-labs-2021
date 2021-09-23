import turtle as t

def draw_star(n, a):
    for i in range(n):
        t.forward(a)
        t.left(180 - 180/n)

t.left(180)
draw_star(5, 200)

t.penup()
t.goto(200, 0)
t.pendown()

draw_star(11, 200)

import turtle as t

for i in range(10):
    koxm = 30*(i+1)
    for j in range(4):
        t.forward(koxm)
        t.left(90)
    t.penup()
    t.right(135)
    t.forward(15 * (2 ** 0.5))
    t.left(135)
    t.pendown()

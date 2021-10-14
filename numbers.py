import turtle

def draw(number, side=30):
    turtle.penup()
    x0, y0 = turtle.pos()

    coords = [(x0, y0           ), (x0 + side, y0           ),
              (x0, y0 -     side), (x0 + side, y0 -     side),
              (x0, y0 - 2 * side), (x0 + side, y0 - 2 * side)]

    def goto(cell):
        turtle.goto(*coords[cell - 1])

    goto(number[0])
    turtle.pendown()

    for el in number:
        goto(el)

    turtle.penup()
    goto(1)
    turtle.pendown()

font = [(1, 2, 6, 5, 1),
        (3, 2, 6),
        (1, 2, 4, 5, 6),
        (1, 2, 3, 4, 5),
        (1, 3, 4, 2, 6),
        (2, 1, 3, 4, 6, 5),
        (2, 3, 5, 6, 4, 3),
        (1, 2, 3, 5),
        (1, 5, 6, 2, 1, 3, 4),
        (4, 3, 1, 2, 4, 5)]

number = list(map(int,list(input())))

for i in number:
    draw(font[i])
    turtle.penup()
    turtle.forward(60)
    turtle.pendown()

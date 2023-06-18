import turtle


turtle.register_shape("outline_red.gif")


a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27 = turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(),

lis = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27]


b1, b2, b3, b4, b5, b6, b7, b8 = turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(),
lis1 = [b1, b2, b3, b4, b5, b6, b7, b8]

turtle.colormode(255)

for i in lis:
    i.hideturtle()
    i.shape("square")
    i.color((173, 216, 230))
    i.shapesize(3.8, 3.8)
    i.speed(0)
    i.penup()
    i.goto(1100, 1100)
    i.showturtle()


for i in lis1:
    i.hideturtle()
    i.shape("outline_red.gif")
    i.speed(0)
    i.penup()
    i.goto(1100, 1100)
    i.showturtle()

import turtle
screen= turtle.Screen()
screen.setup(500,500)
screen.title("Setup/test")
screen.bgcolor("yellow")

canvas= turtle.Turtle()
canvas.fillcolor("green")
canvas.begin_fill()
for i in range(4):
    canvas.forward(100)
    canvas.right(90)
canvas.end_fill()
turtle.done()
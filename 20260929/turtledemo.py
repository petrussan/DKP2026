import turtle

def drawrectangle(pena,size):
    for l in range(4):
        pena.forward(size)
        pena.left(90)

def drawstar(pena,color):
    pena.color(color)
    pena.begin_fill()
    for i in range(5):
        pena.forward(50)
        pena.right(144)
    pena.end_fill()

layar = turtle.Screen()
layar.title("Drawing Canvas")
layar.bgcolor("lightblue")
layar.setup(width=1000,height=600)
pena = turtle.Turtle()

# for l in range(4):
#     pena.forward(100)
#     pena.left(90)

drawrectangle(pena,200)
drawrectangle(pena,100)
pena.penup()
pena.backward(200)
pena.pendown()
drawstar(pena,"Blue")
pena.hideturtle()

turtle.done()
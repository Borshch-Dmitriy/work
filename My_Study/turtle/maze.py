import turtle

def star(side):
    for _ in range(20):
        turtle.forward(side)
        turtle.right(90)
        side = side - 10

star(200)
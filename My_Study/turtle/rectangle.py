# Rectangle

import turtle

def rectangle(width, height):
    turtle.showturtle()
    for _ in range(2):
        turtle.forward(height)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)

width = int(input())
heigth = int(input())

rectangle(width, heigth)
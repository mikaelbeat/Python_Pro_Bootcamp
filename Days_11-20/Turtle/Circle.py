
import turtle as t
import random
from turtle import Screen, Turtle

turtle1 = Turtle()

turtle1.shape("turtle")
turtle1.pensize(5)
turtle1.speed("fastest")
t.colormode(255)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def draw_spirogarph(size_of_the_gap):
    for _ in range(int(360 / size_of_the_gap)):
        turtle1.color(random_colour())
        turtle1.circle(100)
        turtle1.setheading(turtle1.heading() + 10)
        turtle1.circle(100)

draw_spirogarph(5)

screen = Screen()
screen.exitonclick()

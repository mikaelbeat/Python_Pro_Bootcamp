
import turtle as t
import random
from turtle import Screen, Turtle

turtle1 = Turtle()

turtle1.shape("turtle")
turtle1.pensize(5)
turtle1.speed(10)
t.colormode(255)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


directions = [0,
              90,
              180,
              270]


moves = [turtle1.forward,
         turtle1.backward]


for _ in range(50):
    turtle1.pencolor(random_colour())
    direction = random.choice(directions)
    turtle1.setheading(direction)
    move = random.choice(moves)
    move(50)



screen = Screen()
screen.exitonclick()


print(random_colour)
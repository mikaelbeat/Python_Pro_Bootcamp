
from turtle import Turtle, Screen

turtle = Turtle()

turtle.shape("turtle")
turtle.color("red")


# Square
# for _ in range(4):
#     turtle.forward(100)
#     turtle.right(90)


# Dashed line
for _ in range(10):
    turtle.forward(20)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()




screen = Screen()
screen.exitonclick()

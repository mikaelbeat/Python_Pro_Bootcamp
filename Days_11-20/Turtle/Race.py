
from turtle import Turtle, Screen
import random
import turtle

race_is_on = False

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?" )
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

initial_y = 110

for color in colors:
    new_turtle = Turtle("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    initial_y -= 30
    new_turtle.goto(x=-220, y=initial_y)
    turtles.append(new_turtle)
    
if bet:
    race_is_on = True
    
while race_is_on:
    for turtle in turtles:
        if turtle.xcor() > 210:
            race_is_on = False
            winner_color = turtle.pencolor()
            if winner_color == bet:
                print(f"You've won, {winner_color} turtle is the winner!")
            else:
                print(f"You've lost, {winner_color} turtle is the winner!")
        movement = random.randint(0, 10)
        turtle.forward(movement)


screen.exitonclick()

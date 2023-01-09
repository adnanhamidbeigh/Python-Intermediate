from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "pink", "purple"]
y_positions = ["-70", "-40", "-10", "20", "50", "80"]
all_turtles = []
is_running = False


for turtle_index in range(0, 6):   
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=float(y_positions[turtle_index]))
    all_turtles.append(new_turtle)


if user_bet:
    is_running = True

while is_running:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_running = False

            winning_colour = turtle.pencolor()

            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner!")
                
        rand_distance = random.randint(0, 10)
        turtle.fd(rand_distance)

screen.exitonclick()
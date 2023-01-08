import random
import turtle as t
t.colormode(255)

# import colorgram
# colours = colorgram.extract("image.jpg", 10)
# rgb_colours = []
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     rgb_colours.append((r, g, b))
colour_list = [(241, 234, 215), (242, 229, 238), (224, 239, 231), (191, 166, 121), (142, 165, 189),
               (136, 94, 57), (63, 100, 135), (219, 207, 130), (13, 23, 55)]
tim = t.Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.seth(225)
tim.forward(300)
tim.seth(0)
tim.pendown()
no_of_dots = 100

for dot_count in range(1, no_of_dots + 1):
    tim.pendown()
    tim.dot(20, random.choice(colour_list))
    tim.penup()
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.penup()
        tim.seth(90)
        tim.fd(50)
        tim.left(90)
        tim.fd(500)
        tim.seth(0)
screen = t.Screen()
screen.exitonclick()

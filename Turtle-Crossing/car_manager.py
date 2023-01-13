import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_increment = 0
    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(350, random_y)
            self.cars.append(new_car)

    def move_cars(self):
        for cars in self.cars:
            cars.backward(STARTING_MOVE_DISTANCE + self.move_increment)

    def increase_speed(self):
        self.move_increment += MOVE_INCREMENT
from turtle import Turtle
import random
COLORS = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle()
        new_car.shape('square')
        new_car.penup()
        new_car.color(COLORS[random.randint(0, 5)])
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.goto(300, random.randint(-250, 250))
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.speed)

    def faster(self):
        self.speed += MOVE_INCREMENT



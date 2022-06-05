from turtle import Turtle
import random
COLORS = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color(COLORS[random.randint(0, 5)])
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(280, random.randrange(-220, 220, 20))

    def move(self):
        self.back(STARTING_MOVE_DISTANCE)



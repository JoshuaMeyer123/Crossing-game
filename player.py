from turtle import Turtle
from scoreboard import Scoreboard
from car_manager import CarManager

START_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

#scoreboard = Scoreboard()


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(START_POSITION)
        self.scoreboard = Scoreboard()

    def move(self):
        """Distance the turtle travels in an instance"""
        self.forward(MOVE_DISTANCE)

    def finish_line(self):
        """When turtle reaches this point it needs to return to the start for the next level"""
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(START_POSITION)
            self.scoreboard.update()
            return True



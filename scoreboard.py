from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.score}", align='center', font=FONT)
        self.score += 1

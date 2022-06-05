import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
#scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, 'Up')

cars = []
counter = 0

game_is_on = True
while game_is_on:
    #scoreboard.update()
    time.sleep(0.1)
    screen.update()
    player.finish_line()
    if counter % 6 == 0:
        car_manager = CarManager()
        cars.append(car_manager)
    for car in cars:
        car.move()
        if player.distance(car)<28 and abs(player.ycor() - car.ycor()) <= 20:
            game_is_on = False
    counter += 1


screen.exitonclick()
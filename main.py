import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, 'Up')

cars = []
counter = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Detect when turtle reaches the finish line
    if player.finish_line():
        scoreboard.update()
        car_manager.faster()
    # Create a car every six loops
    if counter % 6 == 0:
        car_manager.create_car()
    car_manager.move()
    # Detect when turtle collides with a car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    counter += 1


screen.exitonclick()
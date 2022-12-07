from turtle import Turtle, Screen
from player import Player
from car import Car
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("cadetblue1")
screen.tracer(0)

player = Player()
car = Car()
score = ScoreBoard()

screen.listen()
screen.onkeypress(key="Up", fun=player.move_up)

def check_collision():
    for i in range(0, len(car.car_list)-1):
        #if car.car_list[i].distance(player) < 20:
        if (car.car_list[i].xcor()) < 30 and car.car_list[i].xcor() > -30:
            if abs((car.car_list[i].ycor()) - player.ycor()) < 21:
                player.write("Game Over!", align="center", font=("Arial", 24, "normal"))
                return True


while True:
    time.sleep(0.1)
    screen.update()
    if player.check_if_top():
        score.update_level()
        car.car_speed += 2.5
    if check_collision():
        break
    car.generate_random_car()
    car.move_car()

screen.exitonclick()
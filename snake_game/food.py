from turtle import Turtle
from snake import Snake
from scoreboard import ScoreBoard
import random

class Food(Turtle, Snake):
    def __init__(self):
        super().__init__()
        self.food = Turtle(shape="circle")
        self.food.penup()
        self.food.color("red")
        self.move_food_position()
        self.food_xpos
        self.food_ypos 

    
    def move_food_position(self):
        random_x = random.randrange(-280, 280, 20)
        random_y = random.randrange(-280, 280, 20)
        self.food.goto(random_x, random_y)
        self.food_xpos = self.food.xcor()
        self.food_ypos = self.food.ycor()
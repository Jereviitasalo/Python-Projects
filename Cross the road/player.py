from turtle import Turtle

MOVE_DISTANCE = 10

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setheading(90)
        self.goto(0, -280)
    

    def move_up(self):
        self.forward(MOVE_DISTANCE)
    
    def check_if_top(self):
        if self.ycor() >= 290:
            self.goto(0, -280)
            return True
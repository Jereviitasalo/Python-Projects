from turtle import Turtle

STARTING_COORDS = ((-470, 0),(470, 0))
paddles = [] # List to store both paddles to access them easily

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_paddle() # Creates 2 paddles and place them to STARTING COORDS
        self.y = 0 # Paddles y coordinate to help detect borders
    
    def create_paddle(self):
        for i in range(0, 2):
            paddle = Turtle(shape="square")
            paddle.penup()
            paddle.color("white")
            paddle.shapesize(stretch_len=4, stretch_wid=1)
            paddle.goto(STARTING_COORDS[i])
            paddle.setheading(90)
            paddles.append(paddle)
    
    def change_enemy_direction(self):
        """Changes enemy direction when colliding with borders"""
        if paddles[1].ycor() > 320:
            paddles[1].setheading(270)
        elif paddles[1].ycor() < -320:
            paddles[1].setheading(90)

    def move_enemy(self):
        paddles[1].forward(10)
    
    def move_enemy_up(self):
        self.y = paddles[1].ycor() + 40
        paddles[1].sety(self.y)

    def move_enemy_down(self):
        self.y = paddles[1].ycor() - 40
        paddles[1].sety(self.y)
    
    def move_up(self):
        self.y = paddles[0].ycor() + 40
        paddles[0].sety(self.y)
    
    def move_down(self):
        self.y = paddles[0].ycor() - 40
        paddles[0].sety(self.y)
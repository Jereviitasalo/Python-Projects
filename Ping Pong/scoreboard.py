from turtle import Turtle

FONT = ("Arial", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = [0, 0]
        self.penup()
        self.color("white")
        self.hideturtle()
    
    def add_enemy_score(self):
        self.score[1] += 1

    def add_score(self):
        self.score[0] += 1
    
    def print_enemy_score(self):
        self.write(f"Score: {self.score[1]}", font = FONT)

    def print_score(self):
        self.write(f"Score: {self.score[0]}", font = FONT)


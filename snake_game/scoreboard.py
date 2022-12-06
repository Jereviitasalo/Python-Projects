from turtle import Turtle

TEXT_ALIGN = "center"
FONT = ("Arial", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.goto(0, 250)
        self.write(f"Score: {self.score}", align=TEXT_ALIGN, font=FONT)

    def add_score(self):
        self.score += 1
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=TEXT_ALIGN, font=FONT)
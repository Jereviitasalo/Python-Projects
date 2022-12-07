from turtle import Turtle

TEXT_ALIGN = "center"
FONT = ("Arial", 16, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-240, 250)
        self.write(f"Level {self.level}.", align=TEXT_ALIGN, font=(FONT))
    
    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level {self.level}.", align=TEXT_ALIGN, font=(FONT))
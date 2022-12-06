import turtle as t
import time

TEXT_ALIGN = "center"
FONT = ("Arial", 30, "normal")
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]
        self.is_collision = 0
        self.game_over_txt = t.Turtle()
        self.game_over_txt.hideturtle()
        self.game_over_txt.color("red")

    def create_snake(self):
        x = 0
        for index in range(0, 3):
            snake = t.Turtle(shape="square")
            snake.penup()
            snake.color("white")
            snake.setx(x)
            self.snake_list.append(snake)
            x -= 20
    
    def create_snake_piece(self):
        snake = t.Turtle(shape="square")
        snake.penup()
        snake.color("black")
        self.snake_list.append(snake)
    
    def move_snake(self):
        for i in range(len(self.snake_list)-1, 0, -1):
            x_coord = self.snake_list[i-1].xcor()
            y_coord = self.snake_list[i-1].ycor()
            self.snake_list[i].goto(x_coord, y_coord)
        self.head.forward(MOVE_DISTANCE)
        self.snake_list[len(self.snake_list)-1].color("white")

    def detect_collision(self):
        for snake in self.snake_list[1:]: # Leikataan listan ensimmainen pala pois, koska se on paa
            if self.head.distance(snake) < 10:
                self.is_collision = 1
                self.game_over_txt.write(" Game over! :/", align=TEXT_ALIGN, font=FONT)
                break
            elif abs(int(self.head.xcor())) > 300 or abs(int(round(self.head.ycor()))) > 300:
                self.is_collision = 1
                self.game_over_txt.write("Game over! :/", align=TEXT_ALIGN, font=FONT)
                break

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
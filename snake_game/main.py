import snake as s
from turtle import Screen
from food import Food
import scoreboard as sc
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

snake = s.Snake()
score = sc.ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

food = Food() # Spawnaa automaattisesti ruoka random paikalle

def detect_food():
    # Tunnista jos madon paa on samassa positiossa kuin ruoka
    food_xpos = food.food_xpos
    food_ypos = food.food_ypos
    head_xpos = snake.head.xcor()
    head_ypos = snake.head.ycor()
    if (int(round(head_xpos)) == food_xpos) and (int(round(head_ypos)) == food_ypos):
        score.add_score()
        score.update_score()
        return True
    else:
        return False

game_running = True
while  game_running:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    snake.detect_collision()
    if snake.is_collision == 1:
        game_running = False
    elif detect_food():
        food.reset()
        food.move_food_position()
        snake.create_snake_piece()
    

screen.exitonclick()
from turtle import Turtle, Screen
import paddle
import time
import pong_ball
import scoreboard

screen = Screen()
screen.setup(width=1000, height=700)
screen.bgcolor("black")
screen.tracer(0)

pad = paddle.Paddle()
pong = pong_ball.PongBall()
enemy_score = scoreboard.ScoreBoard()
player_score = scoreboard.ScoreBoard()
enemy_score.goto(50, 300)
player_score.goto(-200, 300)
enemy_score.write(f"Score: {enemy_score.score[1]}", font=("Arial", 24, "normal"))
player_score.write(f"Score: {player_score.score[0]}", font=("Arial", 24, "normal"))

screen.listen()
screen.onkey(key="Up", fun=pad.move_up)
screen.onkey(key="Down", fun=pad.move_down)

while abs(enemy_score.score[1] - player_score.score[0]) < 3:
    screen.update()
    time.sleep(0.1)
    pong.move_ball()
    pong.check_ball_direction()
    if pong.check_if_ball_hit_paddle() == 1:
        player_score.clear()
        player_score.add_score()
        pong.goto(0, 0)
        pong.ball_velocity = 1
    elif pong.check_if_ball_hit_paddle() == 0:
        enemy_score.clear()
        enemy_score.add_enemy_score()
        pong.goto(0, 0)
        pong.ball_velocity = 1
    pad.move_enemy()
    pad.change_enemy_direction()
    enemy_score.print_enemy_score()
    player_score.print_score()

screen.exitonclick()
from turtle import Turtle
import paddle

class PongBall(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setheading(90) # Alustetaan suunta ylospain
        self.increasex = 10 # Alustetaan x:n muutos aluksi positiiviseen suuntaan
        self.ball_velocity = 1 # Pallon vauhti kiihtyy jokaisella mailaan kosketuksella 0.2 verran

    def check_if_ball_hit_paddle(self):
        if self.xcor() > 450 and self.distance(paddle.paddles[1]) < 50: # Jos osutaan vastustajan mailaan, niin vaihdetaan x:n suuntaa
            self.increasex = -10 * self.ball_velocity
            self.ball_velocity += 0.2
        elif self.xcor() > 480:
            self.increasex = -10
            return 1

        if self.xcor() < -450 and self.distance(paddle.paddles[0]) < 50: # Jos osutaan pelaajan mailaan, niin vaihdetaan x:n suuntaa
            self.increasex = 10 * self.ball_velocity
            self.ball_velocity += 0.2
        elif self.xcor() < -480:
            self.increasex = 10
            return 0

    
    def move_ball(self):
        self.setx(self.xcor() + self.increasex) # Liikkuu 10 pykalaa oikealle
        self.forward(10) # Liikkuu 10 pykalaa ylos, koska alustettu suunta ylospain
    
    def check_ball_direction(self):
        if self.ycor() > 320: # Tarkistaa, jos pallo osuu ylareunaan
            self.setheading(270) # Vaihtaa pallon suunnan alaspain
        elif self.ycor() < -320: # Tarkistaa jos pallo osuu alareunaan
            self.setheading(90) # Vaihtaa pallon suunnan ylospain
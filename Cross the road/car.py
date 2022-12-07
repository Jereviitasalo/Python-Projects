import random
from turtle import Turtle

COLORS = ["red", "blue", "yellow", "orange", "green", "pink", "purple"]
LEFT = 180
CAR_SPAWN_TIME = 5 # Mita pienempi luku, sita nopeammin autoja spawnaa

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = [] # Lista luoduille autoille
        self.wait_time = CAR_SPAWN_TIME
        self.car_speed = 10
        self.hideturtle()
    
    def generate_random_car(self):
        if self.wait_time == 0:
            new_car = Turtle(shape="square") # Luodaan uusi auto objekti
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1) # Auton koko
            new_car.setx(300) # Alustetaan jokaisen luodun auto samaan x positioon
            new_car.color(COLORS[random.randint(0, 6)]) # Annetaan autolle random vari
            new_car.sety(random.randint(-260, 260)) # Annetaan autolle random y positio
            self.car_list.append(new_car) # Lisataan auto objekti listaan
            self.wait_time = CAR_SPAWN_TIME
        self.wait_time -= 1


    def move_car(self):
        for car in self.car_list:
            new_x = car.xcor()
            new_x -=  self.car_speed
            car.setx(new_x) # Liikutetaan autoa aina 10 pykalaa eteenpain (CAR_SPEED = 10)

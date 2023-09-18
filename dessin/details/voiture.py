from turtle import *
from random import randint

class voiture:
    def __init__(self) -> None:
        self.x , self.y = randint(-300,300) , randint(-300,-250)
        self.create()

    def create(self):
        x , y = self.x , self.y
        up()
        goto(x,y)
        fillcolor("red")
        begin_fill()
        down()
        forward(100)
        left(90)
        forward(20)
        left(90)
        forward(25)
        right(90)
        forward(20)
        left(90)
        forward(75)
        left(90)
        forward(40)
        left(90)
        end_fill()
        self.roues()
        

    def roues(self):
        fillcolor("black")
        forward(15)
        begin_fill()
        circle(-15,360)
        end_fill()
        forward(60)
        begin_fill()
        circle(-15,360)
        end_fill()
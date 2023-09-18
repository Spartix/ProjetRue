from random import randint
from turtle import *


class passage:
    def __init__(self) -> None:
        self.x = randint(-350,350)
        self.y = -250
        for i in range(5):
            self.create()
            self.y -= 20
    
    def create(self):
        up()
        goto(self.x,self.y)
        down()
        fillcolor("black")
        begin_fill()
        for _ in range(2):
            forward(40)
            right(90)
            forward(10)
            right(90)
        end_fill()
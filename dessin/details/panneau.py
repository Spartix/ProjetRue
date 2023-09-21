from turtle import *
from random import randint , choice

class panneau:
    def __init__(self) -> None:
        print('Y A PAS DE PANNEAUUUUUX')
        x,y = randint(-300,300) , choice([-250,-350])
        self.x = x
        self.y = y

    def create(self) -> None:
        """
        function generant un panneau
        """
        x = self.x -20
        y = self.y +30
        centre = {
            "x":x,
            "y":y
        }
        up()
        goto(self.x,self.y)
        left(90)
        forward(50)
        down()
        fillcolor("red")
        begin_fill()
        circle(20,360)
        end_fill()
        up()
        goto(centre["x"],centre["y"])
        left(180)
        down()
        forward(50)
        up()
        goto(centre["x"],centre["y"]+12)
        left(90)
        fillcolor("white")
        begin_fill()
        forward(10)
        left(90)
        forward(10)
        left(90)
        forward(20)
        left(90)
        forward(10)
        left(90)
        forward(20)
        end_fill()
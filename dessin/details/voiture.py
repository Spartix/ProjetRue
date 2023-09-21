from turtle import *
from random import choice, randint

class voiture:
    def __init__(self) -> None:
        """
        Class voiture permettant de creer une voiture dans une position aleatoire dans sur la route
        """
        position = {
            "x":[
                -300,
                -200,
                -100,
                100,
                250
            ],
            "y":[
                -320,
                -250
            ]
        }
        self.x , self.y = choice(position["x"]), choice(position["y"])

        self.create()

    def create(self):
        """
        function de creation de voiture
        """
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
        """
        function de creation des roues
        """
        fillcolor("black")
        forward(15)
        begin_fill()
        circle(-15,360)
        end_fill()
        forward(60)
        begin_fill()
        circle(-15,360)
        end_fill()
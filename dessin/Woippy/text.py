from turtle import *

class woippy:
    def __init__(self) -> None:
        self.x = -150
        self.y = 250

    def text(self):
        up()
        goto(self.x,self.y)
        down()
        right(90)
        forward(50)
        left(90)
        forward(25)
        left(90)
        forward(50)
        right(180)
        forward(50)
        left(90)
        forward(25)
        left(90)
        forward(50)
        right(180)
        forward(50)
        left(90)
        up()
        forward(20)
        down()
        #FAIRE LE O
        for _ in range(4):
            forward(50)
            left(90)
        up()
        #espace entre le O et le I
        forward(50+20)
        #FAIRE LE I
        down()
        left(90)
        forward(50)
        #BACK a la base de I
        right(180)
        forward(50)
        left(90)
        up()
        #espace entre le I et P
        forward(20)
        #FAIRE LES P
        for _ in range(2):
            down()
            left(90)
            forward(25)
            for _ in range(4):
                    forward(25)
                    right(90)
            left(180)
            forward(25)
            left(90)
            up()
            forward(20+25)
            down()
        #Faire le Y
        up()
        forward(20)
        down()
        left(90)
        forward(35)
        left(60)
        forward(35)
        right(150)
        up()
        forward(35)
        down()
        right(120)
        forward(20)
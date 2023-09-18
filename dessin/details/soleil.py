from random import randint
from turtle import *



class soleil:

    def create():
        up()
        goto(randint(-300,600),150)
        down()
        fillcolor("yellow")
        begin_fill()
        circle(100,360)
        end_fill()
from turtle import *
from .utility.color import color

class house :
    def create(x) -> None:
        up()
        width(2)
        down()
        left(90)
        begin_fill()
        for _ in range(2):
            forward(100)
            right(90)
            forward(125)
            right(90)
        end_fill()
        forward(100)
    
    def mult(etages,x):
        up()
        goto(x,-250)
        down()
        
        fillcolor(color.random())
        for _ in range(etages):
            house.create(x)
            right(90)
        width(5)
        forward(125)
        width(1)
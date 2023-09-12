from turtle import *

class fenetre:
    def create(x,y):
        up()
        goto(x,y)
        down()
        color("black")
        fillcolor("#bffffa")
        
        begin_fill()
        for _ in range(4):
            
            forward(25)
            left(90)
        end_fill()
    
    def porte(x,y,colors):
        up()
        goto(x,y)
        down()
        color("white")
        fillcolor(colors)
        begin_fill()
        for _ in range(2):
            forward(25)
            left(90)
            forward(60)
            left(90)
        end_fill()
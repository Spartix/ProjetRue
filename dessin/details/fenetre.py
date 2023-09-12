from turtle import *

class fenetre:
    def create(x,y):
        up()
        goto(x,y)
        down()
        fillcolor("#ffffff")
        begin_fill()
        for _ in range(4):
            
            forward(25)
            left(90)
        end_fill()
    
    def porte():
        print("JE FAIS UNE PORTE")
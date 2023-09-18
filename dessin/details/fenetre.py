from turtle import *

class fenetre:
    def create(x,y):
        """
        function create permettant de generer une fenetre a des coordonée données
        x (int): position de depart
        y (int): position de depart
        return (Void)
        """
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
        """
        fonction porte permettant de generer une porte a des coordonée données
        x (int): position x de depart
        y (int): position y de depart
        colors (str): couleur de la porte
        return (Void)
        """
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
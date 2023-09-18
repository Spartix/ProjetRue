from turtle import *
from dessin.details.toit import toit
from .utility.color import color

class house :
    """
    Class house permettant de créer des immeubles et etages
    """
    def create(x) -> None:
        """"
        function create permettant de creer un etage à une position x
        x (int) : position de depart de l'etage
        return (Void)
        """
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
        """
        function mult permettant de creer un immeuble de plusieurs etages
        etages(int): Nombre d etages a generer
        x (int): position de depart pour creer l'immeuble
        return (void)
        """
        up()
        goto(x,-250)
        down()
        
        fillcolor(color.random())
        for _ in range(etages):
            house.create(x)
            right(90)
        toit()
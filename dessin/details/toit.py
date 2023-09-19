from random import choice
from turtle import *

class toit:
    """
    Class toit permettant de creer un toit a chaque immeuble

    """
    def __init__(self) -> None:
        """
        function d'initialisation executant une fonction aleatoire de la class toit
        """
        function = [
                    self.triangle,
                    self.cercle,
                    self.droit
                    ]
        choice(function)()

    def droit(self):
        """
        function droit permettant de generer un toit plat
        return (Void)
        """
        width(10)
        forward(125)
        width(1)
    
    def triangle(self):
        """
        function triangle permettant de generer un toit triangulaire
        return (Void)
        """
        fillcolor("black")
        begin_fill()
        width(5)
        left(45)
        forward(87.5)
        right(90)
        forward(87.5)
        left(45)
        left(180)
        forward(125)
        left(180)
        end_fill()
        width(1)

    def cercle(self):
        """
        function generant un toit circulaire
        return (Void)
        """
        fillcolor("black")
        begin_fill()
        width(5)
        forward(125)
        left(90)
        circle(62.5,180)
        left(90)
        width(1)
        end_fill()
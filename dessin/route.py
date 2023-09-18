from turtle import *

class route:
    """
    Class route permettant de generer la route principal de la rue
    """
    def __init__(self,y) -> None:
        up()
        width(5)
        color("#550096")
        goto(-350,y)
        down()
        forward(700)
        color("black")
from random import randint


class color:
    def random():
        colors = ["red","yellow","blue"]
        return colors[randint(0,len(colors)-1)]
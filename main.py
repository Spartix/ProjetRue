from dessin.route import route
from dessin.house import house 
from dessin.details.fenetre import fenetre
from random import randint
from turtle import *

etage = 100
speed(25)
route()
x = -325
y1 = -250
nbetage = list()
for i in range(4):
    retage = randint(1,4)
    nbetage.append(retage)
    house.mult(retage,x)
    x += 150
y1 += 37
up()
print(nbetage)

x1 = -325


for immeuble in nbetage:
    """
    immeuble = nombre d etage sur l immeuble actuel
    a chaque immeuble on va...
    """
    index = 0
    porte = False
    while immeuble != 0:
        xb = x1
        for i in range(3):
            if index == 0:
                if(not(porte)):
                    if(randint(1,3) == 3):
                        fenetre.porte()
                        porte = True
                    else:
                        x1 = x1+12
                        fenetre.create(x1,y1)
                        x1 = x1+25
                        end_fill()
                else:
                    x1 = x1+12
                    fenetre.create(x1,y1)
                    x1 = x1+25
                    end_fill()
            else:
                    x1 = x1+12
                    fenetre.create(x1,y1)
                    x1 = x1+25
                    end_fill()

        y1 += 100
        immeuble -= 1
        x1 = xb
        index +=1

    y1 = -250+37
    x1 += 150
    
route()
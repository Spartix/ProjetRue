from dessin.route import route
from dessin.house import house 
from dessin.details.fenetre import fenetre
from random import randint
from turtle import *
from dessin.utility.color import color
from dessin.details.voiture import voiture
from dessin.details.passage import passage
from dessin.details.soleil import soleil
from dessin.Woippy.text import woippy
from dessin.details.panneau import panneau


def main(vit:int):
    """
    Fonction main permettant de générer la rue
    vit (int) : vitesse de generation de la rue
    return (void)
    """
    ht()

    speed(vit)
    
    soleil.create()
    passage()
    route(-250)
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
    "print(nbetage)"

    x1 = -325


    for immeuble in nbetage:
        """
        immeuble = nombre d etage sur l immeuble actuel
        a chaque immeuble on va faire une porte temps que le rez de chaussé n'a pas au moins une porte
        return (void)
        """
        index = 0
        porte = False
        while immeuble != 0:
            xb = x1
            pos = randint(0,2)
            for i in range(3):
                if(index == 0):
                    if(i == pos):
                        if(not(porte)):
                            x1 = x1+12
                            fenetre.porte(x1,y1-35,color.random())
                            porte = True
                            x1 = x1 +25
                        else:
                            x1 = x1+12
                            fenetre.create(x1,y1)
                            x1 = x1+25
                    else:
                        x1 = x1+12
                        fenetre.create(x1,y1)
                        x1 = x1+25
                else:
                    x1 = x1+12
                    fenetre.create(x1,y1)
                    x1 = x1+25
            y1 += 100
            immeuble -= 1
            x1 = xb
            index +=1

        y1 = -250+37
        x1 += 150
    route(-250)
    route(-350)
    





if __name__ == "__main__":
    vitesse = int(input("Vitesse\n >"))
    while True:
        clearscreen()
        
        main(vitesse)
        
        for i in range(5):
            voiture()
        panneau().create()
        woippy().text()
        mainloop()



99999
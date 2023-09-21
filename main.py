from export import *


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
    nb_etage = list()
    for _ in range(4):
        retage = randint(1,4)
        nb_etage.append(retage)
        house.mult(retage,x)
        x += 150
    y1 += 37
    up()
    "print(nb_etage)"

    x1 = -325


    for immeuble in nb_etage:
        """
        immeuble = nombre d etage sur l immeuble actuel
        a chaque immeuble on va faire une porte temps que le rez de chaussé n'a pas au moins une porte
        return (void)
        """
        index = 0
        porte = False
        while immeuble != 0:
            temp_x = x1
            position = randint(0,2)
            for i in range(3):
                if(index == 0):
                    if(i == position):
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
            x1 = temp_x
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
        
        for _ in range(5):
            voiture()
        panneau().create()
        woippy().text()
        mainloop()

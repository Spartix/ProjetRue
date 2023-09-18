from random import choice


class color:
    """
    class color permettant de generer des couleurs
    """
    def random():
        """
        function random permettant de retourner un code couleur aleatoire
        return (str) : couleur sous forme hex ou str
        """
        colors = ["red","yellow","blue","#c8ffbf","#ff4060","#b87639","#f2f279","#c45033"]
        return choice(colors)
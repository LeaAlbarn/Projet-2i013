import sys
sys.path.append("../..")


def saisieCoup(jeu):
    coordonnees = []
    coordonnees.append(input("Priere d'entrer le numero de la ligne :"))
    coordonnees.append(input("Priere d'entrer le numero de la colonne :"))
    return coordonnees
    
    """ jeu -> coup
        Retourne un coup a jouer
    """


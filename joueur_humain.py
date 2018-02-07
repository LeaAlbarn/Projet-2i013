import sys
sys.path.append("../..")

def saisieCoup(jeu):
    
    coordonnees = []
    coordonnees.append(jeu[1]-1)
    coordonnees.append(input("Tape un numero de colonne etre humain :"))
    return coordonnees
    

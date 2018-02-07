import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_humain
game.joueur1=joueur_humain
game.joueur2=joueur_humain

def joue ():
    """void -> nat
    retourne un gagnant"""
    jeu = game.initialiseJeu ()

     
 
    while not game.finJeu(jeu) : 
        game.affiche(jeu)
        coup = game.saisieCoup(game.getCopieJeu(jeu))
        game.joueCoup(jeu, coup)
        game.affiche(jeu)
    return game.getGagnant (jeu)
    
victoires = []
for i in range (50) : 
    gagnant = joue()
    victoires[gagnant]+=1

print str(victoires)

joueur = game.joueur2
game.joueur2 = game.joueur1
game.joueur1 = joueur

for i in range (50) : 
    g=joue()
    victoires[g%2+1]+=1

print str(victoires)





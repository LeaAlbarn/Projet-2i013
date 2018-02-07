import othello1
import sys
sys.path.append("..")
import game
game.game=othello1
sys.path.append("./Joueurs")
import joueur_humain
game.joueur1=joueur_humain
game.joueur2=joueur_humain
jeu=game.initialiseJeu()

while(not game.finJeu(jeu)) :
    game.affiche(jeu)
    print"Joueur ", jeu[1], ", a votre tour de jouer"
    coup = game.saisieCoup(jeu)
    game.joueCoup(jeu, coup)
gagnant=game.getGagnant(jeu)
game.affiche(jeu)
print "Le gagnant est le joueur",gagnant+1


import sys
sys.path.append("..")
import game

def initPlateau() : 
    plateau=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    plateau[3][3]=1
    plateau[4][4]=1
    plateau[3][4]=2
    plateau[4][3]=2
    return plateau
    
def getCoupsValides (jeu) : 
	"""jeu -> liste de coups
	retourne une liste de coups valides"""
	coups = toucheAdversaire(jeu)
	return [x for x in coups if len(encadrements(jeu,x,False))>0]
	#si False, on s'arrete des que l'on a un coup valide

def toucheAdversaire (jeu) :
	"""jeu -> liste de coups
	retourne la liste des coups touchant l'adversaire"""
	return[[i,j] for i in range(8) for j in range(8) for k in [-1,0,1] for l in [-1,0,1] if (jeu[0][i][j] == 0) and (i+k) >= 0 and (i+k)<8 and (j+k)>=0 and (j+l)<8 and jeu[0][i+k][j+l]==(jeu[1]%2+1)]
	
def getCaseAutour (jeu,case) :
	"""jeu*case -> liste de cases
	prend une case d'un jeu et retourne les 8 cases autour de celle-ci"""
	return [[case[0]+i, case[1]+j] for i in [-1,0,1] for j in [-1,0,1] if case[0]+i < 8 and case[0] + i >= 0 and case[0]+j < 8 and case[0]+j >= 0 and (case[i]!=0 or case[j]!=0) ]
	

def encadrements(jeu,coup,tous=True) : 
    """jeu, liste, bool -> liste de directions
    retourne une liste de directions"""
    liste_retour = []
    for i in [-1,0,1] :
         for j in [-1,0,1] :
             if (i==0) and (j==0) :
                 continue
             if checkDirection(jeu,coup,[i,j]) :
                 liste_retour.append([i,j])
                 if not tous :
                     return liste_retour
    return liste_retour
					
def checkDirection(jeu,coup,direction) : #direction [i,j]
	"""jeu* liste* [i,j] -> bool
	retourne vrai si on va dans la bonne direction, false sinon"""
	joueur = jeu[1]
	i = 0
	while True : 
		i+=1
		coup = [coup[0]+direction[0], coup[1]+direction[1]]
		if coup[0]<0 or coup[0] >8 or coup[1] < 0 or coup[1]>8 :
			return False
		if jeu[0][coup[0]][coup[1]] == 0 :
			return False
		if jeu[0][coup[0]][coup[1]] == joueur :
			return i>1


def joueCoup(jeu, coup) : 
	"""jeu*coordonnees -> void
	met a jour le jeu avec le coup joue"""
	game.getCoupsJoues(jeu).append(coup)
	joueur=jeu[1]
	scores=game.getScores(jeu)
	encadrement=encadrements(jeu, coup, True) 
	adversaire=joueur%2+1
	game.setCaseVal(jeu, coup[0], coup[1], joueur)
	scores[joueur-1]+=1
	for d in encadrement: 
        	ligne=coup[0]
       		colonne=coup[1]
        while (True) : 
        	ligne+=d[0]
        	colonne+=d[1]
       		if (game.getCaseVal(jeu, ligne, colonne)==joueur) :
                	break
        	game.setCaseVal(jeu, ligne, colonne, joueur)
        	scores[joueur-1]+=1 
        	scores[adversaire-1]-=1
	game.changeJoueur(jeu)
        
        
        
def initScores():
	"""void -> [int,int]
	retourne les scores initiaux"""
	score = [2,2]
	return score	
 
def finPartie(jeu) :
    """jeu->bool
    retourne vrai si la fin du jeu est atteinte, false sinon"""
    fin_atteinte = True
    for i in range(8) :
        for j in range(8) :
            if jeu[0][i][j]==0 :
                fin_atteinte= False
    if len(jeu[3])>100 :
        fin_atteinte = True
    return fin_atteinte

def gagnant(jeu) :
    """jeu-> nat
    renvoie le numero du joueur gagant, 0 si match nul"""
    score = jeu[4]
    if score[0]>score[1] : 
        return 1
    if score[1]>score[0] : 
        return 2
    return 0
	
	

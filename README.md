*This project has been created as part of the 42 curriculum by eolivier and mbouyer.*


explication rapide de l'algo: possibilite et opposite: chiffre binnaires.
    current la case sur laquelle on se trouve
    stack le chemin
    self.visited: voir si on a visiter la case
    a partir du while: on regarde si il y a des voisins possbles (List[Tuple[int, int, str])
    si oui on ajoute comme valide dans stack, on modifie les murs de current pour les oubrir ou non:
    0000 en binaire = Tout ouvert. 1111 tout ferme. grace a &= on dit ca prend les bits en commun entre 15 et l'inverse de ce qui a ete selectionner dans possibility
    exemple: on a 15 donc 1111 et on veut retirer un mur au Nord(= 0001): on dit donc de garder ce qui est egale entre 1111 et 1110 donc 1110
    ensuite sur la nouvelle case voisine choisie au hazard grace a randit, on fait la meme, car si on retire un mur Est par exemple, on retire le mur West sur la case a Gauche d'elle
    si il n'y a pas de voisin on retourne en arriere en suprime le derniere element et le donne en nouvelle position


1. Générer la structure du maze (bits) OK
2. Vérifier qu’il est valide OK
3. Ajouter le "42" OK
4. Calculer le chemin (Backtraking)OK
5. Écrire en hex dans le fichier OK
6. (bonus) affichage ASCII  OK
7. Norme OK

    ce qu'il reste a faire:
    Il faut juste implementer la mecanique du flag Perfect
    Il faut faire en sorte que si exit ou entrer est dans le 42 on print un message d'erreur
    Rediger le Readme
    Rendre le projet

















## Description

**Amazing** est un projet d'algorithmie dont l'objectif est de generer un labirinthe en python 3.10 totalement dinamyque et maleable grace a un fichier de configuration.
Nous avons decide d'implementer un algorithme de bactraking iteratif.
Expliacation Rapide de l'algorithme:<br>
&nbsp;&nbsp;&nbsp;&nbsp;-On initialise maze: une liste de liste de int a 15 en fonction de height et width<br>
&nbsp;&nbsp;&nbsp;&nbsp;-On initialise see: une liste de liste de bool a False en fonction de height et width<br>
&nbsp;&nbsp;&nbsp;&nbsp;-Pourquoi 15 ? Car apres on va faire des operation binaires et 1 bit = 15 car = a 1111 donc a 8 + 4 + 2 + 1<br>
&nbsp;&nbsp;&nbsp;&nbsp;-Si la taille est plus grande que 9 et la longueur plus grande que 7 on place le motif 42 comme demander dans le sujet sinon on print un message<br>

&nbsp;&nbsp;&nbsp;&nbsp;-Grace a Random.seed() On choisis l'aleatoire entre guilemet<br>
&nbsp;&nbsp;&nbsp;&nbsp;On creer un dict possibilty qui a la valeur binaire de chaques point ou on peut se deplacer puis sont inverse avec opposite<br>
&nbsp;&nbsp;&nbsp;&nbsp;On initialise la position avec Entry renseigne dans le config.txt puis on met see a True pour dire qu'on a deja vu la case.<br>

&nbsp;&nbsp;&nbsp;&nbsp;Ensuite on va regarder chaques voisins pour voir si il a deja ete visite ou pas et si il est plus grand que 0 mais plus petit que height ou width et on va renvoyer des tuples de coordonne et en choisir au hazard grace a random pour se deplacer sur la case.<br>
&nbsp;&nbsp;&nbsp;&nbsp;Chaques deplacement est energistrer dans stack, une liste de tuple. Si On tombes sur aucun voisins valide, on suprime le drenier element de la stack et on le donne comme nouvelle position pour exploiter les autres voisins.<br>

&nbsp;&nbsp;&nbsp;&nbsp;Si on obtient des voisins valide, on va alors &= ~ Voulant dire "On garde les bits en commun entre l'inverse de" pour retirer les bits du mur et creer notre maze en meme temps.<br>
&nbsp;&nbsp;&nbsp;&nbsp;Des qu'on est sur la case de sortie on enregistre la stack pour garder le path.<br
## Instructions

Pour utiliser notre **Amazing**, il faut renseigner des donne dans le fichier de configuration **config.txt** dans lequelle on peut renseigner:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Width: La largeur du labirinthe<br>
&nbsp;&nbsp;&nbsp;&nbsp;Height: La Hauteur du labirinthe<br>
&nbsp;&nbsp;&nbsp;&nbsp;Entry: Les coordonne d'entre sous format Int, Int<br>
&nbsp;&nbsp;&nbsp;&nbsp;Exit: Les coordonne de sorte sous format Int, Int<br>

&nbsp;&nbsp;&nbsp;&nbsp;OUTPUT_FILE: Le fichier ou sera ecrit le resulat sous format HEXADECIMAL et le chemin pour aller jusqu'a la sortie<br>
&nbsp;&nbsp;&nbsp;&nbsp;PERFECT: Mettre 1(TRUE) ou 2(FALSE) sortie<br>
&nbsp;&nbsp;&nbsp;&nbsp;ALGORITHM: Bactracking<br>
&nbsp;&nbsp;&nbsp;&nbsp;SEED: Choisir de Manipuler l'aleatoire<br>
Vous avez acces a plusieurs commandes grace au **Makefile**:<br>
&nbsp;&nbsp;&nbsp;&nbsp;make install: Installer les dependance dans un virtual environnement<br>
&nbsp;&nbsp;&nbsp;&nbsp;make run: lancer le programme soit (python3 a_maze_ing.py config.txt)<br>
&nbsp;&nbsp;&nbsp;&nbsp;make debug: lancer le debugeur python<br>
&nbsp;&nbsp;&nbsp;&nbsp;make clean: suprimer les fichier du a mypy ou le cache python<br>
&nbsp;&nbsp;&nbsp;&nbsp;make lint: flake8 et mypy<br>
&nbsp;&nbsp;&nbsp;&nbsp;make lint strict: flake8 et mypy -strict<br>

## Resources

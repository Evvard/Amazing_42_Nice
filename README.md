""" explication rapide de l'algo: possibilite et opposite: chiffre binnaires.
    current la case sur laquelle on se trouve
    stack le chemin
    self.visited: voir si on a visiter la case
    a partir du while: on regarde si il y a des voisins possbles (List[Tuple[int, int, str])
    si oui on ajoute comme valide dans stack, on modifie les murs de current pour les oubrir ou non:
    0000 en binaire = Tout ouvert. 1111 tout ferme. grace a &= on dit ca prend les bits en commun entre 15 et l'inverse de ce qui a ete selectionner dans possibility
    exemple: on a 15 donc 1111 et on veut retirer un mur au Nord(= 0001): on dit donc de garder ce qui est egale entre 1111 et 1110 donc 1110
    ensuite sur la nouvelle case voisine choisie au hazard grace a randit, on fait la meme, car si on retire un mur Est par exemple, on retire le mur West sur la case a Gauche d'elle

    si il n'y a pas de voisin on retourne en arriere en suprime le derniere element et le donne en nouvelle position"""


"""
1. Générer la structure du maze (bits) OK
2. Vérifier qu’il est valide OK
3. Ajouter le "42" OK
4. Calculer le chemin (Backtraking)OK
5. Écrire en hex dans le fichier
6. (bonus) affichage ASCII """

"""     sys.setrecursionlimit(new_limit)
    changed_current_limit = sys.getrecursionlimit() """

from typing import List, Tuple
import random


# x = largeur
# y = taile

class MazeGenerator():

    def __init__(self, config: dict):
        self.height = config.get("HEIGHT")
        self.width = config.get("WIDTH")
        self.algo = config.get("ALGORITHM")
        self.seed = config.get("SEED")
        self.output = config.get("OUTPUT_FILE")
        self.perfect = config.get("PERFECT")
        self.entry = config.get("ENTRY")
        self.exit = config.get("EXIT")

    def maze_empty_generation(self) -> None:
        self.maze = [[15 for _ in range(self.width)]
                     for _ in range(self.height)]

    def visited(self) -> None:
        self.see = [[False for _ in range(self.width)]
                    for _ in range(self.height)]

    def check_case(self, x: int, y: int) -> bool:
        if 0 <= x < self.width and 0 <= y < self.height:
            if not self.see[y][x]:
                return True
        return False

    def get_valid_neighbors(self,
                            x: int,
                            y: int) -> List[Tuple[int, int, str]]:
        valid = []
        if self.check_case(x + 1, y):
            valid += [(x + 1, y, "E")]
        if self.check_case(x - 1, y):
            valid += [(x - 1, y, "W")]
        if self.check_case(x, y + 1):
            valid += [(x, y + 1, "S")]
        if self.check_case(x, y - 1):
            valid += [(x, y - 1, "N")]
        return valid

    def apply_42_pattern(self):
        pattern = [
                    "1000111",
                    "1000001",
                    "1110111",
                    "0010100",
                    "0010111"
                    ]
        offset_x = (self.width - 7) // 2
        offset_y = (self.height - 5) // 2

        pattern_height = len(pattern)
        pattern_width = len(pattern[0])

        for py in range(pattern_height):
            for px in range(pattern_width):
                if pattern[py][px] == "1":
                    real_x = px + offset_x
                    real_y = py + offset_y
                    self.see[real_y][real_x] = True
                    self.maze[real_y][real_x] = 15
                    if real_x + 1 < self.width:
                        self.maze[real_y][real_x + 1] |= 8
                    if real_x - 1 >= 0:
                        self.maze[real_y][real_x - 1] |= 2
                    if real_y + 1 < self.height:
                        self.maze[real_y + 1][real_x] |= 1
                    if real_y - 1 >= 0:
                        self.maze[real_y - 1][real_x] |= 4

    def bactracking_algorithm(self) -> List[List[int]]:
        self.maze_empty_generation()
        self.visited()

        if self.height >= 9 and self.width >= 7:
            self.apply_42_pattern()
        else:
            print("42 not appplied, parameter of configuration are too small")

        if self.seed is not None:
            random.seed(self.seed)

        posibility = {"N": 1, "S": 4, "E": 2, "W": 8}
        opposite = {"N": 4, "S": 1, "E": 8, "W": 2}
        current = (self.entry[0], self.entry[1])

        stack = []
        self.see[current[1]][current[0]] = True

        while True:
            neighbors = self.get_valid_neighbors(current[0], current[1])
            if neighbors:
                stack.append(current)
                nx, ny, direction = random.choice(neighbors)
                self.maze[current[1]][current[0]] &= ~posibility.get(direction)
                self.maze[ny][nx] &= ~opposite.get(direction)
                current = (nx, ny)
                self.see[ny][nx] = True

            elif stack:
                current = stack.pop()
            else:
                break

        # a retirer apres les test
        print(self.maze)
        print()
        print(stack)
        print()
        print()
        print(current)











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
2. Vérifier qu’il est valide
3. Ajouter le "42"
4. Calculer le chemin (Backtraking)
5. Écrire en hex dans le fichier
6. (bonus) affichage ASCII """

"""     sys.setrecursionlimit(new_limit)
    changed_current_limit = sys.getrecursionlimit() """

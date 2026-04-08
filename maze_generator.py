from typing import List, Optional, Tuple
import random


#x = largeur
#y = taile



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
        self.maze = [[15 for _ in range(self.width)] for _ in range(self.height)]

    def visited(self) -> None:
        self.visited = [[False for _ in range(self.width)] for _ in range(self.height)]

    def check_case(self, x: int, y: int) -> bool:
        if 0 <= x < self.width and 0 <= y < self.height:
            if not self.visited[y][x]:
                return True
        return False

    def get_valid_neighbors(self, x: int, y: int) -> Optional[List[Tuple[int, int, str]] | None]:
        valid = []
        if self.check_case(x + 1, y):
            valid += [(x + 1, y, "E")]
        if self.check_case(x - 1, y):
            valid += [(x - 1, y, "O")]
        if self.check_case(x, y + 1):
            valid += [(x, y + 1, "N")]
        if self.check_case(x, y - 1):
            valid += [(x, y - 1, "S")]
        return valid

    #Typer apres
    def bactracking_algorithm(self):
        self.maze_empty_generation()
        self.visited()

        current = (self.entry[0], self.entry[1])
        stack = []
        self.visited[current[1]][current[0]] = True

        while stack or self.get_valid_neighbors(current[0], current[1]):
            neighbors = self.get_valid_neighbors(current[0], current[1])
            if neighbors:
                stack.append(current)
                nx, ny, direction = random.choice(neighbors)
                current = (nx, ny)
                self.visited[ny][nx] = True
            else:
                current = stack.pop()

        print(stack)
        print()
        print()
        print(current)



""" 
1. Générer la structure du maze (bits)
2. Vérifier qu’il est valide
3. Ajouter le "42"
4. Calculer le chemin (Backtraking)
5. Écrire en hex dans le fichier
6. (bonus) affichage ASCII """



"""     sys.setrecursionlimit(new_limit)  
    changed_current_limit = sys.getrecursionlimit() """
from typing import List, Optional



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

    def algo_generation(self) -> None:
        self.visited = [[False for _ in range(self.width)] for _ in range(self.height)]

    def check_case(self, x: int, y: int) -> bool:
        if 0 <= x < self.width and 0 <= y < self.height:
            if not self.visited[y][x]:
                return True
        return False

    def get_valid_neighbors(self, x: int, y: int) -> List[tuple]:
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

    def bactracking_algorithm(self) -> ?:
    
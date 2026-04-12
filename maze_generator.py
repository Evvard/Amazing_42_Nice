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
        self.solution = []

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

    def apply_42_pattern(self) -> None:
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
        if (real_x, real_y) == self.entry or (real_x, real_y) == self.exit:
            raise ValueError("Entry or exit must be outside the 42 pattern")

    def bactracking_algorithm(self) -> List[List[int]]:
        self.maze_empty_generation()
        self.visited()

        if self.height >= 9 and self.width >= 7:
            self.apply_42_pattern()
        else:
            print("\n42 not appplied, height or width are too small\n")

        if self.seed is not None:
            random.seed(self.seed)

        posibility = {"N": 1, "S": 4, "E": 2, "W": 8}
        opposite = {"N": 4, "S": 1, "E": 8, "W": 2}
        current = (self.entry[0], self.entry[1])

        stack = []
        self.see[current[1]][current[0]] = True

        while True:
            if current == (self.exit[0], self.exit[1]) and not self.solution:
                self.solution += stack + [current]
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
        for i in range(len(self.maze)):
            print(self.maze[i])

        return self.maze

    def file_output(self) -> List[str]:
        file = open(self.output, 'w')
        for i in self.maze:
            hex_row = "".join("{:X}".format(cell) for cell in i)
            file.write(hex_row + "\n")
        file.write("\n")
        file.write(f"{self.entry[0]}, {self.entry[1]}\n")
        file.write(f"{self.exit[0]}, {self.exit[1]}\n")
        file.write("\n")

        direction = []
        solution = []
        for i in range(len(self.solution) - 1):
            curr = self.solution[i]
            nxt = self.solution[i+1]

            dx = nxt[0] - curr[0]
            dy = nxt[1] - curr[1]

            if dx == 1:
                direction.append("E")
                solution += ["E"]
            elif dx == -1:
                direction.append("W")
                solution += ["W"]
            elif dy == 1:
                direction.append("S")
                solution += ["S"]
            elif dy == -1:
                direction.append("N")
                solution += ["N"]

        file.write(" ".join(direction) + "\n")
        file.close()
        return solution

from typing import List, Tuple, Optional
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
        self.solution: List[Tuple[int, int]] = []

    def maze_empty_generation(self) -> None:
        if not self.width or not self.height:
            return
        self.maze = [[15 for _ in range(self.width)]
                     for _ in range(self.height)]

    def visited(self) -> None:
        if not self.width or not self.height:
            return
        self.see = [[False for _ in range(self.width)]
                    for _ in range(self.height)]

    def check_case(self, x: int, y: int) -> bool:
        if not self.width or not self.height:
            return False
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
        if not (self.width, self.height, self.maze, self.exit, self.see):
            return

        pattern = [
                    "1000111",
                    "1000001",
                    "1110111",
                    "0010100",
                    "0010111"
                    ]

        offset_x = (self.width - 7) // 2 if self.width else None
        offset_y = (self.height - 5) // 2 if self.height else None

        pattern_height = len(pattern)
        pattern_width = len(pattern[0])

        for py in range(pattern_height):
            for px in range(pattern_width):
                if pattern[py][px] == "1":
                    if px is not None and offset_x:
                        real_x = px + offset_x
                    else:
                        return None
                    if py is not None and offset_y:
                        real_y = py + offset_y
                    else:
                        return None
                    self.see[real_y][real_x] = True
                    self.maze[real_y][real_x] = 15
        if (real_x, real_y) == self.entry or (real_x, real_y) == self.exit:
            raise ValueError("Entry or exit must be outside the 42 pattern")

    def bactracking_algorithm(self) -> Optional[List[List[int]] | None]:
        self.maze_empty_generation()
        self.visited()

        if not self.width or not self.height:
            return None
        if self.height >= 9 and self.width >= 7:
            self.apply_42_pattern()
        else:
            print("\n42 not appplied, height or width are too small\n")

        if self.seed is not None:
            random.seed(self.seed)

        posibility = {"N": 1, "S": 4, "E": 2, "W": 8}
        opposite = {"N": 4, "S": 1, "E": 8, "W": 2}
        if not self.entry:
            return None
        current = (self.entry[0], self.entry[1])

        stack: List[tuple] = []
        self.see[current[1]][current[0]] = True

        if not self.exit or self.solution != []:
            return None

        while True:
            if current == (self.exit[0], self.exit[1]) and not self.solution:
                self.solution += stack + [current]
            neighbors = self.get_valid_neighbors(current[0], current[1])
            if neighbors:
                stack.append(current)
                nx, ny, direction = random.choice(neighbors)
                val = posibility.get(direction)
                opp = opposite.get(direction)

                if val is not None and opp is not None:
                    self.maze[current[1]][current[0]] &= ~val
                    self.maze[ny][nx] &= ~opp
                current = (nx, ny)
                self.see[ny][nx] = True

            elif stack:
                current = stack.pop()
            else:
                break
        return self.maze

    def file_output(self) -> Optional[List[str] | None]:
        file_name = self.output if self.output else "maze.txt"
        with open(file_name, 'w') as file:
            for i in self.maze:
                hex_row = "".join("{:X}".format(cell) for cell in i)
                file.write(hex_row + "\n")
            file.write("\n")
            if not self.entry or not self.exit:
                return None
            file.write(f"{self.entry[0]}, {self.entry[1]}\n")
            file.write(f"{self.exit[0]}, {self.exit[1]}\n")
            file.write("\n")

            direction: List[str] = []
            solution: List[str] = []
            for z in range(len(self.solution) - 1):
                curr_x, curr_y = self.solution[z]
                next_x, next_y = self.solution[z + 1]
                dx = next_x - curr_x
                dy = next_y - curr_y

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
        return solution

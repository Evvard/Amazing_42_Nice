from typing import List


def display(maze: List[List[int]], path: List[tuple] = None) -> None:

    line = []
    for r in maze:
        for i in r:
            if i == 15:
                line.append("█")
            else:
                line.append(" ")
        print(line)

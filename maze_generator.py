from typing import List


def maze_empty_generation(height: int, width: int) -> List[List[str]]:
    return [[15 for _ in range(width)] for _ in range(height)]


def backtraking_algorithm()
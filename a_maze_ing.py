from parser import extraction_config, config_validator
from sys import argv
from maze_generator import MazeGenerator
from display import display
import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def main() -> None:
    try:
        brut_data_from_config_txt = extraction_config(argv[1])
    except IndexError:
        raise IndexError("Missing file.txt is 2nd argument")

    config = config_validator(brut_data_from_config_txt)
    if isinstance(config, str):
        raise ValueError(config)
    print(config)
    maze = MazeGenerator(config)
    maze_brut = maze.bactracking_algorithm()
    solution = maze.file_output()
    display(maze_brut, solution)

    while True:

        print("\n--- A-Maze-ing ---")
        print("1. Re-generate a new maze")
        print("2. Show/Hide Path from entry to exit")
        print("3. Rotate maze colors")
        print("4. Quit")
        try:
            choice = int(input("Choice?(1-4):"))
            if choice < 1 or choice > 4:
                raise ValueError
        except Exception:
            raise ValueError("Wrong value in input for choice")
        if choice == 1:
            clear_terminal()
            config = config_validator(brut_data_from_config_txt)
            maze = MazeGenerator(config)
            maze_brut = maze.bactracking_algorithm()
            solution = maze.file_output()
            display(maze_brut, solution)
        elif choice == 2:
            pass
            pass
            pass
        elif choice == 3:
            pass
            pass
            pass
        else:
            break


if __name__ == "__main__":
    main()
""" try:
        main()
    except Execption as m:
         print(m) """

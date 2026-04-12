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
    display(maze_brut, solution, False, config.get("ENTRY"),
            config.get("EXIT"), False)

    path_visible = False
    colors_rotated = False

    while True:
        clear_terminal()
        display(maze_brut, solution, path_visible, config.get("ENTRY"),
                config.get("EXIT"), colors_rotated)

        print("\n--- A-Maze-ing ---")
        print("1. Re-generate a new maze")
        print("2. Show/Hide Path")
        print("3. Rotate maze colors")
        print("4. Quit")

        choice = input("Choice?(1-4): ")
        if choice == "1":
            config = config_validator(brut_data_from_config_txt)
            maze = MazeGenerator(config)
            maze_brut = maze.bactracking_algorithm()
            solution = maze.file_output()
        elif choice == "2":
            path_visible = not path_visible
        elif choice == "3":
            colors_rotated = not colors_rotated
        elif choice == "4":
            break
        else:
            raise Exception("Wrong input for --- A-Maze-ing ---")


if __name__ == "__main__":
    main()
""" try:
        main()
    except Execption as m:
         print(m) """

from parser import extraction_config, config_validator
from sys import argv
from mazegen.maze_generator import MazeGenerator
from display import display
import os


def clear_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def main() -> None:
    try:
        brut_data_from_config_txt = extraction_config(argv[1])
    except IndexError:
        raise IndexError("Missing file.txt is 2nd argument")

    if brut_data_from_config_txt is None:
        raise ValueError("Config file is empty or invalid")

    config = config_validator(brut_data_from_config_txt)

    maze = MazeGenerator(config)
    if config.get("ALGORITHM") == "bactracking":
        maze_brut = maze.bactracking_algorithm()
        solution = maze.file_output()

    if maze_brut is None or solution is None:
        print("Error: Could not generate maze or solution.")
        return

    path_visible = False
    colors_rotated = False
    bad_choice = False

    while True:
        height = config.get("HEIGHT")
        width = config.get("WIDTH")

        clear_terminal()
        if height < 9 or width < 7 if height and width else None:
            print("\n42 not appplied, height or width are too small\n")
        display(maze_brut, solution, path_visible,
                config.get("ENTRY", [0, 0]),
                config.get("EXIT", [0, 0]), colors_rotated)
        if bad_choice:
            print("Wrong input, please enter a number between 1 and 4.")
            bad_choice = False
            input("Press Enter to continue...")
        print("\n--- A-Maze-ing ---")
        print("1. Re-generate a new maze")
        print("2. Show/Hide Path")
        print("3. Rotate maze colors")
        print("4. Quit")

        choice = input("Choice?(1-4): ")
        if choice == "1":
            config = config_validator(brut_data_from_config_txt)
            maze = MazeGenerator(config)
            if config.get("ALGORITHM") == "bactracking":
                maze_brut = maze.bactracking_algorithm()
            solution = maze.file_output()
            if maze_brut is None or solution is None:
                break
        elif choice == "2":
            path_visible = not path_visible
        elif choice == "3":
            colors_rotated = not colors_rotated
        elif choice == "4":
            break
        else:
            break


if __name__ == "__main__":
    try:
        main()
    except Exception as m:
        print(m)

from parser import extraction_config, config_validator
from sys import argv
from maze_generator import MazeGenerator


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
    maze.bactracking_algorithm()



verifier que la demande pour exit et entrer sois bien plus petite que la longeur et la largeur
if __name__ == "__main__":
    
    # try:
    main()
    # except Exception as m:
    #    print(m)

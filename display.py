from typing import List, Tuple
from time import sleep


def transform_path(path: List[str],
                   start_pos: List[int]) -> List[Tuple[int, int]]:
    curr_x, curr_y = start_pos[0], start_pos[1]
    lst = []
    for move in path:
        if move == "E":
            curr_x += 1
        elif move == "W":
            curr_x -= 1
        elif move == "S":
            curr_y += 1
        elif move == "N":
            curr_y -= 1
        lst.append((curr_y, curr_x))
    return lst


def display(maze: List[List[int]], path: List[str], show_path: bool,
            entry: List[int], exit_pos: List[int], change_color: bool,
            time_animation: bool) -> None:

    W = "\033[47m  \033[0m" if not change_color else "\033[46m  \033[0m"
    MOTIF_W = "\033[100m  \033[0m" if not change_color else "\033[47m  \033[0m"
    START = "\033[45m  \033[0m"
    EXIT = "\033[41m  \033[0m"
    PATH = "\033[42m  \033[0m"
    EMPTY = "  "

    nw_path = transform_path(path, entry) if path and show_path else []
    f_path = [(entry[1], entry[0])] + nw_path
    entry_t = (entry[1], entry[0])
    exit_t = (exit_pos[1], exit_pos[0])

    width = len(maze[0])

    print(W * (width * 2 + 1))

    for y, line in enumerate(maze):
        mid_line = W
        bot_line = W

        for x, char in enumerate(line):
            curr = (y, x)

            if curr == entry_t:
                content = START
            elif curr == exit_t:
                content = EXIT
            elif curr in f_path:
                content = PATH
            elif char == 15:
                content = MOTIF_W
            else:
                content = EMPTY

            east_wall = (char & 2) != 0
            south_wall = (char & 4) != 0

            next_east = (y, x + 1)
            if not east_wall and curr in f_path and next_east in f_path:
                east_color = PATH
            else:
                east_color = MOTIF_W if (char == 15)\
                    else W if east_wall else EMPTY

            next_south = (y + 1, x)
            if not south_wall and curr in f_path and next_south in f_path:
                south_color = PATH
            else:
                south_color = MOTIF_W if (char == 15)\
                 else W if south_wall else EMPTY

            corner_color = MOTIF_W if (char == 15) else W

            mid_line += content + east_color
            bot_line += south_color + corner_color

        print(mid_line)
        if time_animation:
            sleep(0.5)
        else:
            pass
        print(bot_line)

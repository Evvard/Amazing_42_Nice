from typing import List, Tuple


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
            entry: List[int], exit_pos: List[int], change_color: bool) -> None:

    W = "\033[47m  \033[0m" if not change_color else "\033[46m  \033[0m"
    MOTIF_W = "\033[100m  \033[0m"

    START = "\033[45m  \033[0m"
    EXIT = "\033[41m  \033[0m"
    PATH = "\033[42m  \033[0m"
    EMPTY = "  "

    nw_path = transform_path(path, entry) if path and show_path else []
    entry_t = (entry[1], entry[0])
    exit_t = (exit_pos[1], exit_pos[0])

    height = len(maze)
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
            elif curr in nw_path:
                content = PATH
            elif char == 15:
                content = MOTIF_W
            else:
                content = EMPTY

            is_motif = (char == 15)

            east_color = MOTIF_W if is_motif else W
            south_color = MOTIF_W if is_motif else W
            corner_color = MOTIF_W if is_motif else W

            east_wall = (char & 2) or (x + 1 < width and (maze[y][x+1] & 8))
            south_wall = (char & 4) or (y + 1 < height and (maze[y+1][x] & 1))

            mid_line += content + (east_color if east_wall else content)
            bot_line += (south_color if south_wall else content) + corner_color

        print(mid_line)
        print(bot_line)

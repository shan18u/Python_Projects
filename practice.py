from curses import wrapper


maze = [
    ["/", "O", "/", "/", "/", "/", "/", "/", "/"],
    ["/", " ", " ", " ", " ", " ", " ", " ", "/"],
    ["/", " ", "#", "#", " ", "#", "#", " ", "/"],
    ["/", " ", "#", " ", " ", " ", "#", " ", "/"],
    ["/", " ", "#", " ", "#", " ", "#", " ", "/"],
    ["/", " ", "#", " ", "#", " ", "#", " ", "/"],
    ["/", " ", "#", " ", "#", " ", "#", "#", "/"],
    ["/", " ", " ", " ", " ", " ", " ", " ", "/"],
    ["/", "/", "/", "/", "/", "/", "/", "X", "/"]
]
def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j*2, "X", RED)
            else:
                stdscr.addstr(i, j*2, value, BLUE)



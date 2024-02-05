import curses
from curses import wrapper
from typing import List, Tuple, Optional
import queue
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#","#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ","#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ","#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ","#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#", " ", " ", "#", "#", "#", "#", " ", " ", " ", " ","#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ","#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#", "#", "#", "#", " ", " ", " ", "#", "#", " ", "#","#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ","#"],
    ["#", "#", " ", "#", " ", "#", " ", " ", " ", " ", " ", "#", "#", "#", "#", " ", "#", " ", " ","#"],
    ["#", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", "#", " ", "#", " ", " ","#"],
    ["#", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ","#"],
    ["#", " ", " ", "#", "#", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ","#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "X","#"]
]

def print_maze(maze: List[List[str]], stdscr, path: List[Tuple[int, int]] = None) -> None:
    """
    Print the maze with a given path highlighted.

    Parameters:
    - maze (list): The maze represented as a 2D list of characters.
    - stdscr: The standard screen object.
    - path (list): List of tuples representing the path to be highlighted.

    Returns:
    None
    """

    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for row, lis in enumerate(maze):
        for col, val in enumerate(lis):
            if (row, col) in path:
                stdscr.addstr(row, col*2, "X", RED)
            else:
                stdscr.addstr(row, col*2, val, BLUE) 

def find_start(maze: List[List[str]], start: str) -> Optional[Tuple[int, int]]:
    """
    Find the starting position in the maze.

    Parameters:
    - maze (list): The maze represented as a 2D list of characters.
    - start (str): The starting character.

    Returns:
    tuple or None: The coordinates of the starting position, or None if not found.
    """

    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            if val == start:
                return i, j
    return None

def find_neighbours(maze: List[List[str]], row: int, col: int) -> List[Tuple[int, int]]:
    """
    Find the neighboring positions of a given position in the maze.

    Parameters:
    - maze (list): The maze represented as a 2D list of characters.
    - row (int): Row index of the position.
    - col (int): Column index of the position.

    Returns:
    list: List of neighboring positions (tuples).
    """

    neighbours = []

    if row > 0:
        neighbours.append((row -1, col))
    if row + 1 < len(maze):
        neighbours.append((row + 1, col))
    if col > 0:
        neighbours.append((row, col - 1))
    if col < len(maze[0]):
        neighbours.append((row, col + 1))

    return neighbours

def find_path(maze: List[List[str]], stdscr) -> None:
    """
    Find and display the path from the starting position to the ending position in the maze.

    Parameters:
    - maze (list): The maze represented as a 2D list of characters.
    - stdscr: The standard screen object.

    Returns:
    None
    """

    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][col] == end:
            break

        neighbours = find_neighbours(maze, row, col)

        for neighbour in neighbours:
            if neighbour in visited:
                continue

            r, c = neighbour
            if maze[r][c] == "#":
                continue

            new_path = path + [neighbour]
            q.put((neighbour, new_path))
            visited.add(neighbour)

def main(stdscr) -> None:
    """
    Main function to run the maze solving visualization.

    Parameters:
    - stdscr: The standard screen object.

    Returns:
    None
    """

    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(maze, stdscr)
    stdscr.getch()

wrapper(main)

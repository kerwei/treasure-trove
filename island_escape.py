import numpy as np

from typing import Callable, List, Tuple, Union
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


elevation: List[List[int]] = []


def pathfind_up(coord: Tuple[int, int]) -> Union[Tuple[int, int], None]:
    """
    Returns the coord for the up direction if the elevation diff is one
    """
    x, y = coord
    if abs(elevation[x][y] - elevation[x-1][y]) <= 1:
        return (x-1, y)

    return ()


def pathfind_down(coord: Tuple[int, int]) -> Union[Tuple[int, int], None]:
    """
    Returns the coord for the down direction if the elevation diff is one
    """
    x, y = coord
    if abs(elevation[x][y] - elevation[x+1][y]) <= 1:
        return (x+1, y)

    return ()


def pathfind_left(coord: Tuple[int, int]) -> Union[Tuple[int, int], None]:
    """
    Returns the coord for the left direction if the elevation diff is one
    """
    x, y = coord
    if abs(elevation[x][y] - elevation[x][y-1]) <= 1:
        return (x, y-1)

    return ()


def pathfind_right(coord: Tuple[int, int]) -> Union[Tuple[int, int], None]:
    """
    Returns the coord for the right direction if the elevation diff is one
    """
    x, y = coord
    if abs(elevation[x][y] - elevation[x][y+1]) <= 1:
        return (x, y+1)

    return ()


def move_to_coord(coord: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Returns the possible paths from the given coord.
    Returns the same coord if terminal has been reached.
    Returns an empty list if it is a dead-end
    """
    x, y = coord
    traversed[x][y] = 1

    # Check for terminal points
    if any([
        x == 1,
        x == n,
        y == 1,
        y == n
    ]):
        return [coord]

    movements: List[Callable] = [
        pathfind_up,
        pathfind_down,
        pathfind_left,
        pathfind_right
    ]

    possible_paths: List[Tuple[int, int]] = []
    for move in movements:
        nxt = move(coord)
        if not nxt:
            continue

        nxt_x, nxt_y = nxt
        # Check if traversed
        if not traversed[nxt_x][nxt_y]:
            possible_paths.append((nxt_x, nxt_y))

    return possible_paths


def main(
    n: int,
    mtx: List[List[int]],
    traversed: np.ndarray) -> str:
    zeroth = n// 2 + 1      # 0-indexed +1 for padding
    global elevation
    elevation = [[-1] * (n + 2)]

    for i in range(1, n + 1):
        _row = [-1] + ([0] * n) + [-1]
        elevation.append(_row)

        for j, v in enumerate(mtx[i-1].split()):
            elevation[i][j+1] = int(v)

    elevation.append([-1] * (n + 2))
    traversed: np.ndarray = np.zeros((n + 2, n + 2))

    possible_paths: List[Tuple[int, int]] = [(zeroth, zeroth)]
    next_possible_paths: List[Tuple[int, int]] = []
    escapable: str = 'no'

    while True:
        for pth in possible_paths:
            _paths = move_to_coord(pth)

            if pth in _paths:
                escapable = 'yes'
                break

            next_possible_paths += _paths

        if escapable == 'yes' or not next_possible_paths:
            break

        possible_paths = next_possible_paths
        next_possible_paths = []

    return escapable


if __name__ == '__main__':
    n = 5
    mtx = ['0 0 0 0 0', '0 1 1 0 0', '0 1 1 1 0', '0 0 1 1 0', '0 0 0 0 0']
    traversed: np.ndarray = np.zeros((n + 2, n + 2))
    escapable = main(n, mtx, traversed)

    print(escapable)


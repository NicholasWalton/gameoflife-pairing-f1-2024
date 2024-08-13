import copy
import os
import random
import time
from pprint import pprint


def main():
    grid = [random_row() for _ in range(15)]

    # grid[1][1] = 1
    # grid[1][2] = 1
    # grid[1][3] = 1
    # print()
    # neighbors(grid)
    # print()
    generation_count = 0
    while True:
        os.system("cls")
        print("\n".join("".join("#" if cell else " " for cell in row) for row in grid))
        print()
        print(f"Generation count: {generation_count}")
        grid = next_generation(grid)
        generation_count += 1
        time.sleep(1)


def random_row():
    return [random.randint(0, 1) for _ in range(60)]


def neighbors(grid):
    for i, _ in enumerate(grid):
        for j, _ in enumerate(grid[i]):
            print(count_neighbors(grid, i, j), end="")
        print()


def count_neighbors(grid, row, col):
    count = 0
    row_count = len(grid)
    for i in range(max(0, row - 1), min(row_count - 1, row + 2)):
        col_count = len(grid[i])
        for j in range(max(0, col - 1), min(col_count - 1, col + 2)):
            if (i, j) != (row, col) and grid[i][j] == 1:
                count += 1
    return count


def next_generation(grid):
    new_grid = copy.deepcopy(grid)
    for i, _ in enumerate(grid):
        for j, _ in enumerate(grid[i]):
            neighbors = count_neighbors(grid, i, j)

            if grid[i][j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i][j] = 0
            else:
                if neighbors == 3:
                    new_grid[i][j] = 1

    return new_grid

if __name__ == "__main__":
    main()

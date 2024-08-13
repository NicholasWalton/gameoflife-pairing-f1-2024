import copy
import os
import random
import time


def main():
    grid = [random_row() for _ in range(15)]
    
    generation_count = 0
    while True:
        os.system("cls")
        print("\n".join("".join("#" if cell else " " for cell in row) for row in grid))
        print()
        print(f"Generation count: {generation_count}")
        grid = next_generation(grid)
        generation_count += 1
        time.sleep(0.1)


def random_row():
    return [random.randint(0, 1) for _ in range(60)]


def next_generation(grid):
    new_grid = copy.deepcopy(grid)
    for i, _ in enumerate(grid):
        for j, _ in enumerate(grid[i]):
            new_grid[i][j] = update_cell(grid, i, j)

    return new_grid

def update_cell(grid, i, j):
    neighbors = count_neighbors(grid, i, j)

    if grid[i][j]:
        if neighbors < 2 or neighbors > 3:
            return 0
    else:
        if neighbors == 3:
            return 1
    return grid[i][j]


def count_neighbors(grid, row, col):
    return sum(
        sum(row[col-1:col+2])
        for row in grid[row-1:row+2]
    ) - grid[row][col]


if __name__ == "__main__":
    main()

import numpy as np
from itertools import combinations
filename = "input.txt"
# filename = "test_input.txt"

file = open(filename).readlines()
file = [f.strip() for f in file]


def part_one():
    grid = [[f for f in l] for l in file]
    grid = expand(grid)
    galaxies = find_galaxies(grid)
    sum = 0
    for pair in combinations(galaxies, repeat=2):
        sum += find_distance(pair[0],pair[1])
    return

def part_two():
    grid = [[f for f in l] for l in file]
    empty = []
    # grid = expand(grid,i)
    empty = find_empty(grid)
    print(empty)
    galaxies = find_galaxies(grid)
    sum = 0
    for pair in combinations(galaxies, 2):
        i = pair[0]
        j = pair[1]
        sum += find_distance(i,j)
        empties_between = 0
        for e in empty[0]:
            if e in range(i[0], j[0]):
                empties_between += 1
        for e in empty[1]:
            if(i[1] > j[1]):
                if e in range(j[1], i[1]+1):
                    empties_between += 1
            else:
                if e in range(i[1], j[1]+1):
                    empties_between += 1
        sum += empties_between * 999999
    print(sum)
    return

def expand(grid, num_dupes=1):
    grid = np.array(grid)

    def process_and_expand(g):
        expanded = []
        for row in g:
            expanded.append(row)
            if '#' not in row:
                for i in range(num_dupes):
                    expanded.append(row)
        return np.array(expanded)

    expanded_grid = process_and_expand(grid)
    expanded_grid = expanded_grid.T
    expanded_grid = process_and_expand(expanded_grid)

    return expanded_grid.T.tolist()

def find_empty(grid):
    empty_rows = []
    empty_cols = []
    grid = np.array(grid)
    for row in range(len(grid)):
        if '#' not in grid[row]:
            empty_rows.append(row)
    grid = grid.T
    for row in range(len(grid)):
        if '#' not in grid[row]:
            empty_cols.append(row)
    return (empty_rows,empty_cols)


def find_galaxies(grid):
    coords = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                coords.append((i,j))
    return coords

def find_distance(i,j):
    return abs(i[0] - j[0]) + abs(i[1] - j[1])



def main():
    # part_one()
    part_two()

if __name__ == '__main__':
    main()
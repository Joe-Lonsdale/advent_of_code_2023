import numpy as np
filename = "input.txt"
# filename = "test_input.txt"

file = open(filename).readlines()
file = [f.strip() for f in file]


def part_one():
    grid = [[f for f in l] for l in file]
    grid = expand(grid)
    galaxies = find_galaxies(grid)
    sum = 0
    for i in galaxies:
        for j in galaxies:
            if i == j: continue
            sum += find_distance(i,j)
    print(sum/2)
    return

def part_two():
    return

def expand(grid):
    grid = np.array(grid)

    def process_and_expand(g):
        expanded = []
        for row in g:
            expanded.append(row)
            if '#' not in row:
                for i in range(1000000):
                    expanded.append(row)
        return np.array(expanded)

    expanded_grid = process_and_expand(grid)
    expanded_grid = expanded_grid.T
    expanded_grid = process_and_expand(expanded_grid)

    return expanded_grid.T.tolist()

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
    part_one()

if __name__ == '__main__':
    main()
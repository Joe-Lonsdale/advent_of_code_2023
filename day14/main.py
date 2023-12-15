# filename = "input.txt"
filename = "test_input.txt"

file = open(filename).readlines()
file = [f.strip() for f in file]

grid = [[o for o in line] for line in file]


def part_one():
    print(grid)
    # for i in range(len(grid)):
    #     for j in range(len(grid[i])):
    #         if grid[i][j] == 'O':
    #             slide_up(grid, i, j)
    # for i in range(len(grid)):
    #     for j in range(len(grid[i])):
    #         if grid[i][j] == 'O':
    #             slide_left(grid,i,j)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'O':
                slide_down(grid,i,j)
    # for i in range(len(grid)):
    #     for j in range(len(grid[i])):
    #         if grid[i][j] == 'O':
    #             slide_right(grid,i,j)
    print("\n\n")
    print(grid)
    print(get_load(grid))

    return

def slide_up(grid, i,j):
    if i == 0: return grid
    while(grid[i-1][j] == '.' and i > 0):
        grid[i-1][j] = 'O'
        grid[i][j] = '.'
        i = i-1
    return grid

def slide_down(grid, i,j):
    if i >= len(grid)-2: return grid
    while(grid[i+1][j] == '.' and i < len(grid)-2):
        grid[i+1][j] = 'O'
        grid[i][j] = '.'
        i = i+1
    return grid

def slide_left(grid, i,j):
    if j == 0: return grid
    while(grid[i][j-1] == '.' and j > 0):
        grid[i][j-1] = 'O'
        grid[i][j] = '.'
        j = j-1
    return grid

def slide_right(grid, i,j):
    if j >= len(grid)-2: return grid
    while(grid[i][j-1] == '.' and j < len(grid[0])-2):
        grid[i][j+1] = 'O'
        grid[i][j] = '.'
        j = j+1
    return grid

def get_load(grid):
    load = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'O':
                # grid[i][j] = len(grid) - i
                load += len(grid) - i
    return load
def part_two():
    return

def main():
    part_one()
    # part_two()

if __name__ == '__main__':
    main()
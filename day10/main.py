import os
filename = "input.txt"
# filename = "test_input.txt"

file = open(filename).readlines()
file = [f.strip() for f in file]
grid = []

def init_grid():
    for line in range(len(file)):
        x = []
        for l in range(len(file[line])):
            x.append(file[line][l])
            if file[line][l] == 'S':
                start = (line,l)
        grid.append(x)
    return start

def part_one():
    start = init_grid()
    loop = [start]
    loop_finished = False
    curr = start
    prev = None
    while not loop_finished:
        next = get_next(curr,prev)
        if next in loop:
            loop_finished = True
            continue
        loop.append(next)
        prev = curr
        curr = next
    isolated_loop = get_isolated_loop(grid,loop)
    loop_bounds = get_outside_loop_bounds(isolated_loop)
    inside_count = 0
    for i in loop_bounds:
        inside_count += i.count('.')
    print(inside_count)
    print(len(loop) / 2)
    return

def get_next(curr, prev):
    if grid[curr[0]][curr[1]] in "S|LJ" and curr[0] != 0 and grid[curr[0]-1][curr[1]] in "S|F7" and prev != (curr[0]-1,curr[1]):
        return (curr[0]-1,curr[1])
    if grid[curr[0]][curr[1]] in "S-J7" and curr[1] != 0 and grid[curr[0]][curr[1]-1] in "S-FL" and prev != (curr[0],curr[1]-1):
        return (curr[0],curr[1]-1)
    if grid[curr[0]][curr[1]] in "S|7F" and curr[0] != len(grid)-1 and grid[curr[0]+1][curr[1]] in "S|LJ" and prev != (curr[0]+1,curr[1]):
        return (curr[0]+1,curr[1])
    if grid[curr[0]][curr[1]] in "SLF-" and curr[1] != len(grid)-1 and grid[curr[0]][curr[1]+1] in "S-7J" and prev != (curr[0],curr[1]+1):
        return (curr[0],curr[1]+1)

def print_only_loop(grid,loop):
    for i in range(len(grid)):
        output = ""
        for j in range(len(grid[0])):
            if (i,j) in loop:
                output += grid[i][j]
            else:
                output += "."
        print(output)

def print_grid(grid):
    for i in range(len(grid)):
        output = ""
        for j in range(len(grid[0])):
            output += grid[i][j]
        print(output)

def get_isolated_loop(grid, loop):
    out = []
    for i in range(len(grid)):
        out.append([])
        for j in range(len(grid[0])):
            if (i,j) in loop:
                out[i].append(grid[i][j])
            else:
                out[i].append('.')
    return out

def get_outside_loop_bounds(loop):
    searching = [(0,0)]
    while len(searching) > 0:
        if loop[searching[0][0]][searching[0][1]] == '.':
            loop[searching[0][0]][searching[0][1]] = 'O'
            for x in [searching[0][0]-1,searching[0][0],searching[0][0]+1]:
                for y in [searching[0][1]-1,searching[0][1],searching[0][1]+1]:
                    if x >= 0 and x < len(loop) and y >= 0 and y < len(loop[0]) and (x,y) not in searching:
                        searching.append((x,y))
            searching.pop(0)
        else:
            searching.pop(0)
    return loop

def part_two():
    return


def main():
    part_one()

if __name__ == '__main__':
    main()
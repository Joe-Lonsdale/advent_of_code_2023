import os
# filename = "input.txt"
filename = "test_input.txt"

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
    print(len(loop) / 2)
    return

def get_next(curr, prev):
    if grid[curr[0]][curr[1]] in "S|LJ" and curr[0] != 0 and grid[curr[0]-1][curr[1]] in "S|F7" and prev != (curr[0]-1,curr[1]):
        return (curr[0]-1,curr[1])
    if grid[curr[0]][curr[1]] in "S-J7" and curr[1] != 0 and grid[curr[0]][curr[1]-1] in "S-FL" and prev != (curr[0],curr[1]-1):
        return (curr[0],curr[1]-1)
    if grid[curr[0]][curr[1]] in "S|7F" and curr[0] != len(grid)-1 and grid[curr[0]+1][curr[1]] in "S|LJ" and prev != (curr[0]+1,curr[1]):
        return (curr[0]+1,curr[1])
    if grid[curr[0]][curr[1]] in "SLF-" and curr[1] != len(grid[0])-1 and grid[curr[0]][curr[1]+1] in "S-7J" and prev != (curr[0],curr[1]+1):
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
    return loop

def break_out_of_inside(loop):
    insides = []
    for i in range(len(loop)):
        for j in range(len(loop[0])):
            insides.append((i,j))
    for x in insides:


def follow_pipe(grid, coord1, coord2, dir):
    match dir:
        case 'up':
            if grid[coord1[0] + 1][coord1[1]] in '7|J' and grid[coord2[0] + 1][coord2[1]] in 'F|L':
                return follow_pipe(grid, (coord1[0]+1,coord1[1]), (coord2[0]+1,coord2[1]), 'up')
            if grid[coord1[0] + 1][coord1[1]] == '-' and grid[coord2[0] + 1][coord2[1]] in '7':
                return follow_pipe(grid, (coord1[0]+1,coord1[1]), (coord2[0]+1,coord2[1]), 'left')
            if grid[coord1[0] + 1][coord1[1]] == 'F' and grid[coord2[0] + 1][coord2[1]] == '-':
                return follow_pipe(grid, (coord1[0]+1,coord1[1]), (coord2[0]+1,coord2[1]), 'right')


def part_two():
    start = init_grid()
    loop = [start]
    loop_finished = False
    curr = start
    prev = None
    while not loop_finished:
        print(get_next(curr,prev))
        print(grid[get_next(curr,prev)[0]][get_next(curr,prev)[1]])
        next = get_next(curr,prev)
        if next in loop:
            loop_finished = True
            continue
        loop.append(next)
        prev = curr
        curr = next
    isolated_loop = get_isolated_loop(grid,loop)
    print_grid(isolated_loop)
    loop_bounds = get_outside_loop_bounds(isolated_loop)
    print(loop_bounds)
    inside_count = 0
    for i in loop_bounds:
        inside_count += i.count('.')
    print(inside_count)
    return


def main():
    part_two()

if __name__ == '__main__':
    main()
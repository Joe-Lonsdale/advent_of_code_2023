# filename = "input.txt"
filename = "test_input.txt"
import random

file = open(filename).readlines()
file = [f.strip() for f in file]
grid = [[int(l) for l in line] for line in file]

def part_one():
    full_paths = []
    x,y = [0,0]
    paths = get_possible_paths(x,y,[[0,0]])
    while len(paths):
        print(f"{len(paths)} paths remaining  |  found {len(full_paths)} possible paths", end="\r")
        path = paths.pop(0)
        new_paths = get_possible_paths(path[-1][0], path[-1][1], path)
        # print(f"checking {len(new_paths)} new paths")
        # for path in paths:
        #     print(path)
        #     print("\n")

        for p in new_paths:
            if p[-1] == [len(grid[0])-1, len(grid)-1]:
                full_paths.append(p)
                # print("\n###################")
                # print(p)
                # print(get_loss(p))
                # print("###################\n")
            else:
                found = False
                for i in paths:
                    if p[-1] in i and p[-1] != [0,0]:
                        found = True
                        if(get_loss(p) < get_loss(i[:i.index(p[-1])])):
                            paths.remove(i)
                            paths.append(p)
                        break
                if not found:
                    paths.append(p)

    best = 9999999999
    best_index = 0
    for p in range(len(full_paths)):
        if get_loss(full_paths[p]) < best:
            best_index = p
            best = get_loss(full_paths[p])

    print_path(full_paths[best_index])
    print(best)

def get_possible_paths(x,y,path):
    possible = []
    for i in range(-1,2):
        for j in range(-1,2):
            if [i,j] not in [[-1,0],[1,0],[0,-1],[0,1]]: continue
            if [x+i,y+j] not in path and x+i in range(0,len(grid[0])) and y+j in range(0,len(grid)) and not is_too_straight(i,j,path):
                p = path.copy()
                p.append([x+i, y+j])
                possible.append(p)
    return possible

def is_too_straight(i,j,path):
    if len(path) < 3: return False
    match(i):
        case -1:
            return path[-1][0] - path[-3][0] == -2
        case 1:
            return path[-1][0] - path[-3][0] == 2
    match(j):
        case -1:
            return path[-1][1] - path[-3][1] == -2
        case 1:
            return path[-1][1] - path[-3][1] == 2
    return False

def print_path(path):
    output = ""
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if [j,i] in path:
                output+="#"
            else: output+= "."
        output+="\n"
    print(output)


def get_loss(path):
    return sum([grid[y][x] for x,y in path]) - grid[0][0]

def part_two():
    return

def main():
    part_one()
    # part_two()

if __name__ == '__main__':
    main()
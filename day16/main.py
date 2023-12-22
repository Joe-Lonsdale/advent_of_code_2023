filename = "input.txt"
# filename = "test_input.txt"

file = open(filename).readlines()
file = [f.strip() for f in file]

grid = [[l for l in line] for line in file]
dirs = [['' for _ in line] for line in file]


def part_one():
    for dir in get_next_dirs('r', grid[0][0]):
        do_path(dir,0,0)
    count = sum([sum([1 for x in dir if len(x) != 0]) for dir in dirs])
    print([(['#' if len(x) != 0 else '.' for x in dir]) for dir in dirs])
    print(count)
    return

def do_path(dir_init, y_init, x_init):
    moves_to_do = [(dir_init,y_init,x_init)]
    while len(moves_to_do):
        dir,y,x = moves_to_do[0]
        moves_to_do = moves_to_do[1:]
        dirs[y][x] += dir
        match(dir):
            case 'u':
                if y - 1 >= 0:
                    for d in get_next_dirs(dir, grid[y - 1][x]):
                        if d not in dirs[y-1][x]:
                            moves_to_do.append((d,y-1,x))
            case 'd':
                if y + 1 <= len(grid)-1:
                    for d in get_next_dirs(dir, grid[y + 1][x]):
                        if d not in dirs[y+1][x]:
                            moves_to_do.append((d,y+1,x))

            case 'l':
                if x - 1 >= 0:
                    for d in get_next_dirs(dir, grid[y][x-1]):
                        if d not in dirs[y][x-1]:
                            moves_to_do.append((d,y,x-1))

            case 'r':
                if x + 1 <= len(grid[0])-1:
                    for d in get_next_dirs(dir, grid[y][x+1]):
                        if d not in dirs[y][x+1]:
                            moves_to_do.append((d,y,x+1))


def get_next_dirs(dir,symbol):
    match(symbol):
        case '.':
            return dir
        case '|':
            if dir in 'ud':
                return dir
            return 'ud'
        case '-':
            if dir in 'lr':
                return dir
            return 'lr'
        case '/':
            match(dir):
                case 'l':
                    return 'd'
                case 'd':
                    return 'l'
                case 'r':
                    return 'u'
                case 'u':
                    return 'r'
        case '\\':
            match(dir):
                case 'l':
                    return 'u'
                case 'u':
                    return 'l'
                case 'r':
                    return 'd'
                case 'd':
                    return 'r'

def part_two():
    global grid,dirs
    best_count = 0
    for y in range(len(grid)):
        reset_grid()
        for dir in get_next_dirs('r', grid[y][0]):
            do_path(dir,y,0)
        count = sum([sum([1 for x in dir if len(x) != 0]) for dir in dirs])
        if count > best_count: best_count = count
        reset_grid()
        for dir in get_next_dirs('l', grid[y][-1]):
            do_path(dir,y,len(grid[y])-1)
        count = sum([sum([1 for x in dir if len(x) != 0]) for dir in dirs])
        if count > best_count: best_count = count
    for x in range(len(grid[0])):
        reset_grid()
        for dir in get_next_dirs('d', grid[0][x]):
            do_path(dir,0,x)
        count = sum([sum([1 for x in dir if len(x) != 0]) for dir in dirs])
        if count > best_count: best_count = count
        reset_grid()
        for dir in get_next_dirs('u', grid[-1][x]):
            do_path(dir,len(grid[0])-1,x)
        count = sum([sum([1 for x in dir if len(x) != 0]) for dir in dirs])
        if count > best_count: best_count = count
    print([(['#' if len(x) != 0 else '.' for x in dir]) for dir in dirs])
    print(best_count)
    return

def reset_grid():
    global grid,dirs
    grid = [[l for l in line] for line in file]
    dirs = [['' for _ in line] for line in file]

def main():
    # part_one()
    part_two()

if __name__ == '__main__':
    main()
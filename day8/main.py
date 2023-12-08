from numpy import lcm
filename = "input.txt"
# filename = "test_input.txt"

file = open(filename, "r")
instructions = {}
dirs = ""
line_count = 0
for line in file:
    line = line.strip()
    if line_count == 0:
        dirs = line
        line_count += 1
    elif line != "":
        l = line.split(' = ')
        leftright = l[1].split(', ')
        instructions[l[0]] = (leftright[0][1:],leftright[1][:-1])


def part_one():
    curr = 'AAA'
    dir_pointer = 0
    steps = 0
    while(not curr != 'ZZZ'):
        if(dir_pointer >= len(dirs)): dir_pointer = 0
        if(dirs[dir_pointer] == 'L'):
            curr = instructions[curr][0]
        else:
            curr = instructions[curr][1]
        steps += 1
        dir_pointer += 1

    print(steps)

def part_two():
    currs = []

    for key in instructions.keys():
        if key[-1] == 'A':
            currs.append(key)

    def is_finished(nodes):
        count = 0
        for node in nodes:
            if node[-1] == 'Z':
                count += 1
        return count == len(nodes)

    fins = {}

    dir_pointer = 0
    steps = 0
    while (len(fins.keys()) != len(currs)):
        if(dir_pointer >= len(dirs)): dir_pointer = 0
        currs = [instructions[curr][dirs[dir_pointer] == 'R'] for curr in currs]
        steps += 1
        dir_pointer += 1
        for curr in currs:
            if(curr[-1] == 'Z'):
                fins[curr] = steps
    print(fins)
    print(lcm.reduce(list(fins.values())))


def main():
    part_two()

if __name__ == '__main__':
    main()
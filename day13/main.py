import numpy as np
filename = "input.txt"
# filename = "test_input.txt"

file = open(filename).readlines()
file = [f.strip() for f in file]

def load_patterns():
    output = [[]]
    for line in file:
        if line == '':
            output.append([])
        else:
            output[-1].append([1 if l == '#' else 0 for l in line ])

    return [np.array(o) for o in output]

def get_row_reflection(pattern, pt1=True):
    row_pointer = 1
    while row_pointer < pattern.shape[0]:
        top = pattern[:row_pointer,:]
        bot = pattern[row_pointer:,:]
        if top.shape[0] > bot.shape[0]:
            top = top[-bot.shape[0]:,:]
        else:
            bot = bot[:top.shape[0],:]
        diff = 0
        for i in range(top.shape[0]):
            for j in range(top.shape[1]):
                diff += abs(top[i][j] - np.flip(bot,0)[i][j])
        if diff == 1 and not pt1:
            return row_pointer
        if diff == 0 and pt1:
            return row_pointer
        row_pointer += 1
    return None

def get_col_reflection(pattern,pt1=True):
    col_pointer = 1
    while col_pointer < pattern.shape[1]:
        left = pattern[:,:col_pointer]
        right = pattern[:,col_pointer:]
        if left.shape[1] > right.shape[1]:
            left = left[:,-right.shape[1]:]
        else:
            right = right[:,:left.shape[1]]
        diff = 0
        for i in range(left.shape[0]):
            for j in range(left.shape[1]):
                diff += abs(left[i][j] - np.flip(right,1)[i][j])
        if diff == 1 and not pt1:
            return col_pointer
        if diff == 0 and pt1:
            return col_pointer
        col_pointer += 1
    return None

def part_one():
    patterns = load_patterns()
    sum = 0
    for x in patterns:

        val = get_row_reflection(x)
        if val == None:
            val = get_col_reflection(x)
            sum += val
        else:
            sum += 100 * val
    print(sum)
    return

def part_two():
    patterns = load_patterns()
    sum = 0
    for x in patterns:

        val = get_row_reflection(x, False)
        if val == None:
            val = get_col_reflection(x, False)
            sum += val
        else:
            sum += 100 * val
    print(sum)
    return

def main():
    part_one()
    part_two()

if __name__ == '__main__':
    main()
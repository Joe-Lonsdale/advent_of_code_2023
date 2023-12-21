filename = "input.txt"
# filename = "test_input.txt"

file = open(filename).readlines()
file = [f.strip() for f in file]
file = [f for f in file[0].split(',')]

def HASH(val, input):
    return ((val + ord(input)) * 17) % 256

def part_one():
    print(file)
    tot = 0
    for x in file:
        val = 0
        for y in x:
            val = HASH(val, y)
        tot += val
    print(tot)
    return

def part_two():
    return

def main():
    part_one()
    # part_two()

if __name__ == '__main__':
    main()
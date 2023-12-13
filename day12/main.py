import re
import itertools

# filename = "input.txt"
filename = "test_input.txt"

file = open(filename).readlines()
file = [f.strip() for f in file]

lines = []

def part_one():
    for line in file:
        l = line.split(' ')
        lines.append((l[0], [int(x) for x in l[1].split(',')]))
    print(get_possible_arrangements(lines[2][0], lines[2][1]))
    for x in lines:
        print(get_possible_arrangements(x[0], x[1]))
    return

def get_possible_arrangements(springs, records):
    matches = re.finditer(r'([\?\#]+)', springs)
    results = [match.span(1) for match in matches]
    contiguous = []
    for i,j in results:
        x = springs[i:j]
        contiguous.extend([[x[lower:upper],i+lower,i+upper] for lower,upper in itertools.combinations(range(0,len(x)+1), 2) if upper-lower >= records[0]])
    contiguous = [c for c in contiguous if c]
    if(contiguous):
        new_set = set([springs[upper+1:] for _,_,upper in contiguous if len(springs[upper+1:])])
    if(len(records) == 1 and len(contiguous)):
        return 1
    new_set = set([springs[upper+1:] for _,_,upper in contiguous if len(springs[upper+1:])])
    return sum([get_possible_arrangements(x, records[1:]) for x in new_set])
def part_two():
    return

def main():
    part_one()
    # part_two()

if __name__ == '__main__':
    main()
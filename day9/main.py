filename = "input.txt"
# filename = "test_input.txt"

file = open(filename, "r")

def part_one():
    sequences = []
    for line in file:
        sequences.append([int(x) for x in line.split(' ')])
    total = 0
    for seq in sequences:
        seqs = break_down_seq(seq)
        seqs.append(seq)
        for s in seqs:
            print(s)
            total += s[-1]
        print("==========================================")
    print(total)
    return

def part_two():
    sequences = []
    for line in file:
        sequences.append([int(x) for x in line.split(' ')])
    total = 0
    for seq in sequences:
        seqs = break_down_seq(seq)
        seqs.append(seq)
        subtotal = 0
        for i in range(1, len(seqs)):
            print(seqs[i])
            subtotal = seqs[i][0] - subtotal
            print(subtotal)
        total += subtotal
        print("==========================================")
    print(total)
    return

def break_down_seq(seq):
    diffs = [seq[i] - seq[i-1] for i in range(1,len(seq))]
    if(diffs.count(0)) == len(diffs):
        return [diffs]
    ret = break_down_seq(diffs)
    ret.append(diffs)
    return ret




def main():
    part_two()

if __name__ == '__main__':
    main()
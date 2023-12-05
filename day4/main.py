filename = "input.txt"

file = open(filename, "r")

count = 0
file_arr = []
for line in file:
    file_arr.append(line)

file = file_arr
multiples = {str(i):1 for i in range(len(file))}

for line in range(len(file)):
    x = file[line].split(': ')[1].split(' | ')
    winning = x[0]
    nums = x[1]
    nums = [int(x.strip()) for x in nums.split(' ') if x != '']
    winning = [int(x.strip()) for x in winning.split(' ') if x != '']
    for z in range(multiples[str(line)]):
        lineWinning = 0
        for winning_num in winning:
            if winning_num in nums:
                lineWinning += 1
        for i in range(1, lineWinning+1):
            multiples[str(line+i)] += 1

for i in multiples:
    count+= multiples[i]

print(count)
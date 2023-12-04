filename = "input.txt"

file = open(filename, "r")
chars = []
i = 0

for line in file:
    chars.append([])
    for char in line.strip():
        chars[i].append(char)
    i += 1

nums = [0,1,2,3,4,5,6,7,8,9]
nums = [str(num) for num in nums]


indices_of_nums = []

for i in range(len(chars)):
    for j in range(len(chars[0])):
        if chars[i][j] in nums:
            indices_of_nums.append([i,j])

grouped_indices = []
prev_num = None
gear_coords = []

def gear_around_coord(x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0: continue
            if x+i >= len(chars) or x+i < 0 or y+j >= len(chars[0]) or y+j < 0: continue
            if chars[x+i][y+j] == '*':
                return [x+i,y+j]

    return False

def get_num_from_coords(coords):
    num = ''
    for coord in coords:
        num += chars[coord[0]][coord[1]]
    return int(num)


for indice in indices_of_nums:
    if prev_num and (grouped_indices[-1][-1][1] == indice[1] - 1 and grouped_indices[-1][-1][0] == indice[0]):
        grouped_indices[-1].append(indice)
        prev_num = chars[indice[0]][indice[1]]
    else:
        grouped_indices.append([indice])
        prev_num = chars[indice[0]][indice[1]]

engine_sum = 0

nums_with_gears = []
for group in grouped_indices:
    part_of_engine = False
    for coord in group:
        gear_coord = gear_around_coord(coord[0],coord[1])
        if gear_coord:
            nums_with_gears.append((get_num_from_coords(group), gear_coord))

counts = dict()
for pair in nums_with_gears:
    if str(pair[1]) not in counts: counts[str(pair[1])] = 1
    else: counts[str(pair[1])] = counts[str(pair[1])] + 1

gear_pairs = dict()
for count in counts.keys():
    if counts[count] == 2:
        gear_pairs[count] = []

for num in nums_with_gears:
    if str(num[1]) in gear_pairs.keys():
        gear_pairs[str(num[1])].append(num[0])

for gear in gear_pairs.keys():
    print(gear)
    engine_sum += gear_pairs[gear][0] * gear_pairs[gear][1]
print(engine_sum)



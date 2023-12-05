filename = "input.txt"

file = open(filename).read().splitlines()

init_seeds = []
seed_to_soil = {}
soil_to_fert = {}
fert_to_water = {}
water_to_light = {}
light_to_temp = {}
temp_to_humid = {}
humid_to_location = {}
current_map = None

count = 0
for line in file:
    print(f"Line {count}")
    count+=1
    if(line.startswith('seeds')):
        init_seeds = [x for x in line.split(': ')[1].split(' ')]
        continue
    if(line == ''): continue
    if(line.startswith('seed')):
        current_map = seed_to_soil
        continue
    if(line.startswith('soil')):
        current_map = soil_to_fert
        continue
    if(line.startswith('fert')):
        current_map = fert_to_water
        continue
    if(line.startswith('water')):
        current_map = water_to_light
        continue
    if(line.startswith('light')):
        current_map = light_to_temp
        continue
    if(line.startswith('temp')):
        current_map = temp_to_humid
        continue
    if(line.startswith('humid')):
        current_map = humid_to_location
        continue
    line = line.split(' ')
    source = int(line[0])
    dest = int(line[1])
    length = int(line[2])
    for i in range(source, source + length + 1):
        if(i): print((i - source) / (length + 1))
        for j in range(dest, dest + length + 1):
            current_map[str(i)] = str(j)

def get_loc_from_seed(seed):
    return humid_to_location[temp_to_humid[light_to_temp[water_to_light[fert_to_water[soil_to_fert[seed_to_soil[seed]]]]]]]

lowest = None
lowest_seed = None
for i in init_seeds:
    loc = int(get_loc_from_seed(i))
    if lowest == None or loc < lowest:
        lowest = loc
        lowest_seed = i

print(lowest_seed)

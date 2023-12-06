filename = "input.txt"
# filename = "test_input.txt"

file = open(filename).read().splitlines()

init_seeds = []
seed_to_soil = {}
soil_to_fert = {}
fert_to_water = {}
water_to_light = {}
light_to_temp = {}
temp_to_humid = {}
humid_to_location = {}

maps = [seed_to_soil, soil_to_fert, fert_to_water, water_to_light, light_to_temp, temp_to_humid, humid_to_location]
current_map = None

count = 0
for line in file:
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
    source = int(line[1])
    dest = int(line[0])
    length = int(line[2])
    current_map[f'{source}-{source+length}'] = dest

lowest = None
lowest_seed = None

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

def seed_to_loc(seed):
    curr_index = int(seed)
    for x in maps:
        print(namestr(x, globals()))
        print(x)
        found = False
        for key in x.keys():
            if found: continue
            k = [int(k) for k in key.split('-')]
            if(curr_index >= k[0] and curr_index <= k[1]):
                print(k)
                diff = abs(curr_index - k[0])
                curr_index = x[key] + diff
                found = True
        print(curr_index)

    return curr_index

def part_one():
    lowest = None
    lowest_seed = None
    for seed in init_seeds:
        print(f'seed: {seed}')
        new = seed_to_loc(seed)
        if not lowest or new < lowest:
            print(new)
            lowest_seed = seed
            lowest = new
        print('===================')
    print(lowest)

def part_two():
    lowest = None
    lowest_seed = None
    for i in range(0,len(init_seeds),2):
        seeds = [int(init_seeds[i]) + x for x in range(int(init_seeds[i+1]))]
        for seed in seeds:
            print(f'seed: {seed}')
            new = seed_to_loc(seed)
            if not lowest or new < lowest:
                lowest_seed = seed
                lowest = new
            print('===================')
    print(lowest)



def main():
    # part_one()
    part_two()


if __name__ == '__main__':
    main()
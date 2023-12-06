times = [57726992]
records = [291117211762026]


ways_to_win = [0]

def do_race(press_time, max_time):
    return(press_time) * (max_time - press_time)


for i in range(len(ways_to_win)):
    for x in range(times[i]+1):
        dist = do_race(x,times[i])
        if dist > records[i]:
            ways_to_win[i] += 1

total = 1

for x in ways_to_win:
    total *= x
print(total)



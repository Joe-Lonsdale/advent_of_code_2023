times = [57726992]
records = [291117211762026]

ways_to_win = [0]

def do_race(press_time, max_time):
    dist = 0
    speed = 0
    for i in range(max_time):
        if i < press_time:
            speed += 1
        else:
            dist += speed
    return dist


for i in range(len(ways_to_win)):
    for x in range(times[i]+1):
        dist = do_race(x,times[i])
        if dist > records[i]:
            ways_to_win[i] += 1

total = 1

for x in ways_to_win:
    total *= x
print(total)



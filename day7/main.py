import functools
# filename = "input.txt"
filename = "test_input.txt"

file = open(filename, "r")

hands = []

for line in file:
    hands.append([line.split(' ')[0], int(line.split(' ')[1])])

def get_score(hand):
    if(get_n(5,hand[0])): return 50
    if(get_n(4,hand[0])): return 49
    if(get_full_house(hand[0])): return 48
    if(get_n(3,hand[0])): return 47
    if(get_two_pair(hand[0])): return 46
    if(get_n(2,hand[0])): return 45
    return get_high_card(hand[0])

def sorting(a,b):
    a_score = get_score(a)
    b_score = get_score(b)
    if(a_score != b_score):
        return a_score - b_score
    a_num = int(''.join([str(f'{get_index(i):02}') for i in a[0]]))
    b_num = int(''.join([str(f'{get_index(i):02}') for i in b[0]]))
    print(a_num, b_num, a, b)
    return a_num - b_num

def get_index(letter):
    match(ord(letter)):
        case 50: return 0
        case 51: return 1
        case 52: return 2
        case 53: return 3
        case 54: return 4
        case 55: return 5
        case 56: return 6
        case 57: return 7
        case 58: return 8
        case 59: return 9
        case 84: return 10
        case 74: return 11
        case 81: return 12
        case 75: return 13
        case 65: return 14

def get_n(n, hand):
    counts = [0]*15
    for h in hand:
        counts[get_index(h)] += 1
    if(n in counts): return True
    return False

def get_full_house(hand):
    counts = [0]*15
    for h in hand:
        counts[get_index(h)] += 1
    if(2 in counts and 3 in counts): return True
    return False

def get_two_pair(hand):
    counts = [0]*15
    for h in hand:
        counts[get_index(h)] += 1
    if(counts.count(2) == 2): return True
    return False

def get_high_card(hand):
    counts = {str(x):0 for x in range(14,-1,-1)}
    for h in hand:
        counts[str(get_index(h))] += 1
    for x in range(14,-1,-1):
        if counts[str(x)] != 0:
            return x

cmp = functools.cmp_to_key(sorting)
hands = sorted(hands, key=cmp)

sum = 0
for i in range(len(hands)):
    print(sum)
    print(hands[i])
    sum += (i+1)*hands[i][1]
print(sum)
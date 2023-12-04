filename = "input.txt"

file = open(filename, "r")


red_limit = 12
green_limit = 13
blue_limit = 14
power_sum = 0

for line in file:
    split_line = line.split(': ')
    id = split_line[0].split(' ')[1]
    rounds = split_line[1].split('; ')
    most_blues = 0
    most_greens = 0
    most_reds = 0

    for round in rounds:
        moves = round.split(',')
        for move in moves:
            print(move)
            match move.strip().split(' ')[1]:
                case 'blue':
                    if int(move.strip().split(' ')[0]) > most_blues:
                        most_blues = int(move.strip().split(' ')[0])
                case 'red':
                    if int(move.strip().split(' ')[0]) > most_reds:
                        most_reds = int(move.strip().split(' ')[0])
                case 'green':
                    if int(move.strip().split(' ')[0]) > most_greens:
                        most_greens = int(move.strip().split(' ')[0])
    print(f'blues: {most_blues}')
    print(f'greens: {most_greens}')
    print(f'reds: {most_reds}')
    print(line)
    power_sum += most_blues * most_greens * most_reds
print(power_sum)
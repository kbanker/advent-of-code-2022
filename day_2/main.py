
f = open('input.txt')
lines = [x.replace('\n','') for x in f]
f.close()

def part1():
    shape_score = { 'X': 1, 'Y': 2, 'Z': 3}
    points = 0
    for line in lines:
        opp, shape = line.split(' ')
        points += shape_score[shape]

        if shape=='X': shape = 'A'
        elif shape=='Y': shape = 'B'
        elif shape=='Z': shape = 'C'

        if shape == opp:
            points += 3 # draw
        elif (shape == 'A' and opp == 'B') or (shape == 'B' and opp == 'C') or (shape == 'C' and opp == 'A'):
            points += 0 # loss
        else:
            points += 6 # win

    print(points)

def part2():
    shape_score = { 'X': 1, 'Y': 2, 'Z': 3}
    points = 0
    for line in lines:
        opp, result = line.split(' ')

        if result=='X':
            #lose
            points += 0
            if opp == 'A': points += 3 
            elif opp == 'B': points += 1
            else: points += 2

        elif result=='Y':
            #draw 
            points += 3
            if opp == 'A': points += 1 
            elif opp == 'B': points += 2
            else: points += 3
        else:
            #win
            points += 6
            if opp == 'A': points += 2 
            elif opp == 'B': points += 3
            else: points += 1
    print(points)

part2()


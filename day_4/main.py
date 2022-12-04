f = open('input.txt')
lines = [x.replace('\n','') for x in f]
f.close()

def part1():
    total = 0
    for line in lines:
        first, second = line.split(',')
        first = [int(x) for x in first.split('-')]
        second = [int(x) for x in second.split('-')]
        if (first[0] <= second[0] and first[1] >= second[1]) or (first[0] >= second[0] and first[1] <= second[1]):
            total += 1
    print(total)

def part2():
    total = 0
    for line in lines:
        first, second = line.split(',')
        first = [int(x) for x in first.split('-')]
        second = [int(x) for x in second.split('-')]
        if (first[0] <= second[0] and first[1] >= second[0]) or (first[0] >= second[0] and first[0] <= second[1]):
            total += 1
    print(total)

part2()


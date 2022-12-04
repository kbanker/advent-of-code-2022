f = open('input.txt')
lines = [x.replace('\n','') for x in f]
f.close()

def part1():
    priority = [x for x in ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
    total = 0
    for line in lines:
        first = line[0:int(len(line)/2)]
        second = line[int(len(line)/2):]
        for x in first:
            if x in second:
                total += priority.index(x)
                #print(x, priority.index(x), total)
                break
    print(total)

def part2():
    priority = [x for x in ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
    total = 0
    for i in range(0, len(lines), 3):
        first = lines[i]
        second = lines[i + 1]
        third = lines[i + 2]
        for x in first:
            if x in second and x in third:               
                total += priority.index(x)
                break
    print(total)

part2()


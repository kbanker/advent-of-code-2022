f = open('input.txt')
lines = [x.replace('\n','') for x in f]
f.close()

def part1():
    line = lines[0]
    index = 3
    buffer = [x for x in line[index-4:4]]
    for i in range(index, len(line)):
        buffer = line[i-3:i+1]
        ct = 0
        for char in buffer: 
            if buffer.count(char) == 1:
                ct += 1
        if ct >= 3:
            index = i
            #print(ct, buffer)
            break
    print(index + 1, buffer)

def part2():
    line = lines[0]
    index = 13
    buffer = [x for x in line[index-14:14]]
    for i in range(index, len(line)):
        buffer = line[i-13:i+1]
        ct = 0
        for char in buffer: 
            if buffer.count(char) == 1:
                ct += 1
        if ct >= 13:
            index = i
            #print(ct, buffer)
            break
    print(index + 1, buffer)


part2()


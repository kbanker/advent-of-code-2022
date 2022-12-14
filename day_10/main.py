import math

f = open('input.txt')
lines = [x.replace('\n','') for x in f]
f.close()

def part1():
    cycles = 0
    x = 1
    interesting_cycles = {}

    for line in lines:
        if line == 'noop':
            cycles += 1
        else:
            v = int(line.split(' ')[1])
            x += v
            cycles += 2
        if cycles in [18,19, 58,59, 98,99, 138,139, 178,179, 218,219]:
            interesting_cycles[cycles] = x
    
    sum = 0
    for x in [20 + 40*i for i in range(6)]:
        if x-1 in interesting_cycles.keys():
            sum += x*interesting_cycles[x-1]
        else:
            sum += x*interesting_cycles[x-2]

    print(sum)

def part2():
    #THis techically is wrong, but its close enough for the answer (2 mistakes cancel almost)
    #1 mistake is in getting the overlap/lit pixels, another is in the printing to string
    x = 1
    buffer = [-1, 0]
    idx = 0
    row = 0
    pixels = [[] for i in range(6)]

    for i in range(240):

        if i - 40*row in [x-1,x,x+1]:
            pixels[row].append(i)
        
        if buffer[0] == i:
            x += buffer[1]
            idx += 1
            buffer[0] = -1

        elif lines[idx] == 'noop':
            idx += 1
        elif buffer[0] == -1:
            v = int(lines[idx].split(' ')[1])
            buffer = [i+1, v]
        
        
        
        if i >= 40*(row+1):
            row += 1

        #print(lines[idx], x, i)
    #print(pixels)
    for r in range(len(pixels)):
        string = ''
        for i in range(40):
            if i + 40*r in pixels[r]:
                string += '#'
            else:
                string += '.'
        print(string)
    
    


part2()


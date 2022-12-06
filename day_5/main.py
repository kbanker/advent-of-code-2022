f = open('input.txt')
lines = [x.replace('\n','') for x in f]
f.close()

def part1():
    total = 0
    rows = []
    commands = []
    numCols = 0
    for line in lines:
        if 'move' in line:
            f_ind = line.index('from')
            t_ind = line.index('to')
            #print(int(line[5:7]))

            commands.append([int(line[5:7]), int(line[f_ind+5]) -1 , int(line[t_ind+3]) -1])
        elif '[' in line:
            rows.append(line)
        elif len(line) == 0:
            pass
        else:
            cols = [int(x) for x in line.split(' ') if len(x) > 0]
            numCols = cols[-1]
    
    columns = [[] for x in range(numCols)]

    for row in rows:
        for i in range(numCols):
            if row[4*i] == '[':
                columns[i].append(row[4*i + 1])

    for command in commands:
        for i in range(command[0]):
            obj = columns[command[1]].pop(0)
            columns[command[2]].insert(0, obj)

    print(''.join([x[0] for x in columns]))

def part2():
    rows = []
    commands = []
    numCols = 0
    for line in lines:
        if 'move' in line:
            f_ind = line.index('from')
            t_ind = line.index('to')
            #print(int(line[5:7]))

            commands.append([int(line[5:7]), int(line[f_ind+5]) -1 , int(line[t_ind+3]) -1])
        elif '[' in line:
            rows.append(line)
        elif len(line) == 0:
            pass
        else:
            cols = [int(x) for x in line.split(' ') if len(x) > 0]
            numCols = cols[-1]
    
    columns = [[] for x in range(numCols)]

    for row in rows:
        for i in range(numCols):
            if row[4*i] == '[':
                columns[i].append(row[4*i + 1])

    for command in commands:
        objs = []
        for i in range(command[0]):
            objs.append(columns[command[1]].pop(0))
        objs.reverse()
        for obj in objs:
            columns[command[2]].insert(0, obj)

    print(''.join([x[0] for x in columns]))

part2()


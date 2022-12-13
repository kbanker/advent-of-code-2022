f = open('input.txt')
lines = [x.replace('\n','') for x in f]
f.close()

def part1():
    cwd = [' ']
    dir_sizes = {}
    for line in lines:
        if line[0] == '$':
            if line[2:4] == 'cd':              
                dir = line.split(' ')[2]
                if dir == '..':
                    cwd.pop()
                elif dir == '/':
                    cwd = [' ']
                else:
                    cwd.append(dir)
            elif line[2:4] == 'ls':
                #print(cwd)
                pass
        else:
            size, name = line.split(' ')
            if size != 'dir':
                size = int(size)
                for i in range(1,len(cwd) + 1):
                    wd_str = '/'.join(cwd[0:i])
                    dir_sizes[wd_str] = dir_sizes.get(wd_str, 0) + size
    total = 0
    for dir_size in dir_sizes.values():
        if dir_size <= 100000:
            total += dir_size
            #print(dir_size)
    print(total)



def part2():
    cwd = [' ']
    dir_sizes = {}
    for line in lines:
        if line[0] == '$':
            if line[2:4] == 'cd':              
                dir = line.split(' ')[2]
                if dir == '..':
                    cwd.pop()
                elif dir == '/':
                    cwd = [' ']
                else:
                    cwd.append(dir)
            elif line[2:4] == 'ls':
                #print(cwd)
                pass
        else:
            size, name = line.split(' ')
            if size != 'dir':
                size = int(size)
                for i in range(1,len(cwd) + 1):
                    wd_str = '/'.join(cwd[0:i])
                    dir_sizes[wd_str] = dir_sizes.get(wd_str, 0) + size
    
    unused = 70000000 - dir_sizes[' ']
    needed = 30000000 - unused

    min_dir = 70000000
    for dir_size in dir_sizes.values():
        if dir_size >= needed:
            min_dir = min(dir_size, min_dir)

    print(min_dir)
part2()


f = open('input.txt')
lines = [x.replace('\n','') for x in f]
f.close()

def part1():
    tail_positions = []
    h_x = 0
    h_y = 0
    t_x = 0
    t_y = 0

    for line in lines:
        if line[0] == 'R':
            for i in range(int(line[2:])):
                h_x += 1
                t_x, t_y = resolve_tail(t_x, t_y, h_x, h_y)
                tail_positions.append((t_x, t_y))
                
        elif line[0] == 'L':
            for i in range(int(line[2:])):
                h_x -= 1
                t_x, t_y = resolve_tail(t_x, t_y, h_x, h_y)
                tail_positions.append((t_x, t_y))

        elif line[0] == 'U':
            for i in range(int(line[2:])):
                h_y += 1
                t_x, t_y = resolve_tail(t_x, t_y, h_x, h_y)
                tail_positions.append((t_x, t_y))

        elif line[0] == 'D':
            for i in range(int(line[2:])):
                h_y -= 1
                t_x, t_y = resolve_tail(t_x, t_y, h_x, h_y)
                tail_positions.append((t_x, t_y))
    
        #print(t_x, t_y)
    print(len(set(tail_positions)))

def resolve_tail(t_x, t_y, h_x, h_y):

    x_resolved = False
    y_resolved = False

    pos = [0, 0]

    if t_x >= h_x - 1 and t_x <= h_x + 1:
        pos[0] = t_x
        x_resolved = True
    if t_y >= h_y - 1 and t_y <= h_y + 1:
        pos[1] = t_y
        y_resolved = True
    
    if not x_resolved and y_resolved:
        if t_y == h_y:
            pos[0] = t_x + int((h_x - t_x)/abs(h_x - t_x))
            x_resolved = True
        else:
            pos[0] = t_x + int((h_x - t_x)/abs(h_x - t_x))
            pos[1] = t_y + int((h_y - t_y)/abs(h_y - t_y))
            x_resolved = True
    
    if not y_resolved and x_resolved:
        if t_x == h_x:
            pos[1] = t_y + int((h_y - t_y)/abs(h_y - t_y))
            y_resolved = True
        else:
            pos[0] = t_x + int((h_x - t_x)/abs(h_x - t_x))
            pos[1] = t_y + int((h_y - t_y)/abs(h_y - t_y))
            y_resolved = True
    
    if not y_resolved and not x_resolved:
        pos[0] = t_x + (h_x - t_x)/abs(h_x - t_x)
        pos[1] = t_y + (h_y - t_y)/abs(h_y - t_y)
        x_resolved = True    
        y_resolved = True
    
    return pos


def part2():
    tail_positions = []
    h_x = 0
    h_y = 0
    knots_pos = [[0,0] for x in range(9)]

    for line in lines:
        if line[0] == 'R':
            for i in range(int(line[2:])):
                h_x += 1
                knots_pos[0] = resolve_tail(knots_pos[0][0], knots_pos[0][1], h_x, h_y)
                for j in range(1,9):
                    knots_pos[j] = resolve_tail(knots_pos[j][0], knots_pos[j][1], knots_pos[j-1][0], knots_pos[j-1][1])
                tail_positions.append((knots_pos[8][0], knots_pos[8][1]))
                
        elif line[0] == 'L':
            for i in range(int(line[2:])):
                h_x -= 1
                knots_pos[0] = resolve_tail(knots_pos[0][0], knots_pos[0][1], h_x, h_y)
                for j in range(1,9):
                    knots_pos[j] = resolve_tail(knots_pos[j][0], knots_pos[j][1], knots_pos[j-1][0], knots_pos[j-1][1])
                tail_positions.append((knots_pos[8][0], knots_pos[8][1]))

        elif line[0] == 'U':
            for i in range(int(line[2:])):
                h_y += 1
                knots_pos[0] = resolve_tail(knots_pos[0][0], knots_pos[0][1], h_x, h_y)
                for j in range(1,9):
                    knots_pos[j] = resolve_tail(knots_pos[j][0], knots_pos[j][1], knots_pos[j-1][0], knots_pos[j-1][1])
                tail_positions.append((knots_pos[8][0], knots_pos[8][1]))

        elif line[0] == 'D':
            for i in range(int(line[2:])):
                h_y -= 1
                knots_pos[0] = resolve_tail(knots_pos[0][0], knots_pos[0][1], h_x, h_y)
                for j in range(1,9):
                    knots_pos[j] = resolve_tail(knots_pos[j][0], knots_pos[j][1], knots_pos[j-1][0], knots_pos[j-1][1])
                tail_positions.append((knots_pos[8][0], knots_pos[8][1]))
    
        #print(t_x, t_y)
    print(len(set(tail_positions)))

part2()


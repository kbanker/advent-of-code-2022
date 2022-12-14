f = open('input.txt')
lines = [x.replace('\n','') for x in f]
f.close()

def part1():
    visible_trees = [[0 for i in range(len(lines[0]))] for j in range(len(lines))]
    tree_matrix = [[int(x) for x in line] for line in lines]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if i == 0 or j == 0:
                visible_trees[i][j] = 1
            elif i == len(lines) - 1 or j == len(lines[0]) - 1:
                visible_trees[i][j] = 1
            else:                
                if is_visible(i, j, tree_matrix):
                    visible_trees[i][j] = 1
                
        #print(visible_trees[i])
    total_visible = 0
    for row in visible_trees:
        for tree in row:
            total_visible += tree
    print(total_visible)

def is_visible(x, y, matrix):
    height = matrix[x][y]
    visible = 4
    for i in range(x):
        if matrix[i][y] >= height:
            visible -= 1
            break
    for i in range(x + 1, len(matrix)):
        if matrix[i][y] >= height:
            visible -= 1
            break
    for j in range(y):
        if matrix[x][j] >= height:
            visible -= 1
            break
    for j in range(y + 1, len(matrix[0])):
        if matrix[x][j] >= height:
            visible -= 1
            break
    return visible > 0


def part2():
    score_trees = [[0 for i in range(len(lines[0]))] for j in range(len(lines))]
    tree_matrix = [[int(x) for x in line] for line in lines]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if i == 0 or j == 0:
                score_trees[i][j] = 0
            elif i == len(lines) - 1 or j == len(lines[0]) - 1:
                score_trees[i][j] = 0
            else:                
                score_trees[i][j] = get_scenic_score(i, j, tree_matrix)
                
        #print(score_trees[i])
    max = 0
    for row in score_trees:
        for score in row:
            if score > max:
                max = score
                #print(row)
    
    print(max)
    

def get_scenic_score(x, y, matrix):
    height = matrix[x][y]
    score = [0,0,0,0]
    #if x-1 == 0: score[0] =1
    #if x+1 == len(matrix): score[1] =1
    #if y-1 == 0: score[2] =1
    #if y+1 == len(matrix[0]): score[3] =1
    for i in range(x -1, -1, -1):
        score[0] += 1
        if matrix[i][y] >= height:
            #print(i, y)
            break
    for i in range(x + 1, len(matrix)):
        score[1] += 1
        if matrix[i][y] >= height:
            #print(i, y)
            break
    for j in range(y-1, -1, -1):
        score[2] += 1
        if matrix[x][j] >= height:
            #print(x,j)
            break
            
    for j in range(y + 1, len(matrix[0])):
        score[3] += 1
        if matrix[x][j] >= height:
            #print(x, j)
            break
            
    #print(score)
    return score[0]*score[1]*score[2]*score[3]

part2()


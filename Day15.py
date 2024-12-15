#First Puzzle Solution
file = open("Puzzle Inputs/Puzzle 29.txt")

mat = []
pos = ()
ops = []
stack = []
mode = 1
dl = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for i,line in enumerate(file):
    if line != "\n":
        if mode == 1:
            mat.append([])
            for j, char in enumerate(line):
                if char == '\n':
                    continue

                mat[i].append(char)

                if char == '@':
                    pos = (i, j)
        else:
            for char in line:
                if char == '\n':
                    continue
                
                ops.append(char)

    else:
        mode += 1

while len(ops) > 0:
    k = 0
    op = ops.pop(0)
    match op:
        case '>':
            k = 1
        case 'v':
            k = 2
        case '<':
            k = 3
    
    new_l = pos[0] + dl[k]
    new_c = pos[1] + dc[k]

    if mat[new_l][new_c] == '#':
        continue

    while mat[new_l][new_c] == 'O':
        stack.append(pos)
        pos = (new_l, new_c)
        new_l = pos[0] + dl[k]
        new_c = pos[1] + dc[k]

    while len(stack) > 0:
        if mat[new_l][new_c] == '.':
            mat[new_l][new_c] = mat[pos[0]][pos[1]]
            mat[pos[0]][pos[1]] = '.'
            pos = (new_l, new_c)
        
        pos = stack.pop(len(stack) - 1)
        new_l = pos[0] + dl[k]
        new_c = pos[1] + dc[k]

    if mat[new_l][new_c] == '.':
        mat[new_l][new_c] = mat[pos[0]][pos[1]]
        mat[pos[0]][pos[1]] = '.'
        pos = (new_l, new_c)

for line in mat:
    print(line)

sum = 0

for i in range(0, len(mat)):
    for j in range(0, len(mat[0])):
        if mat[i][j] == 'O':
            sum += 100 * i + j

print(sum)


#Second Puzzle Solution
print("Second Puzzle")
print("---------------")

file = open("Puzzle Inputs/Puzzle 29.txt")

mat = []
pos = ()
ops = []
stack = []
mode = 1
dl = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for i,line in enumerate(file):
    if line != "\n":
        if mode == 1:
            mat.append([])
            for j, char in enumerate(line):
                match char:
                    case '\n':
                        continue
                    case '#':
                        mat[i].append('#')
                        mat[i].append('#')
                    case '@':
                        mat[i].append('@')
                        mat[i].append('.')
                        pos = (i, j * 2)

                    case 'O':
                        mat[i].append('[')
                        mat[i].append(']')

                    case '.':
                        mat[i].append('.')
                        mat[i].append('.')
                    
        else:
            for char in line:
                if char == '\n':
                    continue
                
                ops.append(char)

    else:
        mode += 1

def can_move(k, pos):
    global mat
    global dl
    global dc

    mstack = []
    mstack.append(pos)

    while (len(mstack) > 0):
        pos = mstack.pop(len(mstack) - 1)
        if mat[pos[0]][pos[1]] == ']':
            pos = (pos[0], pos[1] - 1)

        new_l = pos[0] + dl[k]
        new_c = pos[1] + dc[k]

        if mat[new_l][new_c] == '#' or mat[new_l][new_c + 1] == '#':
            return 0
        
        if k != 1 and mat[new_l][new_c] == ']' or mat[new_l][new_c] == '[':
            mstack.append((new_l, new_c))

        if k != 3 and mat[new_l][new_c + 1] == '[':
            mstack.append((new_l, new_c + 1))
        
    return 1


while len(ops) > 0:
    k = 0
    op = ops.pop(0)
    match op:
        case '>':
            k = 1
        case 'v':
            k = 2
        case '<':
            k = 3

    save = pos
    new_l = pos[0] + dl[k]
    new_c = pos[1] + dc[k]

    if mat[new_l][new_c] == '#':
        continue

    if can_move(k, (new_l, new_c)):
        if mat[new_l][new_c] == '[':
            stack.append((new_l, new_c))
    
        if mat[new_l][new_c] == ']':
            stack.append((new_l, new_c - 1))
        
        while len(stack) > 0:
            pos = stack[len(stack) - 1]
            if mat[pos[0]][pos[1]] == ']':
                pos = (pos[0], pos[1] - 1)

            new_l = pos[0] + dl[k]
            new_c = pos[1] + dc[k]
            
            if k != 1 and mat[new_l][new_c] == ']' or mat[new_l][new_c] == '[':
                stack.append((new_l, new_c))
                continue

            if k != 3 and mat[new_l][new_c + 1] == '[':
                stack.append((new_l, new_c + 1))
                continue

            if mat[new_l][new_c] == '.' or (k == 1 and mat[new_l][new_c + 1] == '.'):
                mat[pos[0]][pos[1]] = '.'
                mat[pos[0]][pos[1] + 1] = '.'
                mat[new_l][new_c] = '['
                mat[new_l][new_c + 1] = ']'

            stack.pop(len(stack) - 1)

    pos = save
    new_l = pos[0] + dl[k]
    new_c = pos[1] + dc[k]
    if mat[new_l][new_c] == '.':
        mat[new_l][new_c] = mat[pos[0]][pos[1]]
        mat[pos[0]][pos[1]] = '.'
        pos = (new_l, new_c)

sum = 0

for line in mat:
    print(line)

for i in range(0, len(mat)):
    for j in range(0, len(mat[0])):
        if mat[i][j] == '[':
            sum += 100 * i + j

print(sum)
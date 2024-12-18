#First Puzzle Solution
file = open("PuzzleIn.txt")

_s_max = 71
_sim_limit = 1024

mat = []
for i in range (0, _s_max):
    mat.append([])
    for j in range (0, _s_max):
        mat[i].append(0)

mat[0][0] = 1

for i, line in enumerate(file):
    if (i >= _sim_limit):
        break
    
    y, x = line.split(',')
    mat[int(x)][int(y)] = -1

queue = [(0, 0, _s_max * 2 - 2, 0)]
dl = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
shortest = 999999

def q_insert(x:tuple):
    global queue

    if (len(queue) == 0):
        queue.append(x)
        return

    l = 0
    r = len(queue) - 1

    while l < r:
        mid = int((l + r) /2)
        if queue[mid][2] == x[2] - 1:
            l = mid
            r = mid

        if queue[mid][2] > x[2] - 1:
            r = mid - 1
        else:
            l = mid + 1

    rg1 = l

    l = 0
    r = len(queue) - 1

    while l < r:
        mid = int((l + r) /2)
        if queue[mid][2] == x[2] + 1:
            l = mid
            r = mid

        if queue[mid][2] > x[2] + 1:
            r = mid - 1
        else:
            l = mid + 1

    rg2 = l

    for l in range (rg1, rg2):
        if queue[l][0] == x[0] and queue[l][1] == x[1]:
            if queue[l][2] > x[2]:
                queue[l] = (x)
            else:
                return

    queue.insert(l, x)

#At long last here we meet Lee once more
while len(queue) > 0:
    pos = queue.pop(0)

    if pos[0] == _s_max - 1 and pos[1] == _s_max - 1:
        if mat[pos[0]][pos[1]] < shortest:
            shortest = mat[pos[0]][pos[1]]
            print(shortest)
            continue

    for k in range(0, 4):
        new_l = pos[0] + dl[k]
        new_c = pos[1] + dc[k]

        if new_l < 0 or new_l >= len(mat) or new_c < 0 or new_c >= len(mat[0]):
            continue

        dist = 2 * _s_max - new_l - new_c - 2

        if mat[pos[0]][pos[1]] + dist > shortest:
            continue

        if mat[new_l][new_c] > mat[pos[0]][pos[1]] + 1 or mat[new_l][new_c] == 0:
            mat[new_l][new_c] = mat[pos[0]][pos[1]] + 1
            x = (new_l, new_c, dist)

            q_insert(x)

print (mat[_s_max-1][_s_max-1] - 1)


#Second Puzzle Solution
print("Second Puzzle")
print("---------------")


file = open("PuzzleIn.txt")

_s_max = 71
_sim_limit = 1024

mat = []
dl = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
for i in range (0, _s_max):
    mat.append([])
    for j in range (0, _s_max):
        mat[i].append(0)

mat[0][0] = 1

def q_insert(queue, x:tuple):
    if (len(queue) == 0):
        queue.append(x)
        return

    l = 0
    r = len(queue) - 1

    while l < r:
        mid = int((l + r) /2)
        if queue[mid][2] == x[2] - 1:
            l = mid
            r = mid

        if queue[mid][2] > x[2] - 1:
            r = mid - 1
        else:
            l = mid + 1

    rg1 = l

    l = 0
    r = len(queue) - 1

    while l < r:
        mid = int((l + r) /2)
        if queue[mid][2] == x[2] + 1:
            l = mid
            r = mid

        if queue[mid][2] > x[2] + 1:
            r = mid - 1
        else:
            l = mid + 1

    rg2 = l

    for l in range (rg1, rg2):
        if queue[l][0] == x[0] and queue[l][1] == x[1]:
            if queue[l][2] > x[2]:
                queue[l] = (x)
            else:
                return

    queue.insert(l, x)

def Lee(mat):
    global _s_max
    global dl 
    global dc
    
    
    shortest = 999999
    queue = [(0, 0, _s_max * 2 - 2, 0)]
    while len(queue) > 0:
        pos = queue.pop(0)

        if pos[0] == _s_max - 1 and pos[1] == _s_max - 1:
            if mat[pos[0]][pos[1]] < shortest:
                shortest = mat[pos[0]][pos[1]]
                continue

        for k in range(0, 4):
            new_l = pos[0] + dl[k]
            new_c = pos[1] + dc[k]

            if new_l < 0 or new_l >= len(mat) or new_c < 0 or new_c >= len(mat[0]):
                continue

            dist = 2 * _s_max - new_l - new_c - 2

            if mat[pos[0]][pos[1]] + dist > shortest:
                continue

            if mat[new_l][new_c] > mat[pos[0]][pos[1]] + 1 or mat[new_l][new_c] == 0:
                mat[new_l][new_c] = mat[pos[0]][pos[1]] + 1
                x = (new_l, new_c, dist)

                q_insert(queue, x)

    return mat[_s_max - 1][_s_max - 1]

def copy_mat(refmat):
    mat = []
    for line in refmat:
        mat.append(line.copy())

    return mat

for i, line in enumerate(file):
    y, x = line.split(',')
    mat[int(x)][int(y)] = -1

    print(f'{i}: {int(y)}, {int(x)}')
    if (i >= _sim_limit and Lee(copy_mat(mat)) == 0):
        print(f'{y}, {x}')
        break
        
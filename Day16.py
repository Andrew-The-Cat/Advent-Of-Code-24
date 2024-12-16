import math
#First Puzzle Solution
file = open("PuzzleIn.txt")

mat = []
path = []
start = ()
end = ()
queue = []

dl = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for i, line in enumerate(file):
    mat.append([])
    path.append([])
    for j, char in enumerate(line):
        if char == '\n':
            continue
        
        if char == 'S':
            start = (i, j, 0, 1)
            queue.append(start)
        
        if char == 'E':
            end = (i, j, 0, -1)

        path[i].append(0)
        mat[i].append(char)

while len(queue) > 0:
    pos = queue.pop(0)
    dir = pos[3]
    for k in range(0, 4):
        new_l = pos[0] + dl[k]
        new_c = pos[1] + dc[k]

        if new_l < 0 or new_l >= len(mat) or new_c < 0 or new_c >= len(mat[0]):
            continue

        if mat[new_l][new_c] != '#' and (path[new_l][new_c] == 0 or path[new_l][new_c] >= pos[2]):
            if k != dir:
                path[new_l][new_c] = pos[2] + 1001
            else:
                path[new_l][new_c] = pos[2] + 1

            if (mat[new_l][new_c] != 'E' and mat[new_l][new_c] != 'S'):
                queue.append((new_l, new_c, path[new_l][new_c], k))

print(path[end[0]][end[1]])

#Second Puzzle Solution
print("Second Puzzle")
print("---------------")

file = open("PuzzleIn.txt")

refmat = []
mat = []
path = []
start = ()
end = ()
stack = []

dl = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def copy_mat(mat1, mat2):
    while len(mat2) < len(mat1):
        mat2.append([])

    for i, line in enumerate(mat1):
        mat2[i] = line.copy()

for i, line in enumerate(file):
    refmat.append([])
    path.append([])
    for j, char in enumerate(line):
        if char == '\n':
            continue
        
        path[i].append(0)
        refmat[i].append(char)

        if char == 'S':
            start = (i, j)
            path[i][j] = 1
        
        if char == 'E':
            end = (i, j)

copy_mat(refmat, mat)

#Was having some sort of issue with using the same approach for the second half so I switched to backtracking for it's easy access to the exact path taken
stack.append((start[0], start[1], -1, 0))
cnt = 2
score = 0
minscore = -1

while (len(stack) > 0):
    pos = stack[len(stack) - 1]
    while pos[2] < 3:
        pos = (pos[0], pos[1], pos[2] + 1, pos[3])

        new_l = pos[0] + dl[pos[2]]
        new_c = pos[1] + dc[pos[2]]

        if (new_l >= len(mat) or new_l < 0 or new_c >= len(mat[0]) or new_c < 0):
            continue

        if mat[new_l][new_c] == '#' or mat[new_l][new_c] == 'S':
            continue

        if path[new_l][new_c] == 0 or (pos[2] != pos[3] and path[new_l][new_c] - 1000 > path[pos[0]][pos[1]]) or (pos[2] == pos[3] and path[new_l][new_c] + 1000 > path[pos[0]][pos[1]]):
            path[new_l][new_c] = path[pos[0]][pos[1]] + 1
            score += 1
            if pos[2] != pos[3]:
                path[new_l][new_c] += 1000
                score += 1000

            if mat[new_l][new_c] == 'E':
                if path[new_l][new_c] < minscore or minscore == -1:
                    minscore = path[new_l][new_c]
                    copy_mat(refmat, mat)

                if path[new_l][new_c] == minscore:
                    for x,y, w, z in stack:
                        mat[x][y] = 'O'

            else:
                stack[len(stack) - 1] = pos
                stack.append((new_l, new_c, -1, pos[2]))
                pos = stack[len(stack) - 1]
                cnt += 1
    score -= path[pos[0]][pos[1]]
    cnt -= 1
    stack.pop(len(stack) - 1)

for line in mat:
    print(line)
    for char in line:
        if char == 'O':
            cnt += 1

print (cnt)
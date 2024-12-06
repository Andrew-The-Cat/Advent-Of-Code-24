# First Puzzle Solution

file = open("Puzzle Inputs/Puzzle 11.txt")

matrix = []
start = ()
cnt = 0

dl = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for i, line in enumerate(file):
    matrix.append([])
    for j, char in enumerate(line):
        if char == '.':
            matrix[i].append(0)
        if char == '#':
            matrix[i].append(-1)
        if char == '^':
            start = (i, j)
            matrix[i].append(1)
            cnt += 1

k = 0

while start[0] >= 0 and start[0] < len(matrix) and start[1] >= 0 and start[1] < len(matrix[0]):
    if (k > 3):
        k = 0
    
    if matrix[start[0]][start[1]] == 0:
        cnt += 1
        matrix[start[0]][start[1]] = 1

    if matrix[start[0]][start[1]] == -1:
        start = (start[0] - dl[k], start[1] - dc[k])
        k += 1
    else:
        start = (start[0] + dl[k], start[1] + dc[k])



for line in matrix:
    for char in line:
        if char == 0:
            print('.', end='')
        if char == 1:
            print('X', end='')
        if char == -1:
            print('#', end='')
    print()
print(start)
print()
print(cnt)

#Second Puzzle Solution

print("Second Puzzle")
print("----------------")

file = open("Puzzle Inputs/Puzzle 11.txt")

matrix = []
start = ()
loop_cnt = 0

queue = []

dl = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for i, line in enumerate(file):
    matrix.append([])
    for j, char in enumerate(line):
        if char == '.':
            matrix[i].append(0)
        if char == '#':
            matrix[i].append(-1)
        if char == '^':
            matrix[i].append(0)
            start = (i, j)

def search(start, dir, matrix ,write = False):
    k = dir
    global loop_cnt

    while start[0] >= 0 and start[0] < len(matrix) and start[1] >= 0 and start[1] < len(matrix[0]):
        if (k > 3):
            k = 0
        
        if matrix[start[0]][start[1]] == k + 1:
            print("Looping!")
            loop_cnt += 1
            break

        if matrix[start[0]][start[1]] == 0:
            if write:
                queue.append((start[0], start[1], k))
            matrix[start[0]][start[1]] = k + 1

        if matrix[start[0]][start[1]] == -1:
            start = (start[0] - dl[k], start[1] - dc[k])
            k += 1
        else:
            start = (start[0] + dl[k], start[1] + dc[k])

def mat_copy(matrix) -> list[list]:
    ref_matrix = []

    for line in matrix:
        ref_matrix.append(line.copy())

    return ref_matrix

search(start, 0, mat_copy(matrix), True)

for line in matrix:
    for char in line:
        if char == 0:
            print('.', end='')
        if char >= 1:
            print('X', end='')
        if char == -1:
            print('#', end='')
    print()

#This is always going to be the guard's starting position
queue.pop(0)

while len(queue) > 0:
    start = queue.pop(0)

    matrix[start[0]][start[1]] = -1
    
    search((start[0], start[1]), start[2], mat_copy(matrix))
    
    matrix[start[0]][start[1]] = 0


print()
print(loop_cnt)
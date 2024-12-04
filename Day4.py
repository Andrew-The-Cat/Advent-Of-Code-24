def read(significant_char = 'X'):
    file = open("./Puzzle Inputs/Puzzle 7.txt")
    for i,line in enumerate(file):
        matrix.append([])
        matrix_ref.append([])
        for j,char in enumerate(line):
            matrix[i].append(char)
            matrix_ref[i].append('.')
            if (char == significant_char):
                matrix_ref[i][j] = significant_char
                queue.append((i, j))

#First Puzzle Solution

queue = []
matrix = []
matrix_ref=[]

dl = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

read()

key = "MAS"
cnt = 0

for x, y in queue:
    for k in range(0, 8):
        depth = 0
        l = x + dl[k]
        c = y + dc[k]
        while (l >= 0 and l < len(matrix) and c >= 0 and c < len(matrix[0]) and depth < len(key)):
            if (matrix[l][c] != key[depth]):
                break
            else:
                matrix_ref[l][c] = matrix[l][c].lower()
                depth += 1
                l += dl[k]
                c += dc[k]
        if depth == 3:
            cnt += 1


for line in matrix_ref:
    print (line)
print (queue)

print (cnt)


#Second Puzzle Solution
queue = []
matrix = []
matrix_ref=[]

dl = [-1, -1, 1, 1]
dc = [-1, 1, -1, 1]

read('A')

for line in matrix_ref:
    print (line)
print (queue)

key = "MS"
cnt = 0

for x, y in queue:
    x_cnt = 0
    for k in range(0, 4):
        depth = 0
        l = x + dl[k]
        c = y + dc[k]
        while (l >= 0 and l < len(matrix) and c >= 0 and c < len(matrix[0]) and depth < len(key)):
            if (matrix[l][c] != key[depth]):
                break
            else:
                matrix_ref[l][c] = matrix[l][c].lower()
                depth += 1
                l = x + dl[3 - k]
                c = y + dc[3 - k]
        if depth == len(key):
            x_cnt += 1
    if x_cnt == 2:
        cnt += 1


for line in matrix_ref:
    print (line)
print (queue)

print (cnt)

def vec_add (vec1, vec2, sign) -> tuple:
    if (sign == 1):
        return (vec1[0] + vec2[0], vec1[1] + vec2[1])
    if (sign == -1):
        return (vec1[0] - vec2[0], vec1[1] - vec2[1])

def scalar_mul (vec1, scalar) -> tuple:
    return (vec1[0] * scalar, vec1[1] * scalar)

def is_valid (vec) -> bool:
    global matrix

    if vec[0] != int(vec[0]) or vec[1] != int(vec[1]):
        return False

    if not (vec[0] < len(matrix) and vec[0] >= 0 and vec[1] < len(matrix[0]) and vec[1] >= 0):
        return False
    
    return True

def check_matrix(annode):
    global cnt
    global matrix

    if is_valid( annode ):
        annode = (int(annode[0]), int(annode[1]))

        if (matrix[annode[0]][annode[1]] != '#'):
            matrix[annode[0]][annode[1]] = '#'
            cnt += 1


#First Puzzle Solution
file = open("Puzzle Inputs/Puzzle 15.txt")

map = {}
matrix = []
keys = []
cnt = 0

for i, line in enumerate(file):
    matrix.append([])

    for j, char in enumerate(line):
        if char == '\n':
            continue
    
        matrix[i].append(char)

        if char != '.':
            if map.get(char, 0) == 0:
                map[char] = []
                keys.append(char)

            map[char].append((i, j))

#Thought of using vectors for the solution
for antenna in keys:
    pos = map.get(antenna)

    for i in range(1, len(pos)):
        for j in range(0, i):
            diff_vec = vec_add(pos[i], pos[j], -1)
            
            check_matrix( vec_add( diff_vec , pos[i], 1 ) )

            check_matrix( vec_add( pos[j] , diff_vec, -1 ) )

            check_matrix( vec_add( scalar_mul(diff_vec, 1/3) , pos[j], 1 ) )

            check_matrix( vec_add( pos[i] , scalar_mul(diff_vec, 1/3), -1 ) )

            
print(map)
for line in matrix:
    print(line)

print (cnt)


#Second Puzzle Solution
print("Second Puzzle")
print("---------------")

#This time I decided to go with functions
file = open("Puzzle Inputs/Puzzle 15.txt")

map = {}
matrix = []
keys = []
cnt = 0

for i, line in enumerate(file):
    matrix.append([])

    for j, char in enumerate(line):
        if char == '\n':
            continue
    
        matrix[i].append(char)

        if char != '.':
            if map.get(char, 0) == 0:
                map[char] = []
                keys.append(char)

            map[char].append((i, j))

def f(x, pos:tuple):
    return m*(x - pos[0]) + pos[1]

for antenna in keys:
    pos = map.get(antenna)

    for i in range(1, len(pos)):
        for j in range(0, i):
            diff_vec = vec_add(pos[i], pos[j], -1)
            
            m = diff_vec[1] / diff_vec[0]

            for k in range(0, len(matrix[0])):
                check_matrix((k, f(k, pos[i])))

print(map)
for line in matrix:
    print(line)

print (cnt)

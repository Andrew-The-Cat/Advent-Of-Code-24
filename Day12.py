#First Puzzle Solution
file = open("Puzzle Inputs/Puzzle 23.txt")

mat = []
searched = []
queue = []

dl = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

area = 0
perimiter = 0

for i, line in enumerate(file):
    mat.append([])
    searched.append([])
    for j, char in enumerate(line):
        if char != '\n':
            searched[i].append(0)
            mat[i].append(char)

def fill ():
    global area
    global perimiter

    while len(queue) > 0:
        pos = queue.pop(0)

        l = pos[0]
        c = pos[1]
        char = pos[2]

        for k in range (0, len(dl)):
            new_l = l + dl[k]
            new_c = c + dc[k]

            if new_l >= 0 and new_l < len(mat) and new_c >= 0 and new_c < len(mat[0]) and mat[new_l][new_c] == char:
                if searched[new_l][new_c] == 0:
                    area += 1
                    searched[new_l][new_c] = 1
                    queue.append((new_l, new_c, char))
            else:
                perimiter += 1

sum = 0

for i in range (0, len(mat)):
    for j in range (0, len(mat[0])):
        area = 1
        perimiter = 0

        if searched[i][j] == 0:
            queue.append((i, j, mat[i][j]))
            searched[i][j] = 1
            fill()

            print(f'{mat[i][j]} : {area}, {perimiter}')

        sum += area * perimiter

print(sum)

#Second Puzzle Solution

print ("Second Puzzle")
print ("---------------")

file = open("Puzzle Inputs/Puzzle 23.txt")

mat = []
searched = []
searched_edges = {}
queue = []

dl = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

area = 0
perimiter = 0

for i, line in enumerate(file):
    mat.append([])
    searched.append([])
    for j, char in enumerate(line):
        if char != '\n':
            searched[i].append(0)
            mat[i].append(char)

#We're always starting in the top left corner and every plot will make a loop on its peremeter
def fill (start_l, start_c, char, start_dir, edges = False):
    global area
    global perimiter

    first = (start_l, start_c)
    queue = [first]
    passed = False

    dir = start_dir
    while len(queue) > 0:
        pos = queue.pop(0)

        l = pos[0]
        c = pos[1]

        k = 0
        end_dir = 3

        if edges:
            if dir == 0:
                k = 3
            else:
                k = dir - 1
            
            if dir == 0 or dir == 1:
                end_dir = dir + 2
            else:
                end_dir = dir - 2

        while (k != end_dir and edges) or (not edges and k <= end_dir):
            new_l = l + dl[k]
            new_c = c + dc[k]

            if pos == first and k == start_dir and passed:
                return

            if new_l >= 0 and new_l < len(mat) and new_c >= 0 and new_c < len(mat[0]) and mat[new_l][new_c] == char:
                if (edges):
                    if (dir == 0 and k == 3) or (dir != 0 and k == dir - 1):
                        perimiter += 1
                    
                    dir = k
                    passed = True
                    queue.append((new_l, new_c))
                    break
                
                else:
                    if searched[new_l][new_c] == 0:
                        area += 1
                        searched[new_l][new_c] = char
                        queue.append((new_l, new_c))

            else:
                if edges:
                    if (searched_edges.get((l, c), -1) == -1):
                        searched_edges[(l, c)] = []
                    searched_edges[(l, c)].append(k)
                    if ((dir == 0 and k != 3) or (dir != 0 and k != dir - 1)):
                        perimiter += 1
                        
                else:
                    good_to_search = True
                    if searched_edges.get((l, c), -1) != -1:
                        for e in searched_edges[(l, c)]:
                            if k == e:
                                good_to_search = False
                                break

                    if good_to_search:
                        if k == 3:
                            fill (l, c, char, 0, True)
                        else:
                            fill (l, c, char, k + 1, True)

            if k == 3 and edges:
                k = 0
            else:
                k += 1

        if edges and k == end_dir:
            if not passed:
                perimiter += 2
                searched_edges[(l, c)].append(k)
                return

            dir = k
            if pos == first and dir == start_dir:
                return

            new_l = l + dl[k]
            new_c = c + dc[k]

            passed = True
            queue.append((new_l, new_c))

sum = 0

for i in range (0, len(mat)):
    for j in range (0, len(mat[0])):
        area = 1
        perimiter = 0

        if searched[i][j] == 0:
            fill(i, j, mat[i][j], 1, edges=True)
            searched[i][j] = mat[i][j]
            fill(i, j, mat[i][j], 1)

            print(f'{mat[i][j]} : {area} * {perimiter} = {area * perimiter}')

        sum += area * perimiter

print(sum)
#First Puzzle Solution
file = open("Puzzle Inputs/Puzzle 19.txt")

#Decided to have more fun today and as such am using Lee
map = []
end = {}
queue = []

dl = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

start = []

for i, line in enumerate(file):
    map.append([])

    for j, char in enumerate(line):
        if (char == '\n'):
            continue

        map[i].append(int(char))

        if char == '0':
            queue.append((i, j, len(start), -1))
            start.append(0)

def Lee():
    while (len(queue) > 0):
        pos = queue.pop(0)
        if not (pos[0] >= 0 and pos[0] < len(map) and pos[1] >= 0 and pos[1] < len(map[0])):
            continue

        if end.get(pos) == 1:
            continue
        
        if (map[pos[0]][pos[1]] - pos[3] != 1):
            continue

        if map[pos[0]][pos[1]] == 9:
            end[pos] = 1
            start[pos[2]] += 1

        for k in range (0, len(dl)):
            new_l = pos[0] + dl[k]
            new_c = pos[1] + dc[k]

            queue.append((new_l, new_c, pos[2], map[pos[0]][pos[1]]))


print(" |0 1 2 3 4 5 6 7 8 9 10")
for i, line in enumerate(map):
    print (str(i)+ '|', end='')
    for i in line:
        print (str(i) + ' ', end='')
    print()

Lee()
sum = 0
for i in start:
    sum += i
print (start)
print (sum)


#Second Puzzle Solution
#Happened to be basically the exact same but less restricted
print("Second Puzzle")
print("---------------")

file = open("Puzzle Inputs/Puzzle 19.txt")

map = []
end = {}
queue = []

dl = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

start = []
sum = 0

for i, line in enumerate(file):
    map.append([])

    for j, char in enumerate(line):
        if (char == '\n'):
            continue

        map[i].append(int(char))


        if char == '0':
            queue.append((i, j, len(start), -1))
            start.append(0)

def Lee():
    global sum
    while (len(queue) > 0):
        pos = queue.pop(0)
        if not (pos[0] >= 0 and pos[0] < len(map) and pos[1] >= 0 and pos[1] < len(map[0])):
            continue
        
        if (map[pos[0]][pos[1]] - pos[3] != 1):
            continue

        if map[pos[0]][pos[1]] == 9:
            if end.get(pos, 0) == 0:
                end[pos] = 1
            else:
                end[pos] += 1
            start[pos[2]] += 1
            sum += 1

        for k in range (0, len(dl)):
            new_l = pos[0] + dl[k]
            new_c = pos[1] + dc[k]

            queue.append((new_l, new_c, pos[2], map[pos[0]][pos[1]]))


print(" |0 1 2 3 4 5 6 7 8 9 10")
for i, line in enumerate(map):
    print (str(i)+ '|', end='')
    for int in line:
        print (str(int) + ' ', end='')
    print()

Lee()

print (start)
print (sum)
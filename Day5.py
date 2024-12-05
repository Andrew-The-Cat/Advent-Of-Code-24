from math import *

#First Puzzle Solution

file = open("./Puzzle Inputs/Puzzle 9.txt")

rule_map = {}
sum = 0

for line in file:
    if line.find("|") != -1:
        [x, y] = line.split("|")
        if not rule_map.get(int(x), 0):
            rule_map[int(x)] = []
        rule_map[int (x)].append(int(y))

    elif(line == '\n'):
        continue

    else:
        a = line.split(',')
        correct = True

        for i, x in enumerate(a):
            x = int(x)

            for k in range (0, i):
                if rule_map.get(x, 0) != 0 and rule_map[x].count(int(a[k])) > 0:
                    correct = False
                    break

            if not correct:
                break
        
        if (correct):
            sum += int(a[floor(len(a)/2)])
            print(a[floor(len(a)/2)])

print (sum)


#Second Puzzle Solution
print("\n Second Puzzle")
print("--------------------------------")
file = open("./Puzzle Inputs/Puzzle 9.txt")

rule_map = {}
sum = 0

for line in file:
    if line.find("|") != -1:
        [x, y] = line.split("|")
        if not rule_map.get(int(x), 0):
            rule_map[int(x)] = []
        rule_map[int (x)].append(int(y))

    elif(line == '\n'):
        continue

    else:
        needs_correcting = False

        a = line.split(',')
        print()
        print(a)
        correct = False
        while not correct:
            correct = True

            for i, x in enumerate(a):
                x = int(x)

                for k in range (0, i):
                    if rule_map.get(x, 0) != 0 and rule_map[x].count(int(a[k])) > 0:
                        correct = False
                        needs_correcting = True
                        aux = int(a[k])
                        a[k] = x
                        a[i] = aux
                        print(a)
                        break

                if not correct:
                    break
        
        if (correct and needs_correcting):
            sum += int(a[floor(len(a)/2)])
            print(a[floor(len(a)/2)])
            

print (sum)
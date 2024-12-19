import re
#First Puzzle Solution
file = open("PuzzleIn.txt")
mode = 0

cnt = 0
available = []
final_pattern = "^(?:"
aux_pattern = ""

for line in file:
    if line == '\n':
        done = False

        while not done:
            done = True
            for idx in range(0, len(available)):
                aux_pattern = "^("
                z = available.pop(0)

                for towel in available:
                    aux_pattern += towel
                    aux_pattern += '|'
                aux_pattern = aux_pattern.removesuffix('|') + ')+$'

                if len(re.findall(aux_pattern, z)) == 0:
                    available.append(z)
                else:
                    done = False

        for towel in available:
            final_pattern += towel
            final_pattern += '|'
        final_pattern = final_pattern.removesuffix('|') + ')+$'

        print(final_pattern)

        mode = 1
        continue

    if mode == 0:
        x = line.split(',')
        for c in x:
            c = c.strip('\n ')

            available.append(c)
    else:
        print(line, end='')

    if mode == 1:
        line = line.removesuffix('\n')
        matches = re.findall(final_pattern, line)

        if len(matches) > 0 and matches[0] == line:
            print("Correct")
            cnt += 1

print ('\n'+ str(cnt))

#Second Puzzle Solution
print("Second Puzzle")
print("---------------")


file = open("PuzzleIn.txt")
mode = 0

sum = 0
available = []
aux_pattern = ""

combos = {}

def count(current:str):
    if combos.get(current, -1) != -1:
        return combos[current]
    
    if current == '':
        return 1
    
    cnt = 0
    for towel in available:
        if current.startswith(towel):
           cnt += count(current[len(towel):])

    combos[current] = cnt
    return cnt

for line in file:
    if line == '\n':
        mode = 1
        continue

    if mode == 0:
        x = line.split(',')
        for c in x:
            c = c.strip('\n ')

            available.append(c)

    if mode == 1:
        line = line.removesuffix('\n')

        sum += count(line)

print (sum)
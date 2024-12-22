#First Puzzle Solution
file = open("PuzzleIn.txt")

seeds = {}

def tick():
    global seeds
    copy = seeds.copy()

    for seed in list(seeds.keys()):
        if seeds[seed] <= 0:
            continue
        temp = seed
        copy[seed] -= seeds[seed]

        aux = seed << 6
        seed ^= aux
        seed = seed & 16777215
        aux = seed >> 5
        seed ^= aux
        seed = seed & 16777215
        aux = seed << 11
        seed ^= aux
        seed = seed & 16777215

        if copy.get(seed, -1) == -1:
            copy[seed] = 0
        copy[seed] += seeds[temp]

    for seed in list(copy.keys()):
        if copy[seed] == 0:
            copy.pop(seed)

    seeds = copy

for line in file:
    seeds[int(line)] = 1

for i in range(0, 2000):
    #print (f'Tick {i}:')
    tick()

s = 0
for key in list(seeds.keys()):
    if seeds[key] > 0:
        print(f'{key}: {seeds[key]}')
        s += key

print (f'Sum: {s}')

#Second Puzzle Solution
file = open("PuzzleIn.txt")

monkeys = []
buy = {}
changes = []
checked = set()

def tick(iter):
    global monkeys
    global buy
    global changes
    global checked

    copy = monkeys.copy()

    for i in range(0, len(monkeys)):
        monkey = copy.pop(0)
        if monkey[1] <= 0: 
            continue
        seed = monkey[1]

        aux = seed << 6
        seed ^= aux
        seed = seed & 16777215
        aux = seed >> 5
        seed ^= aux
        seed = seed & 16777215
        aux = seed << 11
        seed ^= aux
        seed = seed & 16777215

        copy.append((monkey[0], seed))

        changes[monkey[0]] = (seed % 10 - monkey[1] % 10, changes[monkey[0]][0], changes[monkey[0]][1], changes[monkey[0]][2])

        if iter < 3 or (monkey[0], changes[monkey[0]]) in checked:
            continue
        checked.add((monkey[0], changes[monkey[0]]))
        if buy.get(changes[monkey[0]], -1) == -1:
            buy[changes[monkey[0]]] = 0

        buy[changes[monkey[0]]] += seed % 10
    monkeys = copy

for i, line in enumerate(file):
    monkeys.append((i, int(line)))
    changes.append((0, 0, 0, 0))

for i in range(0, 2000):
    print (f'Tick {i}:')
    tick(i)

max = 0
max_it = 0
for item in list(buy.keys()):
    if buy[item] >= max:
        max = buy[item]
        max_it = item

print(s)
print(f'{max_it}   ---   {max}')
#First Puzzle Solution
#For the first part I made this hediously slow algorithm and tried to make it as good as possible
file = open("Puzzle Inputs/Puzzle 21.txt")

queue = []
results = {}
num_blinks = 5

for num in file.readline().split(' '):
    queue.append( (int(num), 0) )

cnt = 0

while len(queue) > 0:
    stone = queue.pop(0)

    if (stone[1] >= num_blinks):
        cnt += 1
        continue
    
    if results.get(stone[0], -1) != -1:
        while results.get(stone[0], -1) != -1 and stone[1] < num_blinks and type(results[stone[0]]) != type(()):
            stone = (results[stone[0]], stone[1] + 1)

        if (type(results.get(stone[0], -1)) == type(()) and stone[1] < num_blinks):
            queue.append( (results[stone[0]][0], stone[1] + 1) )
            queue.append( (results[stone[0]][1], stone[1] + 1) )
        else:
            queue.append( stone )
        continue

    if (stone[0] == 0):
        results[stone[0]] = 1
        queue.append( (results[stone[0]], stone[1] + 1) )
        continue

    if (len(str(stone[0])) % 2 == 0):
        p = pow(10, int(len(str(stone[0])) / 2))

        results[stone[0]] = ( int(stone[0] / p),  stone[0] % p)

        queue.append( (results[stone[0]][0], stone[1] + 1) )
        queue.append( (results[stone[0]][1], stone[1] + 1) )
        continue

    results[stone[0]] = stone[0] * 2024
    queue.append( (results[stone[0]], stone[1] + 1) )

print (cnt)
results.clear()
queue.clear()

print("Second Puzzle")
print("---------------")

#Second Puzzle Solution
#However, after seeing the 75 blink requirement I went right back to the drawing board
#and then I found a much better solution thanks to arthomnix on github https://github.com/arthomnix

file = open("Puzzle Inputs/Puzzle 21.txt")

#using the number of stones rather than checking each one
stones = {}
num_blinks = 75

for num in file.readline().split(' '):
    if stones.get(int(num), -1) == -1:
        stones[int(num)] = 0
    stones[int(num)] += 1

#Indeed very silly of me to have not thought of this earlier
for blink in range (0, num_blinks):
    copy = stones.copy()
    for key in list(stones.keys()):
        if stones[key] <= 0:
            continue
        copy[key] -= stones[key]

        if key == 0:
            if copy.get(1, -1) == -1:
                copy[1] = 0
            copy[1] += stones[key]
            continue

        if len(str(key)) % 2 == 0:
            p = pow(10, int(len(str(key)) / 2))
            
            if copy.get(int (key / p), -1) == -1:
                copy[int (key / p)] = 0
            copy[int (key / p)] += stones[key]

            if copy.get(int (key % p), -1) == -1:
                copy[int (key % p)] = 0
            copy[int (key % p)] += stones[key]
            
            continue

        if copy.get(key * 2024, -1) == -1:
            copy[key * 2024] = 0
        copy[key * 2024] += stones[key]

    stones = copy

sum = 0
for i in list(stones.values()):
    sum += i

print(sum)
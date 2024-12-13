#First Puzzle Solution

#Today I had a hunch that there would only be one solution and that would be solving the system of equations so that's just what I did
file = open("Puzzle Inputs/Puzzle 25.txt")

in_str = file.read()
puzzle_in = []

i = 0
while i < len(in_str):
    num = 0
    if in_str[i].isdigit():
        while (in_str[i].isdigit()):
            num = 10 * num + int(in_str[i])
            i += 1
        
        puzzle_in.append(num)
    i += 1

sum = 0

while len(puzzle_in) > 0:
    a1 = puzzle_in.pop(0)
    a2 = puzzle_in.pop(0)
    b1 = puzzle_in.pop(0)
    b2 = puzzle_in.pop(0)
    res1 = puzzle_in.pop(0)
    res2 = puzzle_in.pop(0)

    det1 = a1 * b2 - b1 * a2
    det2 = res1 * b2 - b1 * res2
    det3 = a1 * res2 - res1 * a2

    x = det2 / det1
    y = det3 / det1

    print (f'{a1} + {a2} = {res1}')
    print (f'{b1} + {b2} = {res2}')

    if x != int(x) or y != int(y):
        print ("No Result")

    else:
        sum += 3 * int(x) + int(y)
        print (f'{int(x)}   {int(y)}')

print(sum)

print("Second Puzzle")
print("--------------")

#Second Puzzle Solution
file = open("Puzzle Inputs/Puzzle 25.txt")

in_str = file.read()
puzzle_in = []

i = 0
while i < len(in_str):
    num = 0
    if in_str[i].isdigit():
        while (in_str[i].isdigit()):
            num = 10 * num + int(in_str[i])
            i += 1
        
        puzzle_in.append(num)
    i += 1

sum = 0

while len(puzzle_in) > 0:
    a1 = puzzle_in.pop(0)
    a2 = puzzle_in.pop(0)
    b1 = puzzle_in.pop(0)
    b2 = puzzle_in.pop(0)
    res1 = puzzle_in.pop(0)
    res2 = puzzle_in.pop(0)

    res1 += 10000000000000
    res2 += 10000000000000

    det1 = a1 * b2 - b1 * a2
    det2 = res1 * b2 - b1 * res2
    det3 = a1 * res2 - res1 * a2

    x = det2 / det1
    y = det3 / det1

    print (f'{a1}A + {a2}B = {res1}')
    print (f'{b1}A + {b2}B = {res2}')

    if x != int(x) or y != int(y):
        print ("No Result")

    else:
        sum += 3 * int(x) + int(y)
        print (f'A: {int(x)}   B: {int(y)}')

print(sum)
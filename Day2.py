''' First Puzzle Solution 
out1 = open("./TEST1.txt", "wt")
out2 = open("./TEST2.txt", "wt")
file = open("./Puzzle Inputs/Puzzle 3.txt")
cnt = 0

for line in file:
    a = line.split(" ")
    b = [0]
    safe = True

    a[0] = int(a[0])
    for i in range (1, len(a)):
        a[i] = int(a[i])

        b.append(a[i] - a[i-1])

        if b[i] == 0 or abs(b[i]) > 3:
            safe = False
            break


        if i > 1 and b[i] * b[i-1] <= 0:
            safe = False
            break

    if safe:
        cnt += 1
        out1.write("Safe" + '\n')
    else:
        out1.write ("Unsafe" + '\n')

    out1.write (str(a) + '\n')
    out1.write (str(b) + '\n')
    out1.write ('\n')

out1.write (str(cnt) + '\n')
'''

''' Second Puzzle Solution

    Rly wanted to find a better solution but I came up 6 answers short for 3 hours and I gave up :3

file = open("./Puzzle Inputs/Puzzle 3.txt", "rt")

cnt = 0

for line in file:
    failures = 1
    a = line.split(" ")

    for i in range(0, len(a)):
        a[i] = int(a[i])

    x = []
    x.append(a)
    for i in range (0, len(a) + 1):
        b = [0]
        safe = True
        if i > 0:
            z = a.copy()
            z.pop(i-1)
            x.append(z)

        for j in range (1, len(x[i])):
            b.append(x[i][j] - x[i][j-1])

            if (b[j] == 0 or abs(b[j]) > 3) or (j > 1 and b[j] * b[j-1] <= 0):
                safe = False
                break

        if safe:
            cnt += 1
            print("Safe")
            print(str(x[i]))
            print(str(b))
            print('\n')
            break

print(cnt)
'''
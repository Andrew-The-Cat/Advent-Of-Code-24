import time

#First Puzzle Solution
file = open("Puzzle Inputs/Puzzle 27.txt")

marginx = 101
marginy = 103

cntI = 0
cntII = 0
cntIII = 0
cntIV = 0

mat = []
for i in range (0, marginy):
    mat.append([])
    for j in range(0, marginx):
        mat[i].append(0)

for line in file:
    p, v = line.split(" ")

    x, y = p.split(',')
    x = int(x.removeprefix("p="))
    y = int(y)

    vx, vy = v.split(',')
    vx = int(vx.removeprefix("v="))
    vy = int(vy)

    for i in range (0, 100):
        x += vx
        y += vy

        if x >= marginx:
            x -= marginx
        if x < 0:
            x += marginx

        if y >= marginy:
            y -= marginy
        if y < 0:
            y += marginy


    mat[y][x] += 1
    print(f'robot at {x}, {y} with speed {vx}, {vy}')

    if x > int(marginx / 2) and y > int(marginy / 2):
        cntI += 1
    if x < int(marginx / 2) and y > int(marginy / 2):
        cntII += 1
    if x < int(marginx / 2) and y < int(marginy / 2):
        cntIII += 1
    if x > int(marginx / 2) and y < int(marginy / 2):
        cntIV += 1

for line in mat:
    print (line)

print(f'{cntI} - {cntII} - {cntIII} - {cntIV}')

print (cntIV * cntI * cntII * cntIII)


#Second Puzzle Solution
#I didn't exactly know how to check for a 'christmas tree' so I decided to look for myself
marginx = 101
marginy = 103

ref_mat = []
mat = []

for i in range (0, marginy):
    ref_mat.append([])
    for j in range(0, marginx):
        ref_mat[i].append('.')

def copy_mat(mat1, mat2):
    while len(mat2) < len(mat1):
        mat2.append([])

    for i, line in enumerate(mat1):
        mat2[i] = line.copy()

def step(t):
    global mat

    file = open("Puzzle Inputs/Puzzle 27.txt")
    for line in file:
        p, v = line.split(" ")

        x, y = p.split(',')
        x = int(x.removeprefix("p="))
        y = int(y)
        vx, vy = v.split(',')
        vx = int(vx.removeprefix("v="))
        vy = int(vy)

        for i in range (0, t):
            x += vx
            y += vy

            if x >= marginx:
                x -= marginx
            if x < 0:
                x += marginx

            if y >= marginy:
                y -= marginy
            if y < 0:
                y += marginy

        mat[y][x] = '#'

for k in range(98, 10600, 101):
    copy_mat(ref_mat, mat)
    step(k)


    print(k)
    print('-------------------------------------------------------------------------------------------------------------------------------------------')
    print()
    for line in mat:
        print (line)
    print()

    time.sleep(0.2)

print(f'{cntI} - {cntII} - {cntIII} - {cntIV}')

print (cntIV * cntI * cntII * cntIII)
#Actually really disliked this second challenge
a = []
b = []

def read(a, b, f_path):
    file = open(f_path, "rt")
    for z in file:
        [x, y] = z.split("   ")

        a.append(int(x))
        b.append(int(y))

# First Puzzle Solution
def pivot(a, l, r):
    i = l
    j = r
    direction = 1
    
    while j > i:
        if a[i] > a[j]:
            aux = a[i]
            a[i] = a[j]
            a[j] = aux
            direction *= -1
        
        if direction == 1:
            j -= 1
        else:
            i += 1
    return i
    
def QuickSort(a, l, r):
    if l >= r:
        return
    
    pivot_pos = pivot(a, l, r)
    
    QuickSort(a, l, pivot_pos - 1)
    QuickSort(a, pivot_pos + 1, r)

read(a, b, "./Puzzle Inputs/Puzzle 1.txt")

QuickSort(a, 0, len(a)-1)
QuickSort(b, 0, len(b)-1)
sum = 0

for i, x in enumerate(a):
    sum += abs(x - b[i])

print (sum)

# Second Puzzle Solution
sol = {}
sum = 0
a.clear()
b.clear()

read(a, b, "./Puzzle Inputs/Puzzle 2.txt")
for x in b:
    if x in sol:
        sol[x] += 1
    else:
        sol[x] = 1

for y in a:
    if y in sol:
        sum += y * sol[y]

print (sum)
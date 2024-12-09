#First Puzzle Solution
file = open("Puzzle Inputs/Puzzle 17.txt")

p = file.readline()
chk = 0
l = 0
if len(p) % 2 == 0:
    r = len(p) - 2
else:
    r = len(p) - 1

v = []
for char in p:
    v.append(int(char))
#I really didn't think it necessary to expand the list and neither did I want to so I am just simulating an index position
idx = 0

while (l < r):
    if (l%2 == 0):
        idx_range = range(idx, idx+int(v[l]))

        for idx in idx_range:
            #print(idx  * int(l/2))
            chk += idx * int(l/2)

        idx += 1
    else:
        idx_range = range(idx, idx + int(v[l]))

        while v[l] > 0 and l < r:
            if v[r] >= v[l]:
                for idx in range(idx, idx + v[l]):
                    #print(idx  * int(r/2))
                    chk += idx * int(r/2)

                v[r] -= v[l]
                v[l] = 0
                idx += 1
            else:
                for idx in range(idx, idx + v[r]):
                    #print(idx  * int(r/2))
                    chk += idx * int(r/2)

                v[l] -= v[r]
                v[r] = 0
                idx += 1
            
            if (v[r] == 0):
                r -= 2

    l += 1

if l == r:
    for idx in range(idx, idx + v[r]):
        #print(idx  * int(r/2))
        chk += idx * int(r/2)

print (chk)

print ("Second Puzzle")
print ("---------------")

#Second Puzzle Solution

#Works REALLY slow- surprisingly so
#Then again it's already well into the evening and I can't focus enough to fix it now :3

file = open("Puzzle Inputs/Puzzle 17.txt")

p = file.readline()
chk = 0
if len(p) % 2 == 0:
    refr = len(p) - 2
else:
    refr = len(p) - 1

l = 0
r = refr

v = []
#decided that I needed to know the numbers
num = []
for char in p:
    v.append(int(char))

    if len(v) %2 != 0:
        num.append(int(len(v) / 2))
    else:
        num.append(0)
idx = 0

#print(v)
#print (num)

while (r > 0):
    l = 1
    while l < r:
        if  v[l] >= v[r]:
            aux = num[r]
            
            num[r] = 0

            num.insert(l, aux)
            num.insert(l, 0)
            v[l] -= v[r]

            v.insert(l, v[r])
            v.insert(l, 0)

            r += 2
            break  
            
        l+=2

    r -= 2

#print("vvvvvvvvvvvvvvv")
#print(v)
#print(num)

for i in range (0, len(v)):
    fin_idx = idx + v[i]
    for idx in range (idx, fin_idx):
        #print (idx * num[i])
        chk += idx * num[i]

    idx = fin_idx


print (chk)
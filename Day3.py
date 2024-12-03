import re

file = open("./Puzzle Inputs/Puzzle 5.txt")

#First Puzzle Solution
s = 0

for line in file:
    ops = re.findall("mul\(\d+,\d+\)", line)

    for op in ops:
        print(op)

        stripped = str(op).strip("mul()")
        
        p = 1

        for x in str(stripped).split(","):
            p *= int(x)

        s += p
        
print('\n' + str(s))

file.seek(0)
s = 0
enabled=True

for line in file:
    ops = re.findall("(mul\(\d+,\d+\)|do\(\)|don't\(\))", line)

    for op in ops:
        print(op)

        if (str(op).find("mul") != -1 and enabled):
            stripped = str(op).strip("mul()")
            
            p = 1

            for x in str(stripped).split(","):
                p *= int(x)

            s += p
        
        if (str(op).find("don't()") != -1):
            enabled = False
        elif (str(op).find("do") != -1):
            enabled = True
        
        
print('\n' + str(s))
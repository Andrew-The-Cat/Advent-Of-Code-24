import re
#First Puzzle Solution
file = open("PuzzleIn.txt")
mode = 1

puzzleIn = re.findall("\d+", file.read())
ops = []

regA = int(puzzleIn.pop(0))
regB = int(puzzleIn.pop(0))
regC = int(puzzleIn.pop(0))

for i in range(0, len(puzzleIn), 2):
    ops.append((int(puzzleIn[i]), int(puzzleIn[i+1])))

print (f"Reg A: {regA}")
print(f"Reg B: {regB}")
print(f"Reg C: {regC}")

print(f"Instructions: ", end='')
for op in ops:
    print(f"{op}, ", end='')
print()

def decode_operand(operand) -> int:
    if operand in range(0, 3+1):
        return operand
    if operand == 4:
        return regA
    if operand == 5:
        return regB
    if operand == 6:
        return regC
    if operand == 7:
        raise ValueError("Invalid use of reserved operand")

pointer = 0

while pointer < len(ops):
    instruction = ops[pointer][0]
    operand = ops[pointer][1]

    match instruction:
        case 0:
            regA = regA >> decode_operand(operand)

        case 1:
            regB = regB ^ operand
        
        case 2:
            regB = decode_operand(operand) & 7

        case 3:
            if regA != 0:
                pointer = operand - 1

        case 4:
            regB = regC ^ regB

        case 5:
            print(f'{decode_operand(operand) & 7},', end='')

        case 6:
            regB = regA >> decode_operand(operand)

        case 7:
            regC = regA >> decode_operand(operand)

    pointer += 1


#Second Puzzle Solution
print("\n Second Puzzle")
print("---------------")

file = open("PuzzleIn.txt")
mode = 1

puzzleIn = re.findall("\d+", file.read())
ops = []

regA = int(puzzleIn.pop(0))
regB = int(puzzleIn.pop(0))
regC = int(puzzleIn.pop(0))

for i in range(0, len(puzzleIn), 2):
    ops.append((int(puzzleIn[i]), int(puzzleIn[i+1])))

print (f"Reg A: {regA}")
print(f"Reg B: {regB}")
print(f"Reg C: {regC}")

print(f"Instructions: ", end='')
for op in ops:
    print(f"{op}, ", end='')
print()

def decode_operand(operand, regA, regB, regC) -> int:
    if operand in range(0, 3+1):
        return operand
    if operand == 4:
        return regA
    if operand == 5:
        return regB
    if operand == 6:
        return regC
    if operand == 7:
        raise ValueError("Invalid use of reserved operand")

def compute(ops, regA, regB, regC) -> int:
    pointer = 0
    while pointer < len(ops):
        instruction = ops[pointer][0]
        operand = ops[pointer][1]

        match instruction:
            case 0:
                regA = regA >> decode_operand(operand, regA, regB, regC)

            case 1:
                regB = regB ^ operand
            
            case 2:
                regB = decode_operand(operand, regA, regB, regC) & 7

            case 3:
                if regA != 0:
                    pointer = operand - 1

            case 4:
                regB = regC ^ regB

            case 5:
                return (decode_operand(operand, regA, regB, regC) & 7)

            case 6:
                regB = regA >> decode_operand(operand, regA, regB, regC)

            case 7:
                regC = regA >> decode_operand(operand, regA, regB, regC)

        pointer += 1


regA = 0
matched = len(ops) * 2 - 1
stack = [0]

while len(stack) <= len(ops) * 2:
    found = False
    idx = len(ops) * 2 - len(stack)
    start = stack[len(stack) - 1]

    t = ops[int (idx / 2)][idx % 2]

    for x in range(start, 8):
        rez = compute(ops, (regA << 3) + x, 0, 0)

        if rez == t:
            regA = (regA << 3) + x
            found = True
            stack[len(stack) - 1] = x + 1
            break

    if found:
        stack.append(0)
        continue

    regA = regA >> 3
    stack.pop(len(stack) - 1)

print(regA)
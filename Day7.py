from math import *

#First Puzzle Solution
file = open("Puzzle Inputs/Puzzle 13.txt")
sol = []
val = []
correct = False
sum = 0
operators = ['+', '*']

#Decided the easiest would probably be backtracking
def back(k, res, max_res):
    global sol
    global val
    global correct

    if k == len(val):
        return

    for i in range (0, len(operators)):
        if operators[i] == '+':
            res += int(val[k])
        if operators[i] == '*':
            res *= int(val[k])

        if res <= max_res:
            if res == max_res:
                correct = True
            if not correct:
                back(k + 1, int(res), max_res)

        if operators[i] == '+':
            res -= int(val[k])
        if operators[i] == '*':
            res /= int(val[k])


for line in file:
    correct = False
    result = int(line.split(":")[0])
    val = line.split(":")[1].split(" ")
    
    #The split leaves an empty string at the 0th index
    val.pop(0)

    back(1, int(val[0]), result)

    if correct:
        sum += result

    print(f'{result} : {val}')

print(sum)

#Second Puzzle Solution
print("Second Puzzle")
print("----------------")

file = open("Puzzle Inputs/Puzzle 13.txt")
sol = []
val = []
correct = False
sum = 0
operators = ['+', '*', '||']

#Was lucky to be right in my assumption the second half would also be bkt
def back(k, res, max_res):
    global sol
    global val
    global correct

    if k == len(val):
        return

    for i in range (0, len(operators)):
        if operators[i] == '+':
            res += int(val[k])
        if operators[i] == '*':
            res *= int(val[k])
        if operators[i] == '||':
            res = int(str(res) + str(val[k]))

        if res <= max_res:
            if res == max_res:
                correct = True
            if not correct:
                back(k + 1, int(res), max_res)

        if operators[i] == '+':
            res -= int(val[k])
        if operators[i] == '*':
            res = floor(res / int(val[k]))
        if operators[i] == '||':
            res = int(str(res).removesuffix(str(val[k])))


for line in file:
    correct = False
    result = int(line.split(":")[0])
    val = line.split(":")[1].split(" ")
    val.pop(0)

    back(1, int(val[0]), result)

    if correct:
        sum += result

    print(f'{result} : {val}')

print(sum)
#Solution for the second puzzle takes considerably longer but I don't think there's a faster solution
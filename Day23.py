from collections import defaultdict

file = open("PuzzleIn.txt")

connections = defaultdict(list)
solutions = set()
def find_set(depth:int, stack:list, x:str):
    if depth == 2:
        if x in connections[stack[depth]]:
            solutions.add(tuple(sorted(stack[:depth + 1])))
        return
    for connect in connections[stack[depth]]:
        stack.append(connect)
        find_set(depth + 1, stack, x)
        stack.pop()

def check_valid(depth, stack):
    for k in stack[:depth]:
        if stack[depth] == k or k not in connections[stack[depth]]:
            return False
    return True

def find_lan(depth:int, stack:list):
    if tuple(sorted(stack[:depth+1])) in solutions:
        return
    for connect in connections[stack[depth]]:
        stack.append(connect)
        if check_valid(depth, stack):
            find_lan(depth + 1, stack)  
            if depth > 1:
                solutions.add(tuple(sorted(stack[:depth + 1])))
        stack.pop()


for line in file:
    ch = line.rstrip('\n').split('-')
    connections[ch[0]].append(ch[1])
    connections[ch[1]].append(ch[0])

#Part 1:
for x in [key for key in connections if key.startswith('t')]:
    find_set(0, [x], x)

print (len(solutions))

#Part 2:
for x in connections:
    find_lan(0, [x])

a = max([len(sol) for sol in solutions])
for sol in solutions:
    if len(sol) == a:
        print(','.join([val for val in sol]))
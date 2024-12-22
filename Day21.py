import time
file = open("PuzzleIn.txt")

numpad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [' ', '0', 'A']
]

dirpad = [
    [' ', '^', 'A'],
    ['<', 'v', '>']
]

def posNumpad(num):
    match num:
        case '0':
            return (3, 1)
        case '1':
            return (2, 0)
        case '2':
            return (2, 1)
        case '3':
            return (2, 2)
        case '4':
            return (1, 0)
        case '5':
            return (1, 1)
        case '6':
            return (1, 2)
        case '7':
            return (0, 0)
        case '8':
            return (0, 1)
        case '9':
            return (0, 2)
        case 'A':
            return (3, 2)
        case _:
            raise ValueError("Invalid numberpad input! " + str(num))
        
def posDirpad(dir):
    match dir:
        case '<':
            return (1, 0)
        case 'v':
            return (1, 1)
        case '>':
            return (1, 2)
        case '^':
            return (0, 1)
        case 'A':
            return (0, 2)
        case _:
            raise ValueError("Invalid directionpad input! " + dir)


def withinBounds(x, y, pad):
    if pad == 'number':
        return x >= 0 and y >= 0 and x < 4 and y < 4 and not(x == 3 and y == 0)
    else:
        return x >= 0 and y >= 0 and x < 2 and y < 2 and not(x == 0 and y == 0)

chunks = {}
paths = {}
_dirrobos = 1

def expandCtrl (depth, pad:str):  
    global chunks
    global fuck
    if pad == 'number':
        start = posNumpad('A')
    else:
        start = posDirpad('A')

    s = 0
    copy = chunks.copy()
    for chunk in list(chunks.keys()): 
        if depth >= _dirrobos:
            s += chunks[chunk] * len(chunk)
            continue

        if copy[chunk] == 0:
            continue

        copy[chunk] -= chunks[chunk]
        expandedStr = ''  

        if paths.get((chunk, pad), -1) != -1:
            expandedStr += paths[(chunk, pad)]

            print(f'{depth}: {chunk} ---> {expandedStr}')
            result = expandedStr.split('A')
            result.pop()
            for part in result:
                part += 'A'
                if copy.get(part, -1) == -1:
                    copy[part] = 0
                copy[part] += chunks[chunk]

            continue

        for char in chunk:
            if pad == 'number':
                end = posNumpad(char)
            else:
                end = posDirpad(char)

            if paths.get((start, end, pad), -1) != -1:
                expandedStr += paths[(start, end, pad)]
                start = end
                continue

            start_cpy = (start[0], start[1])
            
            diry = start[0] - end[0]
            dirx = start[1] - end[1]
            auxStr = ''

            while dirx != 0 or diry != 0:
                while dirx > 0:
                    if (pad == 'number' and numpad[start[0]][start[1] - dirx] == ' ') or (pad != 'number' and dirpad[start[0]][start[1] - dirx] == ' '):
                        break
                    auxStr += '<'
                    dirx -= 1
                    start = (start[0], start[1] - 1)
                while diry < 0:
                    if (pad == 'number' and numpad[start[0] - diry][start[1]] == ' ') or (pad != 'number' and dirpad[start[0] - diry][start[1]] == ' '):
                        break
                    auxStr += 'v'
                    diry += 1
                    start = (start[0] + 1, start[1])
                while diry > 0:
                    if (pad == 'number' and numpad[start[0] - diry][start[1]] == ' ') or (pad != 'number' and dirpad[start[0] - diry][start[1]] == ' '):
                        break
                    auxStr += '^' 
                    diry -= 1
                    start = (start[0] - 1, start[1])
                while dirx < 0:
                    if (pad == 'number' and numpad[start[0]][start[1] - dirx] == ' ') or (pad != 'number' and dirpad[start[0]][start[1] - dirx] == ' '):
                        break
                    auxStr += '>'
                    dirx += 1
                    start = (start[0], start[1] + 1)
            auxStr += 'A'

            paths[(start_cpy, end, pad)] = auxStr
            expandedStr += auxStr

        paths[(chunk, pad)] = expandedStr

        print(f'{depth}: {chunk} ---> {expandedStr}')
        result = expandedStr.split('A')
        result.pop()
        for part in result:
            part += 'A'
            if copy.get(part, -1) == -1:
                copy[part] = 0
            copy[part] += chunks[chunk]

    chunks = copy
    
    if depth >= _dirrobos:
        return s

    return expandCtrl(depth + 1, pad)

s = 0
t1 = time.time()
for line in file:
    _dirrobos = 1
    chunks.clear()
    line = line.rstrip('\n')
    rez = int(line.rstrip('A'))

    chunks[line] = 1
    x = expandCtrl(0, 'number')
    _dirrobos = 25
    x = expandCtrl(0, 'dirpad')

    print (f'x:{x} * r:{rez}  ---  {x * rez}')
    rez *= x
    s += rez
t2 = time.time()
print (s)
print (t2-t1)
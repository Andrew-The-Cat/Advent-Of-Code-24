#First and Second Puzzle Solution
#In the middle of figuring out the first solution a far better way to do cheating hit me
#This time I've built functions for all the useful stuff so no need to copy the code again

file = open("PuzzleIn.txt")

race_tr = []
debug_tr = []
start = ()
end = ()

for i, line in enumerate(file):
    race_tr.append([])
    for j, char in enumerate(line):
        if char == 'S':
            start = (i, j)
            race_tr[i].append(1)
            continue
        elif char == 'E':
            end = (i, j)
        
        if char == '#':
            race_tr[i].append(-1)
        else:
            race_tr[i].append(0)

def within_bounds(x, y):
    global race_tr
    return x >= 0 and x < len(race_tr) and y >= 0 and y < len(race_tr)

def copy_mat(mat:list, mat_cpy:list) -> list:
    mat_cpy.clear()
    for line in mat:
        mat_cpy.append(line.copy())

    return mat_cpy


def r_search(x, y, track, radius, pico_saves):
    for i in range(-radius, radius + 1):
        for j in range(-radius, radius + 1):
            if abs(i) + abs(j) > radius:
                continue

            s_x = x + i
            s_y = y + j

            if within_bounds(s_x, s_y) and track[s_x][s_y] != -1:
                pico_save = track[s_x][s_y] - track[x][y] - (abs(i) + abs(j))
                if pico_save <= 0:
                    continue

                if pico_saves.get(pico_save, -1) == -1:
                    pico_saves[pico_save] = 0

                pico_saves[pico_save] += 1


def Lee(track, start, end, radius = 0, cheats = False):    
    queue = [start]
    pico_saves = {}

    dl = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    debug_tr = copy_mat(track, [])

    while len(queue) > 0:
        pos = queue.pop(0)

        if not cheats and pos == end:
            return track[pos[0]][pos[1]]

        if cheats:
            debug_tr[pos[0]][pos[1]] = 'O'

            r_search(pos[0], pos[1], track, radius, pico_saves)

        for k in range(0, 4):
            new_l = pos[0] + dl[k]
            new_c = pos[1] + dc[k]

            if track[new_l][new_c] != -1 and (track[new_l][new_c] > track[pos[0]][pos[1]] or track[new_l][new_c] == 0):
                track[new_l][new_c] = track[pos[0]][pos[1]] + 1
                queue.append((new_l, new_c))

    if cheats:
        for line in debug_tr:
            for char in line:
                if char == -1:
                    print ('#', end='  ')
                else:
                    print(char, end='  ')
            print()
        return pico_saves

print (Lee(race_tr, start, end))

saves_p1 = Lee(copy_mat(race_tr, []), start, end, 2, True)
print (saves_p1)

cnt = 0
for key in list(saves_p1.keys()):
    if key >= 100:
        cnt += saves_p1[key]    

print (cnt)

cnt = 0
saves_p2 = Lee(copy_mat(race_tr, []), start, end, 20, True)
for key in list(saves_p2.keys()):
    if key >= 100:
        print (f'{key}: {saves_p2[key]}, ', end='') 
        cnt += saves_p2[key]   

print()
print (cnt)



with open('input.txt', 'r') as file:
    content = file.read()

map_v, moves = list(content.split('\n\n'))
map_lines = map_v.split("\n")

map_lines = list(map(list, map_lines))

moves = moves.replace("\n", "")



def update_map():
    new_map = []
    for y, row in enumerate(map_lines):
        for x, v in enumerate(row):
            if v == "#":
                map_lines[y][x] = "##"
            elif v == "O":
                 map_lines[y][x] = "[]"
            elif v == "@":
                 map_lines[y][x] = "@."
            else:
                 map_lines[y][x] = ".."
        new_map += ["".join(map_lines[y])]
    return new_map

map_lines = list(map(list,update_map()))


def find_at():
    at_pos = {}
    for y, row in enumerate(map_lines):
        for x, v in enumerate(row):
            if v == "@":
                at_pos['x'] = x
                at_pos['y'] = y 
                return at_pos

at_pos = find_at()




def recursive_update_left(y, x):
    if map_lines[y][x] == "#":
        return False
    elif map_lines[y][x] == "]":
        update = recursive_update_left(y, x-1)

        if update:
            map_lines[y][x], map_lines[y][x+1] = map_lines[y][x+1], map_lines[y][x]
            return True
        else:
            return False 
    elif map_lines[y][x] == "[":
        update = recursive_update_left(y, x-1)

        if update:
            map_lines[y][x], map_lines[y][x+1] = map_lines[y][x+1], map_lines[y][x]
            return True
        else:
            return False
    else:
        map_lines[y][x], map_lines[y][x+1] = map_lines[y][x+1], map_lines[y][x]
        return True
    
def recursive_update_right(y, x):
    if map_lines[y][x] == "#":
        return False
    elif map_lines[y][x] == "]":
        update = recursive_update_right(y, x+1)

        if update:
            map_lines[y][x], map_lines[y][x-1] = map_lines[y][x-1], map_lines[y][x]
            return True
        else:
            return False
        
    elif map_lines[y][x] == "[":
        update = recursive_update_right(y, x+1)

        if update:
            map_lines[y][x], map_lines[y][x-1] = map_lines[y][x-1], map_lines[y][x]
            return True
        else:
            return False
    else:
        map_lines[y][x], map_lines[y][x-1] = map_lines[y][x-1], map_lines[y][x]
        return True
    
    
def recursive_update_up(y, x):
    if map_lines[y][x] == "#":
        return False
    elif map_lines[y][x] == "]":
        update_r = recursive_update_up(y-1, x)
        update_l = recursive_update_up(y-1, x-1)

        if update_r and update_l:
            map_lines[y][x], map_lines[y+1][x] = map_lines[y+1][x], map_lines[y][x]
            return True
        else:
            return False
    elif map_lines[y][x] == "[":
        update_r = recursive_update_up(y-1, x)
        update_l = recursive_update_up(y-1, x+1)

        if update_r and update_l:
            map_lines[y][x], map_lines[y+1][x] = map_lines[y+1][x], map_lines[y][x]
            return True
        else:
            return False
    else:
        map_lines[y][x], map_lines[y+1][x] = map_lines[y+1][x], map_lines[y][x]
        return True
    
def recursive_update_down(y, x):
    if map_lines[y][x] == "#":
        return False
    elif map_lines[y][x] == "]":
        update_r = recursive_update_down(y+1, x)
        update_l = recursive_update_down(y+1, x-1)

        if update_r and update_l:
            map_lines[y][x], map_lines[y-1][x] = map_lines[y-1][x], map_lines[y][x]
            return True
        else:
            return False
        
    elif map_lines[y][x] == "[":
        update_l = recursive_update_down(y+1, x)
        update_r = recursive_update_down(y+1, x+1)

        if update_r and update_l:
            map_lines[y][x], map_lines[y-1][x] = map_lines[y-1][x], map_lines[y][x]
            return True
        else:
            return False
    else:
        map_lines[y][x], map_lines[y-1][x] = map_lines[y-1][x], map_lines[y][x]
        return True

for r in map_lines:
    print("".join(r))
print(" ")


for m in moves:
    y, x = at_pos['y'], at_pos['x']
    map_copy = [line[:] for line in map_lines]
    if m == "<":
        update = recursive_update_left(y, x-1)
        if update:
            at_pos['x'] -=1
    elif m == ">":
         update = recursive_update_right(y, x+1)
         if update:
            at_pos['x'] +=1
    elif m == "^":
        
        update = recursive_update_up(y-1, x)
        if update:
            at_pos['y'] -=1
        else:
            map_lines = map_copy
    else:
         update = recursive_update_down(y+1, x)
         if update:
            at_pos['y'] +=1
         else:
            map_lines = map_copy
    
   
    
total  = 0
total  = 0
for y, row in enumerate(map_lines):
    for x, v in enumerate(row):
        if v == "[":
            total += 100*y + x 

print(total)


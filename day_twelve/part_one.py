import pandas as pd
import numpy as np
import time

# Start the timer
start_time = time.time()


visited = set()





df = pd.read_csv('input.txt', header=None)
grid = df.to_numpy()
input = np.array([row[0] for row in grid])

row_len, col_len = len(input[0]) , len(input)

visited = set()
perimeter_vis = set()

def in_farm(x, y):
    return x >= 0 and y >= 0 and x <= row_len - 1 and y <= col_len -1


def search_for_region(letter, x, y):
    pos = (y, x)
    if input[y][x] == letter and pos not in visited:
        visited.add(pos)
        # up
        up = 0
        up_pos = (y-1, x)
        if in_farm(x, y-1) and up_pos not in visited:
            up = search_for_region(letter, x, y-1)
        
        # down
        down = 0
        down_pos = (y+1, x)
        if in_farm(x, y+1) and down_pos not in visited:
            down = search_for_region(letter, x, y+1)
        
        # left
        left = 0
        left_pos = (y, x-1)
        if in_farm(x-1, y) and left_pos not in visited:
            left = search_for_region(letter, x-1, y)
        
        # right 
        right = 0
        right_pos = (y, x+1)
        if in_farm(x+1, y) and right_pos not in visited:
            right = search_for_region(letter, x+1, y)
        
        return 1 + up + down + left + right
    else:
        return 0
    

def get_perimeter(letter, x, y, local_perimeter):
    pos = (y, x)

    if input[y][x] == letter:
        # continue 
        if pos not in local_perimeter:
            local_perimeter.add(pos)
            #up
            up = 0
            if in_farm(x, y-1):
                up =  get_perimeter(letter, x, y-1, local_perimeter)
            else:
                up = 1

            
            # down
            down = 0
            if in_farm(x, y+1):
                down =  get_perimeter(letter, x, y+1, local_perimeter)
            else:
                down = 1

             # left
            left = 0
            if in_farm(x-1, y):
                left =  get_perimeter(letter, x-1, y, local_perimeter)
            else:
                left = 1

             # right
            right = 0
            if in_farm(x+1, y):
                right =  get_perimeter(letter, x+1, y, local_perimeter)
            else:
                right = 1


            return up + down + left + right

        else:
            return 0
    else:
        return 1




ans = 0
for y, row in enumerate(input):
    for x, val in enumerate(row):
        area = 0
        if (y, x) not in visited:
            area = search_for_region(val, x, y)
            
        
        perimeter = 0
        if (y, x) not in perimeter_vis:
            local_perimeter = set()
            perimeter = get_perimeter(val, x, y, local_perimeter)
            
            perimeter_vis = perimeter_vis | local_perimeter

        ans += area*perimeter
print(ans)
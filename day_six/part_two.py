import pandas as pd
import numpy as np
import time

start_time = time.time()

# Read the space-delimited file
df = pd.read_csv('input.txt', delim_whitespace=True, header=None)

def convert_array(array):
    
    return array[0]

np_array = df.to_numpy()
map_array = list(map(convert_array, np_array))

arrow_position = {}
row_end = len(np_array) - 1
col_end = len(np_array[0][0]) - 1
for i, row in enumerate(map_array):
    for j, val in enumerate(row):
        if val == "^" or val == ">" or val == "v" or val == "<":
            arrow_position['x'] , arrow_position['y'], arrow_position['direction'] = j, i, val 
            break


start_position = arrow_position.copy()


def updated_visited_position(x, y, direction, visited_blocks): 

    ### if visited with 
    if (direction in visited_blocks):
        if (x in visited_blocks[direction]):
            if (y in visited_blocks[direction][x]):
                return True
            else:
                visited_blocks[direction][x][y] = True
        else:
             visited_blocks[direction][x] = {y: True}
    else:
        visited_blocks[direction] = {x: {y: True}}

    return False




updated_map = map_array

def search_for_route(updated_array):
    routes = 0
    visited_blocks = {}
    arrow_position = start_position.copy()
    while True:
        if arrow_position['x'] == 0 or arrow_position['x'] == row_end or arrow_position['y'] == 0 or arrow_position['y'] == col_end:
            break 
        
        elif updated_visited_position(arrow_position['x'], arrow_position['y'], arrow_position['direction'], visited_blocks):
            routes += 1
            break
        
        else:
            if arrow_position['direction'] == '^':
                if updated_array[arrow_position['y']-1][arrow_position['x']] == "#":
                    arrow_position['direction'] = ">"
                else:
                    arrow_position['y'] -= 1
                
            elif arrow_position['direction'] == ">":
                if updated_array[arrow_position['y']][arrow_position['x']+1] == "#":
                    arrow_position['direction'] = "v"
                else:
                    arrow_position['x'] += 1
            
            elif arrow_position['direction'] == "<":
                if updated_array[arrow_position['y']][arrow_position['x']-1] == "#":
                    arrow_position['direction'] = "^"
                else:
                    arrow_position['x'] -= 1
            
            else:
                if updated_array[arrow_position['y']+1][arrow_position['x']] == "#":
                    arrow_position['direction'] = "<"
                else:
                    arrow_position['y'] += 1

    return routes

ans = 0
for i, row in enumerate(map_array):
    for j, col in enumerate(row):
        if map_array[i][j] == ".":
           updated_map_list = list(updated_map[i])

           # Update the specific index
           updated_map_list[j] = "#"

        # Convert back to string
           updated_map[i] = "".join(updated_map_list)
           ans += search_for_route(updated_map)
           # do search 
           updated_map_list = list(updated_map[i])

           # Update the specific index
           updated_map_list[j] = "."

           # Convert back to string
           updated_map[i] = "".join(updated_map_list)


print(ans)

end_time = time.time()

# Calculate runtime in microseconds
runtime_microseconds = (end_time - start_time) * 1_000_000
print(f"Runtime: {runtime_microseconds:.2f} microseconds")
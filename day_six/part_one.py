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


visited_blocks = {}

def updated_visited_position(x, y): 
    if (x in visited_blocks):
        if (y not in visited_blocks[x]):
            visited_blocks[x][y] = 1
    else:
        visited_blocks[x] = {y: 1}



while True:
    if arrow_position['x'] == 0 or arrow_position['x'] == row_end or arrow_position['y'] == 0 or arrow_position['y'] == col_end:
        break 
    else:
        if arrow_position['direction'] == '^':
            
            if map_array[arrow_position['y']-1][arrow_position['x']] == "#":
                arrow_position['direction'] = ">"
            else:
                updated_visited_position(arrow_position['x'], arrow_position['y'])
                arrow_position['y'] -= 1
            
        elif arrow_position['direction'] == ">":
             if map_array[arrow_position['y']][arrow_position['x']+1] == "#":
                arrow_position['direction'] = "v"
             else:
                updated_visited_position(arrow_position['x'], arrow_position['y'])
                arrow_position['x'] += 1
        
        elif arrow_position['direction'] == "<":
             if map_array[arrow_position['y']][arrow_position['x']-1] == "#":
                arrow_position['direction'] = "^"
             else:
                updated_visited_position(arrow_position['x'], arrow_position['y'])
                arrow_position['x'] -= 1
        
        else:
            if map_array[arrow_position['y']+1][arrow_position['x']] == "#":
                arrow_position['direction'] = "<"
            else:
                updated_visited_position(arrow_position['x'], arrow_position['y'])
                arrow_position['y'] += 1

count = 1
for x in visited_blocks:
    for y in visited_blocks[x]:
        count += visited_blocks[x][y]
print(count)


end_time = time.time()

# Calculate runtime in microseconds
runtime_microseconds = (end_time - start_time) * 1_000_000
print(f"Runtime: {runtime_microseconds:.2f} microseconds")
import pandas as pd
import numpy as np
import time

# Start the timer
start_time = time.time()

def convert_to_list(array):
    
    str_arr = list(map(int, list(array)))
    return str_arr


df = pd.read_csv('input.txt', header=None, names=['num'], dtype={'num': str})
grid = df.to_numpy()
input = np.array([convert_to_list(row[0]) for row in grid])

row_len, col_len = len(input[0]) , len(input)


def find_score(val, x, y, visited):
    if val == 9:
        return 1
    else:

        # four paths 
        # left x - 1 >=0 
        # right x + 1 <= len_row - 1
        # up y - 1 >= 0 
        # down y + 1 <= len_col - 1

        path_one = 0 
        if ((x-1) >= 0):
            pos = (x-1, y)
            if (input[y][x-1] - val == 1 ):
                visited.add(pos)
                path_one = find_score(input[y][x-1], x-1, y, visited)
            
        
        path_two = 0
        if ((x+1) <= (row_len - 1)):
            pos = (x+1, y)
            if (input[y][x+1] - val == 1 ):
                visited.add(pos)
                path_two = find_score(input[y][x+1], x+1, y, visited)
            
        
        path_three = 0
        if ((y-1) >= 0):
            pos = (x, y-1)
            if ((input[y-1][x] - val) == 1 ):
                visited.add(pos)
                path_three = find_score(input[y-1][x], x, y-1, visited)
            
        
        path_four = 0
        if ((y+1) <= (col_len - 1)):
            pos = (x, y+1)
            if ((input[y+1][x] - val) == 1):
                visited.add(pos)
                path_four = find_score(input[y+1][x], x, y+1, visited)
            
        
        return path_one + path_two + path_three + path_four


count = 0
for i, row in enumerate(input):
    for j, col in enumerate(row):
        if col == 0:
            visited = set()
            routes = find_score(col, j, i, visited)
         
            count += routes

print(count)

end_time = time.time()

# Calculate runtime
runtime = (end_time - start_time) * 1_000_000
print(f"Runtime: {runtime:.2f} microseconds")
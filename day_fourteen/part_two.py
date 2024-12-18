
import pandas as pd
import numpy as np
import re
import sys
import time

# Start the timer
start_time = time.time()


with open('input.txt', 'r') as file:
    content = file.read()

parts = list(content.split('\n'))
robots = {}
for i, p in enumerate(parts):

    pv_split = p.split(" ")
    p, v = pv_split[0], pv_split[1]

    _, coordinates = p.split("=")
    p_x, p_y = map(int, coordinates.split(","))
   

    _, coordinates = v.split("=")
    v_x, v_y = map(int, coordinates.split(","))
    robots[i] = {'px':p_x, 'py':p_y, 'vx':v_x, 'vy':v_y}



def move_robot(robot_id):

    # move x
    robots[robot_id]['px'] = (robots[robot_id]['px'] + robots[robot_id]['vx'])%101

    # move y
    
    robots[robot_id]['py'] = (robots[robot_id]['py'] + robots[robot_id]['vy']) % 103
    


def print_grid():
    """
        print robots in grid
    """
    grid = []
    for i in range(103):
        grid.append(list("."*101))

    for r in robots.keys():
        grid[robots[r]['py']][robots[r]['px']] = "*"

    
    
    return grid

def find_line_with_stars(grid, min_stars=7):
    """Find a line with more than 'min_stars' consecutive '*' characters."""
    for row_index, row in enumerate(grid):
        consecutive_stars = 0
        for char in row:
            if char == '*':
                consecutive_stars += 1
                if consecutive_stars > min_stars:
                    return row_index, row  # Return the line index and content
            else:
                consecutive_stars = 0
    return None, None
   

for i in range(10000):
    for j in robots.keys():
        move_robot(j)  
    grid = print_grid()   
    grid = ["".join(row) for row in grid]

    line_index, line_content = find_line_with_stars(grid, min_stars=7)

        
    if line_index is not None:
        output_file = "output_grid.txt"
        with open(output_file, "a") as file:

        

            
            for row in grid:
                file.write(row + "\n")  # Write each row and add a newline

            file.write("\n\n"+ str(i) + "\n\n")


    

q_one, q_two, q_three, q_four = 0, 0, 0, 0

# for r in robots.keys():
#     if robots[r]['px'] < 50 and robots[r]['py'] < 51:
#         q_one += 1
#     elif robots[r]['px'] > 50 and robots[r]['py'] < 51:
#         q_two += 1
#     elif robots[r]['px'] < 50 and robots[r]['py'] > 51:
#         q_three += 1
#     elif robots[r]['px'] > 50 and robots[r]['py'] > 51:
#         q_four += 1 
#     else:
#         pass

# print(q_one*q_two*q_three*q_four)
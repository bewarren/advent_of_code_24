
import pandas as pd
import numpy as np
import re
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
    


def get_quadrant_robots(robots):
    """
        Get number of robots in each quadrant
    """

for i in range(100):
    for j in robots.keys():
        move_robot(j)
    
q_one, q_two, q_three, q_four = 0, 0, 0, 0

for r in robots.keys():
    if robots[r]['px'] < 50 and robots[r]['py'] < 51:
        q_one += 1
    elif robots[r]['px'] > 50 and robots[r]['py'] < 51:
        q_two += 1
    elif robots[r]['px'] < 50 and robots[r]['py'] > 51:
        q_three += 1
    elif robots[r]['px'] > 50 and robots[r]['py'] > 51:
        q_four += 1 
    else:
        pass

print(q_one*q_two*q_three*q_four)

import pandas as pd
import numpy as np
import re
import time

# Start the timer
start_time = time.time()


df = pd.read_csv('input.txt', header=None)
grid = df.to_numpy()
input = np.array([row for row in grid])

input_len = len(input)



total_cost = 0
for i in range(0, input_len, 3):

    # A button 
    a_x, a_y = re.search(r'X\+(\d+)', input[i][0]), re.search(r'Y\+(\d+)', input[i][1])
    b_x, b_y = re.search(r'X\+(\d+)', input[i+1][0]), re.search(r'Y\+(\d+)', input[i+1][1])
    p_x, p_y = re.search(r'X\=(\d+)', input[i+2][0]), re.search(r'Y\=(\d+)', input[i+2][1])

    if a_x and a_y and b_x and b_y and p_x and p_y:
        Ax, Ay, Bx, By, Px, Py = int(a_x.group(1)), int(a_y.group(1)), int(b_x.group(1)), int(b_y.group(1)), int(p_x.group(1)), int(p_y.group(1))

        p_one_solution, p_two_solution = 0, 0
        for p_one in range(1,101):
            lhs = Ay*p_one + (By/Bx)*(Px - Ax*p_one)
            if abs(lhs - Py) < 1e-9:
                p_one_solution = p_one

        for p_two in range(1,101):
            lhs = (Ay/Ax)*(Px - Bx*p_two) + By*p_two
            if abs(lhs - Py) < 1e-9:
                p_two_solution = p_two


        total_cost += p_one_solution*3 + p_two_solution
    
print(total_cost)
row_len, col_len = len(input[0]) , len(input)
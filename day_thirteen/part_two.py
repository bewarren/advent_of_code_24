
import pandas as pd
import numpy as np
import re
from sympy import symbols, Eq, solve
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

        Px = 10_000_000_000_000 + Px
        Py = 10_000_000_000_000 + Py



        a, b = symbols('a b', integer=True)
        eq1 = Eq(Ax * a + Bx * b, Px)
        eq2 = Eq(Ay * a + By * b, Py)
        soln = solve((eq1, eq2), (a, b))
        
        if soln:
            apresses, bpresses = soln[a], soln[b]
            tokens = 3 * apresses + 1 * bpresses
            
            total_cost += tokens
    
print(total_cost)
row_len, col_len = len(input[0]) , len(input)
import pandas as pd 
import numpy as np
import time

# Start the timer
start_time = time.time()

df = pd.read_csv('input.txt', header=None)

ans = 0
for index, row in df.iterrows():
    int_list = list(map(int,row.to_numpy()[0].split()))
    n_row = np.array(int_list)
    
    increasing = n_row[0] < n_row[1]
    decreasing = n_row[0] > n_row[1]
    for i in range(len(n_row)-1):
        difference = abs(n_row[i] - n_row[i+1])
        if (increasing and n_row[i] < n_row[i+1] and difference >= 1 and difference <= 3):
            pass
        elif (decreasing and n_row[i] > n_row[i+1] and difference >= 1 and difference <= 3):   
            pass
        else:
            ans -=1
            break
    ans += 1

print(ans)

end_time = time.time()
runtime = (end_time - start_time) * 1_000_000
print(f"Runtime: {runtime:.2f} microseconds")
import pandas as pd
import numpy as np
import time

# Start the timer
start_time = time.time()

# Read the space-delimited file
df = pd.read_csv('input.txt', delim_whitespace=True, header=None, names=['Left', 'Right'])


left = np.sort(df["Left"].to_numpy())
right = np.sort(df["Right"].to_numpy())

ans = 0 
for l, r in zip(left, right):
    ans += abs(l-r)
print(ans)

end_time = time.time()

# Calculate runtime
runtime = (end_time - start_time) * 1_000_000
print(f"Runtime: {runtime:.2f} microseconds")

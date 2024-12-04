import pandas as pd
import numpy as np
import time

# Start the timer
start_time = time.time()

# Read the input file
df = pd.read_csv('input.txt', header=None)

def is_safe(arr):
    """Check if a sequence is safe."""
    increasing = arr[0] < arr[1]
    for i in range(len(arr) - 1):
        difference = abs(arr[i] - arr[i+1])
        if (increasing and arr[i] >= arr[i+1]) or (not increasing and arr[i] <= arr[i+1]) or difference > 3:
            return False
    return True

def safe_with_dampener(arr):
    """Check if the sequence can be made safe by removing one element."""
    for i in range(len(arr)):
        modified_arr = np.delete(arr, i)  # Remove the i-th element
        if is_safe(modified_arr):
            return True
    return False

# Main logic
ans = 0

for index, row in df.iterrows():
    # Convert row to an integer array
    int_list = list(map(int, row.to_numpy()[0].split()))
    n_row = np.array(int_list)

    if is_safe(n_row):
        ans += 1
    elif safe_with_dampener(n_row):
        ans += 1

print(f"Number of safe reports: {ans}")


end_time = time.time()
runtime = (end_time - start_time) * 1_000_000
print(f"Runtime: {runtime:.2f} microseconds")

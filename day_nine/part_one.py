import pandas as pd
import numpy as np
import time

# Start the timer
start_time = time.time()

df = pd.read_csv('input.txt', header=None)
grid = df.to_numpy()
input = str(np.array([row[0] for row in grid])[0])




output = []
id = 0
input_len = len(input) 


for i in range(0, input_len, 2):
    output += [str(id)]*int(input[i])
    if (i < len(input) -1):
        output += "."*int(input[i+1])
    
    id += 1

# sliding window


output_len = len(output)
i, j = 0, output_len -1

while (i < j):
    if output[i] == ".":
        if output[j].isdigit():
            
            output[i], output[j] = output[j], output[i]
            i += 1
            j -= 1
        else:
            j -= 1
    else:
        i += 1


ans = 0
for i, val in enumerate(output):
    if (val.isdigit()):
        ans += i * int(val)
    else:
        break

print(ans)

end_time = time.time()

# Calculate runtime
runtime = (end_time - start_time) * 1_000_000
print(f"Runtime: {runtime:.2f} microseconds")

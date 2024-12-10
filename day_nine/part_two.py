import pandas as pd
import numpy as np
import time

# Start the timer
start_time = time.time()

df = pd.read_csv('test.txt', header=None)
grid = df.to_numpy()
input = str(np.array([row[0] for row in grid])[0])




output = []
id = 0
input_len = len(input) 


for i in range(0, input_len, 2):
    output += [str(id)*int(input[i])]
    if (i < len(input) -1):
        output += "."*int(input[i+1])
    
    id += 1

# sliding window


output_len = len(output)
i, j = 0, output_len -1

print(output)

while (i < j):
    if output[i] == ".":
        if output[j].isdigit():
            if output[i: i+len(output[j])].count(".") >= len(output[j]):

                output[i:i+len(output[j])], output[j] = output[j], output[i:i+len(output[j])]
                print(output)
                i += len(output[j])
                j -= len(output[j])
            else:
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

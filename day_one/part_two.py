import pandas as pd
import numpy as np

# Read the space-delimited file
df = pd.read_csv('input.txt', delim_whitespace=True, header=None, names=['Left', 'Right'])


left = np.sort(df["Left"].to_numpy())
right = np.sort(df["Right"].to_numpy())

right_dic = {}

for r in right:
    if r in right_dic:
        right_dic[r] += 1
    else:
        right_dic[r] = 1

ans = 0
for l in left:
    if l in right_dic:
        ans += l*right_dic[l]

print(ans)
 
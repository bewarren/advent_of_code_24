import pandas as pd
import numpy as np
import time

# Start the timer
start_time = time.time()

# Read the file into a DataFrame
with open('input.txt', 'r') as file:
    content = file.read()

parts = content.split('\n\n')

part1_lines = parts[0].splitlines()
part2_lines = parts[1].splitlines()

look_up_ordering = {}
for lu in part1_lines:
    lu_split = lu.split("|")
    first, second = int(lu_split[0]), int(lu_split[1])
    if first in look_up_ordering:
        look_up_ordering[first].add(second)
    else:
        look_up_ordering[first] = set([second])


def reorder(unordered_array):
    new_array = unordered_array
    while True:
        ordered = True
        swap = False
        for i, val in enumerate(new_array):
            if i != len(new_array) - 1:
                for j, val_two in enumerate(new_array[i+1:]):
                    if int(val) in look_up_ordering:
                        if int(val_two) not in look_up_ordering[int(val)]:
                            ordered = False 
                            swap = True
                            new_array[i], new_array[j+i+1] = new_array[j+i+1], new_array[i]
                           
                            break
                            
                    else:
                        ordered = False
                        swap = True
                        new_array[i], new_array[-1] = new_array[-1], new_array[i]
                        
                        break
                if swap:
                    break
    
            if swap:
                break
        
        if ordered:
            break

    return unordered_array



ans = 0
for order in part2_lines:
    ordered = True
    order_split = order.split(",")
    for i, val in enumerate(order_split):
        if i != len(order_split) - 1:
            for val_two in order_split[i+1:]:
                if int(val) in look_up_ordering:
                    if int(val_two) in look_up_ordering[int(val)]:
                        pass 
                    else:
                        ordered = False 
                        break 
                else:
                    ordered = False
                    break
    if not ordered:
        new_array = reorder(order_split)
       
        mid =  int(new_array[(len(new_array) - 1) // 2])
        ans += mid


end_time = time.time()
runtime = (end_time - start_time) * 1_000_000
print(f"Runtime: {runtime:.2f} microseconds")

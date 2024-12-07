
import time

start_time = time.time()

def recurive_find_value(ans, value, values):
    if len(values) == 1:
        return (ans == value*values[0]) or (ans == value + values[0])
    else:
        return recurive_find_value(ans, values[0] + value, values[1:]) or recurive_find_value(ans, values[0] * value, values[1:])
        
        

with open('input.txt', 'r') as file:
    count = 0
    for line in file:
        split_line = line.split(": ")
        ans, values = int(split_line[0]), list(map(int, split_line[1].replace("\n", "").split(" ")))
        
        result = recurive_find_value(ans, values[0], values[1:])
        if result:
            count += ans

    print(count)


end_time = time.time()

# Calculate runtime in microseconds
runtime_microseconds = (end_time - start_time) * 1_000_000
print(f"Runtime: {runtime_microseconds:.2f} microseconds")
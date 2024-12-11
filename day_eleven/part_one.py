import time

# Start the timer
start_time = time.time()

input = [0, 7, 198844, 5687836, 58, 2478 ,25475,894]

def transform_number(num):
    if num == 0:
        return [1]
    
    if len(str(num)) % 2 == 0:
        str_num = str(num)
        return  [int(str_num[: len(str_num)//2]), int(str_num[len(str_num)//2: ])]
    else:
        return [num*2024]

for i in range(25):
   
   new_input = []
   for row in map(transform_number, input):
       new_input.extend(row)
   input = new_input

print(len(input))

end_time = time.time()

# Calculate runtime
runtime = (end_time - start_time) * 1_000_000
print(f"Runtime: {runtime:.2f} microseconds")
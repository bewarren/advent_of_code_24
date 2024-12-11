import time

# Start the timer
start_time = time.time()

input = [0, 7, 198844, 5687836, 58, 2478 ,25475,894]

# input = [125, 17]

dict_arr = {}
for i in input:
    dict_arr[i] = 1

def transform_number(num):
    if num == 0:
        return [1]
    
    if len(str(num)) % 2 == 0:
        str_num = str(num)
        return  [int(str_num[: len(str_num)//2]), int(str_num[len(str_num)//2: ])]
    else:
        return [num*2024]


for i in range(75):
    print(i+1)
    new_input = {}
    for k in list(dict_arr):
       for r in transform_number(k):
            if r in new_input:
               new_input[r] += dict_arr[k]
            else:
               new_input[r] = dict_arr[k]
    
       dict_arr[k] -= dict_arr[k]
    
    dict_arr = dict_arr | new_input

    for k in list(dict_arr):
        if dict_arr[k] == 0:
            del dict_arr[k]

    
    
    

print(sum(dict_arr.values()))

end_time = time.time()

# Calculate runtime
runtime = (end_time - start_time) * 1_000_000
print(f"Runtime: {runtime:.2f} microseconds")
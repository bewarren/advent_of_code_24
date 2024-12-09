import pandas as pd
import numpy as np
import time

# Start the timer
start_time = time.time()

df = pd.read_csv('input.txt', header=None)
grid = df.to_numpy()
array = np.array([row[0] for row in grid])

max_row = len(array) - 1
max_col = len(array[0]) -1 

antena_positions = {}

for i, row in enumerate(array):
    for j, character in enumerate(row):
        if character.isdigit() or character.isalpha():
            pos = {'y': i, 'x': j}
            if character in antena_positions:
                antena_positions[character].append(pos)
            else:
                antena_positions[character] =[pos]

unique_list = []
for character in antena_positions:
    if len(antena_positions[character]) > 1:
 
        for k, pos in enumerate(antena_positions[character]):
           
            for pos_two in antena_positions[character][k+1:]:
                x_dis = abs(pos_two['x'] - pos['x'])
                y_dis = abs(pos_two['y'] - pos['y'])

                x_anti_node, x_anti_node_two  = 0, 0
                y_anti_node, y_anti_node_two  = 0, 0

                
                multiply = 1
                
                while (x_anti_node >= 0 and y_anti_node >=0 and x_anti_node <= max_row and y_anti_node <= max_col):
                   
                    if (pos['x'] <= pos_two['x']):
                    
                        x_anti_node = pos['x']-x_dis*multiply  
                
                    else:
                        x_anti_node = pos['x'] + x_dis*multiply
                    

                
                    if pos['y'] <= pos_two['y']:

                        y_anti_node = pos['y']-y_dis *multiply
                
                    else:
                        y_anti_node = pos['y'] + y_dis*multiply
                     
                    
                    new_pos = {'x': x_anti_node, 'y': y_anti_node}
                    if new_pos not in unique_list and x_anti_node >= 0 and y_anti_node >=0 and x_anti_node <= max_row and y_anti_node <= max_col:
                        unique_list.append(new_pos)
                    
                    multiply += 1

                multiply = 1

                while (x_anti_node_two >= 0 and y_anti_node_two >=0 and x_anti_node_two <= max_row and y_anti_node_two <= max_col):

                    if (pos['x'] <= pos_two['x']):
                    
                        x_anti_node_two = pos_two['x'] + x_dis*multiply
                
                    else:
                        x_anti_node_two = pos_two['x'] - x_dis*multiply
                    

                
                    if pos['y'] <= pos_two['y']:

                        y_anti_node_two = pos_two['y'] + y_dis*multiply 
                
                    else:
                        y_anti_node_two = pos_two['y'] - y_dis*multiply


                    new_pos = {'x': x_anti_node_two, 'y': y_anti_node_two}
                    if new_pos not in unique_list and x_anti_node_two >= 0 and y_anti_node_two >=0 and x_anti_node_two <= max_row and y_anti_node_two <= max_col:
                        unique_list.append(new_pos)
                    
                    multiply += 1


ap_len = 0
for k in antena_positions:
    for pos in antena_positions[k]:
        if pos not in unique_list:
            unique_list.append(pos)
    
print(len(unique_list))
                

end_time = time.time()
runtime = (end_time - start_time) * 1_000_000
print(f"Runtime: {runtime:.2f} microseconds")

import pandas as pd
import numpy as np

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




                if (pos['x'] <= pos_two['x']):
                    
                    x_anti_node = pos['x']-x_dis  
                    x_anti_node_two = pos_two['x'] + x_dis 
                
                else:
                    x_anti_node = pos['x'] + x_dis
                    x_anti_node_two = pos_two['x'] - x_dis
                    

                
                if pos['y'] <= pos_two['y']:

                    y_anti_node = pos['y']-y_dis  
                    y_anti_node_two = pos_two['y'] + y_dis 
                
                else:
                    y_anti_node = pos['y'] + y_dis
                    y_anti_node_two = pos_two['y'] - y_dis
                   
                
                if (x_anti_node >= 0 and y_anti_node >=0 and x_anti_node <= max_row and y_anti_node <= max_col):
                    new_pos = {'x': x_anti_node, 'y': y_anti_node}
                    if new_pos not in unique_list:
                        unique_list.append(new_pos)

                if (x_anti_node_two >= 0 and y_anti_node_two >=0 and x_anti_node_two <= max_row and y_anti_node_two <= max_col):
                    new_pos = {'x': x_anti_node_two, 'y': y_anti_node_two}
                    if new_pos not in unique_list:
                        unique_list.append(new_pos)


print(len(unique_list))
                



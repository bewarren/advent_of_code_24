import re
import pandas as pd
import numpy as np

# Read the file into a DataFrame
df = pd.read_csv('input.txt', header=None)
grid = df.to_numpy()
array = np.array([list(row[0]) for row in grid])


def match_xmas(x, y):
    left_diag = array[x-1,y+1] + array[x, y] + array[x+1, y-1]
    right_diag = array[x-1, y-1] + array[x, y] + array[x+1, y+1]

    if (left_diag == "MAS" or left_diag[::-1] == "MAS") and (right_diag == "MAS" or right_diag[::-1] == "MAS"):
        return True
    else:
        return False

# Function to search in all directions
def find_xmas(grid):
    rows, cols = grid.shape
    matches = 0

    # Define all possible directions (dy, dx)
    
    # Function to check if a word exists starting at (x, y) in a given direction

    # Iterate through every cell in the grid
    for x in range(1, rows-1):
        for y in range(1,cols-1):
             if match_xmas(x, y):
                matches += 1

    return matches

# Find all occurrences of the word
total_matches = find_xmas(array)

# Print results
print(f"Total occurrences of XMAS: {total_matches}")


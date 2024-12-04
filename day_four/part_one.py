import pandas as pd
import numpy as np
import time

# Start the timer
start_time = time.time()

# Read the file into a DataFrame
df = pd.read_csv('input.txt', header=None)
grid = df.to_numpy()
array = np.array([list(row[0]) for row in grid])

word = "XMAS"

# Function to search in all directions
def find_word(grid, word):
    rows, cols = grid.shape
    matches = 0
    marked = np.full(grid.shape, ".", dtype=str)  # Mark the result grid with dots

    # Define all possible directions (dy, dx)
    directions = [
        (0, 1),  # Horizontal right
        (0, -1), # Horizontal left
        (1, 0),  # Vertical down
        (-1, 0), # Vertical up
        (1, 1),  # Diagonal down-right
        (-1, -1),# Diagonal up-left
        (1, -1), # Anti-diagonal down-left
        (-1, 1)  # Anti-diagonal up-right
    ]
    
    # Function to check if a word exists starting at (x, y) in a given direction
    def check_direction(x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx, ny] != word[i]:
                return False
        # Mark the word's location in the marked grid
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            marked[nx, ny] = word[i]
        return True

    # Iterate through every cell in the grid
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if check_direction(x, y, dx, dy):
                    matches += 1

    return matches, marked

# Find all occurrences of the word
total_matches, result_grid = find_word(array, word)

# Print results
print(f"Total occurrences of '{word}': {total_matches}")
# print("\nWord Search with Matches Highlighted:")
# for row in result_grid:
#     print("".join(row))

end_time = time.time()
runtime = (end_time - start_time) * 1_000_000
print(f"Runtime: {runtime:.2f} microseconds")

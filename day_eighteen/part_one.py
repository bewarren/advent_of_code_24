import heapq

with open('input.txt', 'r') as file:
    content = file.read()

coords= list(content.split('\n'))



grid = [["." for i in range(71)] for j in range(71)]



    
def a_star(maze, start, end):
    directions = {
        "N": (0, -1),
        "E": (1, 0),
        "S": (0, 1),
        "W": (-1, 0),
    }
    move_cost = 1

    # Priority queue
    queue = []
    heapq.heappush(queue, (0, start[0], start[1], "E"))  # (cost, x, y, direction)

    visited = set()

    while queue:
        cost, x, y, direction = heapq.heappop(queue)

        # Skip if already visited
        if (x, y, direction) in visited:
            continue
        visited.add((x, y, direction))

        # Check if we've reached the end
        if (x, y) == end:
            return cost

        # Explore moves
        for new_dir, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            # Check bounds and walls
            if 0 <= ny < len(maze) and 0 <= nx < len(maze[0]) and maze[ny][nx] != "#":
                # Moving forward
                new_cost = cost + move_cost
                # Add rotation cost if direction changes
                
                heapq.heappush(queue, (new_cost, nx, ny, new_dir))

    return float('inf')  # No path found


for i, c in enumerate(coords):
    
    x, y = c.split(",")
    grid[int(y)][int(x)] = "#"
    min_cost = a_star(grid, (0,0), (70,70))
    if min_cost == float("inf"):
        print(x, y)
        break



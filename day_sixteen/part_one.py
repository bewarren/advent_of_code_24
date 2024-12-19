import heapq

def parse_maze(input_file):
    with open(input_file, 'r') as f:
        lines = f.read().strip().split("\n")
    maze = [list(line) for line in lines]
    start, end = None, None
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "S":
                start = (x, y)
            elif cell == "E":
                end = (x, y)
    return maze, start, end

def a_star(maze, start, end):
    directions = {
        "N": (0, -1),
        "E": (1, 0),
        "S": (0, 1),
        "W": (-1, 0),
    }
    rotation_cost = 1000
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
                if new_dir != direction:
                    new_cost += rotation_cost
                heapq.heappush(queue, (new_cost, nx, ny, new_dir))

    return float('inf')  # No path found

# Parse input and solve
maze, start, end = parse_maze('input.txt')
min_cost = a_star(maze, start, end)
print(f"Minimum cost: {min_cost}")

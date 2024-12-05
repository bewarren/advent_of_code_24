import time
from collections import defaultdict, deque

# Start the timer
start_time = time.time()

# Read the file into a DataFrame
with open('input.txt', 'r') as file:
    content = file.read()

# Split the input into rules and orders
parts = content.split('\n\n')
part1_lines = parts[0].splitlines()
part2_lines = parts[1].splitlines()

# Parse the rules into a lookup dictionary
look_up_ordering = defaultdict(set)
for rule in part1_lines:
    first, second = map(int, rule.split("|"))
    look_up_ordering[first].add(second)

# Function to reorder using topological sorting
def reorder(order, look_up_ordering):
    order_split = list(map(int, order.split(",")))
    pages_in_update = set(order_split)
    
    # Build graph and in-degrees for this update
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for after, befores in look_up_ordering.items():
        if after in pages_in_update:
            for before in befores:
                if before in pages_in_update:
                    graph[before].append(after)
                    in_degree[after] += 1

    # Find all nodes with in-degree 0
    queue = deque([page for page in order_split if in_degree[page] == 0])

    sorted_update = []
    while queue:
        current = queue.popleft()
        sorted_update.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update

# Function to validate order
def is_ordered(order, look_up_ordering):
    order_split = list(map(int, order.split(",")))
    for i in range(len(order_split) - 1):
        current = order_split[i]
        for next_val in order_split[i + 1:]:
            if next_val in look_up_ordering.get(current, set()):
                continue  # Valid dependency
            else:
                return False
    return True

# Process each order and compute the result
ans = 0
for order in part2_lines:
    if not is_ordered(order, look_up_ordering):
        # Reorder if not valid
        reordered_update = reorder(order, look_up_ordering)
        mid_value = reordered_update[(len(reordered_update) - 1) // 2]
        ans += mid_value

# Output the result
print(ans)

# End the timer
end_time = time.time()
runtime = (end_time - start_time) * 1_000_000
print(f"Runtime: {runtime:.2f} microseconds")

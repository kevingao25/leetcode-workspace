# 841. Keys and Rooms

- **Core Pattern:** DFS, iterative DFS, BFS
- **Tricky Edge Case:** duplicate keys, cycles / self-loops, recursion depth limit, disconnected components.

## Complexity

- **Time:** O(N + E) where N is the number of rooms and E is the number of edges
- **Space:** O(N)

## Iterative DFS Template

```python
def iterative_dfs(start_node):
    visited = set([start_node])
    stack = [start_node]

    while stack:
        node = stack.pop()
        
        # Process the current node here if needed
        
        # Iterate through all adjacent nodes
        for neighbor in get_neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)  # Critical: Mark visited BEFORE appending to stack
                stack.append(neighbor)
```

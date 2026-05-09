# 547. Number of Provinces

- **Core Pattern:** DFS, Union Find
- **Tricky Edge Case:** Fully isolated cities.

## The "Aha!" Moment

Count unvisited nodes that trigger a new DFS.

## Complexity

- **Time:** O(N^2) - Must read N x N matrix.
- **Space:** O(N) - Visited array and DFS call stack.

## Alternative Approaches

BFS, Union Find

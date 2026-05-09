# 1466. Reorder Routes to Make All Paths Lead to the City Zero

- **Core Pattern:** DFS/BFS with specialized adjacency list
- **Tricky Edge Case:** Graph is guaranteed to be a tree, so there's only one unique path per city.

## The "Aha!" Moment

Start at city 0 and traverse outwards. If an original edge points *away* from 0, it costs 1 to reverse.

## Complexity

- **Time:** O(N) - Visit every city and edge exactly once.
- **Space:** O(N) - Adjacency list and DFS call stack size.

## Alternative Approaches

BFS using a Queue.

# 1372. Longest ZigZag Path in a Binary Tree

- **Core Pattern:**: DFS with State Tracking
- **Tricky Edge Case:** single node, single straight line

## The "Aha!" Moment

The key is passing the current state (`direction` and `length`) downwards to the children to make decisions.

If you switch direction, add 1 to length. If you move in the same direction, zigzag break, then start a new zigzag with length of 1.

## Complexity

- **Time:** O(N)
- **Space:** O(H)

## Alternative Approaches

Brute force: Initialize a new count and recalculate zigzag from every single node.

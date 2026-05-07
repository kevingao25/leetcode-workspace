# 437. Path Sum III

- **Core Pattern:** Prefix Sum + DFS + Backtrack
- **Tricky Edge Case:** sub-path, all 0, negative values

## The "Aha!" Moment

A path in a tree is conceptually equivalent to subarray of numbers. We can use prefix sum to solve the problem in O(N). Use a hashmap to keep track of prefix sum, and backtrack when searching other path.

## Complexity

- **Time:** O(N)
- **Space:** O(H)

## Alternative Approaches

Brute force: Double iteration DFS

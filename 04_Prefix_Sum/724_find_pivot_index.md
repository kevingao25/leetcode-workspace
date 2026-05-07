# 724. Find Pivot Index

- **Core Pattern:**: Running prefix sum
- **Tricky Edge Case:** index 0 or last element, negative numbers

## The "Aha!" Moment

No need to calculate the right side from scratch, calculate the total_sum.

## Complexity

- **Time:** O(N)
- **Space:** O(1)

## Alternative Approaches

Brute force: iterate through the array, for every element, run a nested loop to calculate the sum of all elements to its left, and another nested loop to calculate all its right. This is O(N^2) time.

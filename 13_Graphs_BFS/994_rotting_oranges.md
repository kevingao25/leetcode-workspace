# 994. Rotting Oranges

- **Core Pattern:** Grid BFS
- **Tricky Edge Case:** no rotten, only rotten, unreachable fresh oranges

## Complexity

- **Time:** O(m * n)
- **Space:** O(m * n)

## Alternative Approaches

- **In-Place Modification (O(1) Space):** Instead of using a queue, you can continuously scan the grid. Use numbers starting from `2` to represent the minute an orange rots. 
    1. During `minute = 2`, scan the grid. If you see a `2`, turn its fresh neighbors (`1`) into `3`s.
    2. Then increment to `minute = 3` and repeat: find all `3`s and turn their fresh neighbors into `4`s.
    3. Keep repeating this until a full scan results in no new oranges rotting.
    4. Finally, return `minute - 2` (or `-1` if any `1`s are left over). 
    - *Trade-off:* This brings your space complexity down to **O(1)**, but worsens your time complexity to **O(m * n * M)** (where M is the total minutes to rot), because you have to loop over the entire grid for every single minute that passes.

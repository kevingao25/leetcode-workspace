"""
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

m == grid.length

n == grid[i].length

1 <= m, n <= 300

grid[i][j] is '0' or '1'.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if r < 0 or r > len(grid) - 1 or c < 0 or c > len(grid[0]) - 1:
                return
            if grid[r][c] != '1':
                return

            # Mark the land as visited
            grid[r][c] = '#'

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        result = 0

        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if grid[r][c] == '1':
                    result += 1
                    dfs(r, c)
        
        return result

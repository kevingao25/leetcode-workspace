"""
994. Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,

1 representing a fresh orange, or

2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:

m == grid.length

n == grid[i].length

1 <= m, n <= 10

grid[i][j] is 0, 1, or 2.
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        result = 0
        queue = deque()

        # Enqueue all the rotten oranges
        for r, row in enumerate(grid):
            for c, orange in enumerate(row):
                if orange == 2:
                    queue.append((r, c))
        
        # BFS algorithm
        while queue:
            length = len(queue)

            # Enqueue fresh orange neighbour
            for _ in range(length):
                r, c =  queue.popleft()

                if r > 0 and grid[r - 1][c] == 1:
                    queue.append((r - 1, c))
                    grid[r - 1][c] = 2
                if r < len(grid) - 1 and grid[r + 1][c] == 1:
                    queue.append((r + 1, c))
                    grid[r + 1][c] = 2
                if c > 0 and grid[r][c - 1] == 1:
                    queue.append((r, c - 1))
                    grid[r][c - 1] = 2
                if c < len(grid[0]) - 1 and grid[r][c + 1] == 1:
                    queue.append((r, c + 1))
                    grid[r][c + 1] = 2

            if queue:
                result += 1
        
        # Check if there's leftover fresh orange
        for r, row in enumerate(grid):
            for c, orange in enumerate(row):
                if orange == 1:
                    return -1
        
        return result

    def orangesRottingOptimized(self, grid: List[List[int]]) -> int:
        result = 0
        queue = deque()
        fresh_count = 0

        # Enqueue all the rotten oranges and count fresh oranges
        for r, row in enumerate(grid):
            for c, orange in enumerate(row):
                if orange == 2:
                    queue.append((r, c))
                elif orange == 1:
                    fresh_count += 1
        
        # BFS algorithm
        # We can stop early if there are no fresh oranges left
        while queue and fresh_count > 0:
            result += 1
            length = len(queue)

            # Enqueue fresh orange neighbour
            for _ in range(length):
                r, c = queue.popleft()

                # Up, Down, Left, Right
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Check if neighbor is in bounds and is a fresh orange
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
        
        return result if fresh_count == 0 else -1

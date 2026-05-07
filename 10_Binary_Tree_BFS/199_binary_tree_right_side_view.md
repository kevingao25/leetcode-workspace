# 199. Binary Tree Right Side View

- **Core Pattern:** BFS or DFS with depth
- **Tricky Edge Case:** Short right branch and long left branch

## The "Aha!" Moment

We can't only iterate right branch because left branch node can be the right most node in the level. Process level by level, and append the last node in each level to result.

## Complexity

- **Time:** O(N)
- **Space:** O(width)

## Alternative Approaches

**Level-Order Traversal (BFS) Template:**
This is the standard template for processing a tree level-by-level.

```python
from collections import deque

def bfs(root):
    if not root:
        return []

    queue = deque([root])
    
    while queue:
        # 1. Capture how many nodes are in the CURRENT level
        level_length = len(queue)
        
        # 2. Iterate exactly that many times to process just this level
        for _ in range(level_length):
            node = queue.popleft()
            
            # --- Do something with the node here! ---
            
            # 3. Add children to the queue for the NEXT level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
```

"""
199. Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:

Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:

Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []

Constraints:

The number of nodes in the tree is in the range [0, 100].

-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.rightSideViewDFS(root)
        # return self.rightSideViewBFS(root)

    def rightSideViewDFS(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def dfs(node, depth):
            if not node:
                return
            
            # If we visit this depth for the first time, add the node's value
            if depth == len(result):
                result.append(node.val)
            
            # Prioritize the right side!
            dfs(node.right, depth + 1)
            # Only go left to find nodes that might be visible underneath
            dfs(node.left, depth + 1)
            
        dfs(root, 0)
        return result

    def rightSideViewBFS(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        result = []
        queue = deque([root])

        while queue:
            level_length = len(queue)
            
            # Process the nodes level-by-level
            for i in range(level_length):
                node = queue.popleft()
                
                # The last node in the current level is the one visible from the right
                if i == level_length - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
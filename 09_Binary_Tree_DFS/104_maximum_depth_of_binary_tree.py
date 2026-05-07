"""
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

Constraints:

The number of nodes in the tree is in the range [0, 104].

-100 <= Node.val <= 100
"""
from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Time Complexity: O(N) where N is the number of nodes
        # Space Complexity: O(N) worst-case (skewed tree), O(log N) average-case (balanced tree) due to recursion stack
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
    def maxDepth_BFS(self, root: Optional[TreeNode]) -> int:
        # Time Complexity: O(N) where N is the number of nodes
        # Space Complexity: O(N) worst-case (balanced tree), O(1) best-case (skewed tree) due to queue
        if not root:
            return 0
            
        depth = 0
        queue = deque([root])
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
            
        return depth
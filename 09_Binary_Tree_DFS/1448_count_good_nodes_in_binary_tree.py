"""
1448. Count Good Nodes in Binary Tree

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].

Each node's value is between [-10^4, 10^4].
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # max_val keeps track of maximum value down the chain
        def goodNodesHelper(root, max_val):
            if not root:
                return 0
            
            if root.val >= max_val:
                return 1 + goodNodesHelper(root.left, root.val) + goodNodesHelper(root.right, root.val)
            else:
                return goodNodesHelper(root.left, max_val) + goodNodesHelper(root.right, max_val)
        
        return goodNodesHelper(root, float("-inf"))

    def goodNodes_clean(self, root: TreeNode) -> int:
        # A cleaner version using the standard 'dfs' naming convention
        def dfs(node, max_val):
            if not node:
                return 0
            
            # If the node is good, update the max_val for its children
            if node.val >= max_val:
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
            
            # Otherwise, pass the existing max_val down
            return dfs(node.left, max_val) + dfs(node.right, max_val)
            
        return dfs(root, float("-inf"))



# --- TESTS ---
if __name__ == '__main__':
    print('Running tests...')
    # Add your test cases here
    # Example: assert Solution().method_name(args) == expected_output
    print('All tests passed!')

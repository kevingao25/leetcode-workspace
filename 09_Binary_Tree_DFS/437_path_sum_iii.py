"""
437. Path Sum III

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Example 1:

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

Constraints:

The number of nodes in the tree is in the range [0, 1000].

-109 <= Node.val <= 109

-1000 <= targetSum <= 1000
"""

from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # Base case
        
        def dfs(node, current_sum):
            if not node:
                return 0
            current_sum += node.val

            # check prefix sum for running count
            # How many times have we seen the "top part" of the path we need to chop off?
            current_count = prefix_sums.get(current_sum - targetSum, 0)

            # Add current node's sum so our children can use it
            prefix_sums[current_sum] += 1

            # Combine the counts from left and right subtrees
            total_count = current_count + dfs(node.left, current_sum) + dfs(node.right, current_sum)
            
            # BACKTRACK: We are leaving this node and going back up the tree.
            # We MUST remove this sum so parallel branches (like a right sibling) 
            # don't accidentally use a sum from this branch!
            prefix_sums[current_sum] -= 1

            return total_count
        
        return dfs(root, 0)
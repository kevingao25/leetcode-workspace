from typing import Optional
from utils.tree import TreeNode, build_tree, tree_to_list

"""
700. Search in a Binary Search Tree

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

Example 1:

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:

Input: root = [4,2,7,1,3], val = 5
Output: []

Constraints:

The number of nodes in the tree is in the range [1, 5000].

1 <= Node.val <= 107

root is a binary search tree.

1 <= val <= 107
"""

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right, val)
        else:
            return root
      

# --- TESTS ---
if __name__ == '__main__':
    sol = Solution()
    
    print('Running tests...')
    
    # Test Case 1
    root1 = build_tree([4, 2, 7, 1, 3])
    val1 = 2
    res1 = sol.searchBST(root1, val1)
    print(f"Test 1 - Expected: [2, 1, 3], Actual: {tree_to_list(res1)}")
    assert tree_to_list(res1) == [2, 1, 3]
    
    # Test Case 2
    root2 = build_tree([4, 2, 7, 1, 3])
    val2 = 5
    res2 = sol.searchBST(root2, val2)
    print(f"Test 2 - Expected: [], Actual: {tree_to_list(res2)}")
    assert tree_to_list(res2) == []
    
    print('All tests passed!')

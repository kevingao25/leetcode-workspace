# 450. Delete Node in a BST

- **Core Pattern:** BST Deletion (Hibbard Deletion Algorithm)
- **Tricky Edge Case:** delete root node, delete single child node, delete two children node, delete leaf node.

## The "Aha!" Moment

<https://www.youtube.com/watch?v=DkOswl0k7s4&t=185s>

Case by case analysis:

1. leaf node?
2. one child?
3. If two child, instead of tangle with pointers assignments, copy the in-order value (which is a leaf node) over to the delete node, and then delete a leaf node. (And the we can reuse the algorithm to delete the leaf node).

## Complexity

- **Time:** O(H) - where H is the height of the tree.
- Worst case O(N) if skewed
- Best case O(log N) if balanced

- **Space:** O(H) - for the recursive call stack. Same best/worst cases as time complexity.

## Alternative Approaches

- **Iterative Approach:** You can solve this iteratively by manually tracking a `parent` pointer as you traverse down. This brings the space complexity down to O(1) since there is no recursive call stack. However, it requires an immense amount of boilerplate to handle edge cases (e.g., checking if the node is the root, or if it's the left vs. right child of its parent), making it highly error-prone in an interview setting.

```python
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 1. Search for the node and its parent
        parent, node = None, root
        while node and node.val != key:
            parent = node
            if key < node.val:
                node = node.left
            else:
                node = node.right
                
        if not node:
            return root  # Key not found
            
        # 2. Node has two children: swap value with inorder successor
        if node.left and node.right:
            succ_parent, succ = node, node.right
            while succ.left:
                succ_parent = succ
                succ = succ.left
            
            node.val = succ.val
            # Update pointers to delete the successor instead
            node, parent = succ, succ_parent
            
        # 3. Node now has at most 1 child. Get that child (or None)
        child = node.left if node.left else node.right
        
        # 4. Perform the deletion by linking parent to the child
        if not parent:
            return child # We are deleting the root
            
        if parent.left == node:
            parent.left = child
        else:
            parent.right = child
            
        return root
```

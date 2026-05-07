# 236. Lowest Common Ancestor of a Binary Tree

- **Core Pattern:** Post-order DFS (Bottom-Up Traversal)
- **Tricky Edge Case:** When `p` is a direct ancestor of `q` (or vice versa).

## The "Aha!" Moment

Use a post-order traversal to bubble answers back up from the leaves. If a node receives a non-null object from BOTH its left and right children, it means one target is on the left and one is on the right, making it the Lowest Common Ancestor! If it only receives one, it just passes it up.

## Complexity

- **Time:** O(N) - In the worst case, we must visit every node in the tree.
- **Space:** O(H) - The recursive call stack goes as deep as the height of the tree (O(N) for a skewed tree, O(log N) for balanced).

## Alternative Approaches

- **Path Tracking:** We could run two separate DFS traversals to build arrays representing the path from the root to `p` and root to `q`. Then, we compare the two arrays and return the last matching node. This takes more space!
- **Parent Pointers:** If the tree nodes had a `.parent` attribute, we could start at `p`, travel up to the root, and save every node in a Hash Set. Then start at `q` and travel up, returning the first node we find that is in the Hash Set!

## Implementation

```python
def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root
    
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    
    if left and right:
        return root
    return left if left else right
```

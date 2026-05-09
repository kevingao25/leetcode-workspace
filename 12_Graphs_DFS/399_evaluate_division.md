# 399. Evaluate Division

Boring question, don't like it.

- **Core Pattern:** Math trick and DFS
- **Tricky Edge Case:** math

## The "Aha!" Moment

To find a / c, we can chain the fractions (e.g. `(a / b) * (b / c) = a / c`). Then we substitue a / b and b / c and this becomes a graph problem.

Each a -> b has a weight v, and reverse edge b -> a has weight 1 / v

## Complexity

- **Time:** O(Q * (V + E))
- **Space:** O(V + E)

## Alternative Approaches

N/A

# 394. Decode String

- **Core Pattern:** Stack
- **Tricky Edge Case:** Nested encodings like `3[a2[c]]` and multi-digit numbers like `10[a]`.

## The "Aha!" Moment

Instead of trying to find matching brackets recursively, use a stack to save your "previous state" whenever you encounter a `[`. Push the current multiplier and the string built so far onto the stack, then start fresh for the inner content. When you see a `]`, pop the previous state and merge it with the inner content you just built!

## Complexity

- **Time:** O(N) - We iterate through the string once. Note that building the final string length might be longer, but the traversal logic is linear relative to output length.
- **Space:** O(M) - Where M is the number of nested brackets. We only push to the stack when we encounter `[`.

## Alternative Approaches

- **Recursion:** You can solve this recursively by treating each `[` as a recursive call that returns the decoded inner string, but tracking the current index globally or passing it by reference can be slightly messier than the clean iterative stack approach.

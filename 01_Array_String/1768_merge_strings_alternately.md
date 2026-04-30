# 1768. Merge Strings Alternately

- **Core Pattern:** Two Pointers (or Single Pointer with bounds checking)
- **Tricky Edge Case:** Strings of unequal lengths. The tricky part is gracefully handling the "leftover" characters of the longer string without going out of bounds on the shorter string.

## The "Aha!" Moment

You only need to alternate characters up to the length of the *shorter* string. Once you hit the end of the shorter string, you can simply append the entire remainder of the longer string at once (using slicing like `word1[i:]`), because string slices handle out-of-bounds indices gracefully by just returning an empty string.

## Complexity

- **Time:** O(?) - O(N + M)
- **Space:** O(?) - O(N + M)

## Alternative Approaches

N/A

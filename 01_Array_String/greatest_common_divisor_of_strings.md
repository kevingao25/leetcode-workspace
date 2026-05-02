# Greatest Common Divisor of Strings

- **Core Pattern:** String
- **Tricky Edge Case:**  N/A

## The "Aha!" Moment

If str1 + str2 == str2 + str1, then it guarantees a repeating common divisor exists. The length of the longest possible divisor is simply the greatest common divisor

## Complexity

- **Time:** O(N + M)
- **Space:** O(N + M)

## Alternative Approaches

Brute force test all substrings

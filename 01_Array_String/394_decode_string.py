"""
394. Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Constraints:

1 <= s.length <= 30

s consists of lowercase English letters, digits, and square brackets '[]'.

s is guaranteed to be a valid input.

All the integers in s are in the range [1, 300].
"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] # Stores tuples of: (previous_number, previous_string)
        current_num = 0
        current_string = ""
        
        for char in s:
            if char.isdigit():
                # Handle multi-digit numbers (e.g., '1' then '2' becomes 12)
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # 1. Save the state we had *before* this bracket
                stack.append((current_num, current_string))
                # 2. Reset the variables to start building the string *inside* the new brackets
                current_num = 0
                current_string = ""
            elif char == ']':
                # 1. Pop the state that we saved right before the matching '['
                prev_num, prev_string = stack.pop()
                # 2. Multiply the inner string we just built, and append it to the previous string
                current_string = prev_string + (current_string * prev_num)
            else:
                # Normal character, just append it to our current working string
                current_string += char
                
        return current_string

# --- TESTS ---
if __name__ == '__main__':
    print('Running tests...')
    sol = Solution()
    assert sol.decodeString("3[a]2[bc]") == "aaabcbc", "Test 1 failed"
    assert sol.decodeString("3[a2[c]]") == "accaccacc", "Test 2 failed"
    assert sol.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef", "Test 3 failed"
    print('All tests passed!')

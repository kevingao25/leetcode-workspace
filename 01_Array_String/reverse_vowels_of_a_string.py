"""
Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

Constraints:

1 <= s.length <= 3 * 105

s consist of printable ASCII characters.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s_list = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            # Find the next vowel for both left and right pointers
            while left < right and s_list[left] not in vowels:
                left += 1
            while left < right and s_list[right] not in vowels:
                right -= 1
            
            # Swap the vowels
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        
        return "".join(s_list)

    def reverseVowelsStack(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        stack = []
        
        # Pass 1: Collect all vowels in order
        for char in s:
            if char in vowels:
                stack.append(char)
                
        # Pass 2: Pop vowels to naturally reverse them
        result = []
        for char in s:
            if char in vowels:
                result.append(stack.pop())
            else:
                result.append(char)
                
        return "".join(result)


# --- TESTS ---
if __name__ == '__main__':
    print('Running tests...')
    sol = Solution()
    
    test_cases = [
        ("IceCreAm", "AceCreIm"),
        ("leetcode", "leotcede"),
        ("hello", "holle"),
        ("aA", "Aa"),
        ("", ""),
        ("xyz", "xyz")
    ]
    
    for input_str, expected in test_cases:
        assert sol.reverseVowels(input_str) == expected, f"Two Pointer failed on {input_str}"
        assert sol.reverseVowelsStack(input_str) == expected, f"Stack failed on {input_str}"
        
    print('All tests passed!')

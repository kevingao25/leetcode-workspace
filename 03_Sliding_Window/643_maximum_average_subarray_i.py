"""
643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

Input: nums = [5], k = 1
Output: 5.00000

Constraints:

n == nums.length

1 <= k <= n <= 105

-104 <= nums[i] <= 104
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) < k:
            return 0

        maxSum = currSum = sum(nums[:k])
        left, right = 0, k
        
        while right < len(nums):
            currSum = currSum + nums[right] - nums[left]
            right += 1
            left += 1
            maxSum = max(currSum, maxSum)
        
        return maxSum / k


# --- TESTS ---
if __name__ == '__main__':
    print('Running tests...')
    # Add your test cases here
    # Example: assert Solution().method_name(args) == expected_output
    print('All tests passed!')

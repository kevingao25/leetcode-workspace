"""
739. Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:

1 <= temperatures.length <= 105

30 <= temperatures[i] <= 100
"""

class Solution:
    def dailyTemperatures_attempt_1(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # monotonic stack that stores (temperature, index). Note that this stack is strictly decreasing

        for i, temp in enumerate(temperatures):
            # Resolve stack with current temperature
            while stack and temp > stack[-1][0]:
                _, j = stack.pop()
                result[j] = i - j
        
            stack.append((temp, i))

        return result

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # monotonic stack that only stores index

        for i, temp in enumerate(temperatures):
            # Resolve stack with current temperature
            while stack and temp > temperatures[stack[-1]]:
                j = stack.pop()
                result[j] = i - j
        
            stack.append(i)

        return result

                
# --- TESTS ---
if __name__ == '__main__':
    print('Running tests...')
    input = [73,74,75,71,69,72,76,73]
    output = [1,1,4,2,1,1,0,0]
    print(Solution().dailyTemperatures(input))
    assert Solution().dailyTemperatures(input) == output

    input = [72]
    output = [0]
    print(Solution().dailyTemperatures(input))
    assert Solution().dailyTemperatures(input) == output

    input = [50,51,52,53,54]
    output = [1,1,1,1,0]
    print(Solution().dailyTemperatures(input))
    assert Solution().dailyTemperatures(input) == output

    input = [54,53,52,51,10]
    output = [0,0,0,0,0]
    print(Solution().dailyTemperatures(input))
    assert Solution().dailyTemperatures(input) == output

    print('All tests passed!')

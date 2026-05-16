# 334. Increasing Triplet Subsequence

- **Core Pattern:** Greedy / LIS
- **Tricky Edge Case:** identical element, smallest number appears late

## The "Aha!" Moment

The variables `first` and `second` do not need to represent active pair. The variable `second` acts as a historical marker. If `second` has a value, it guarantees theres a smaller number before it, so when any number is larger than `second` we know there's a triplet.

## Complexity

- **Time:** O(N)
- **Space:** O(1)

## Alternative Solution

**Prefix/Suffix Arrays ($O(N)$ Time, $O(N)$ Space)**

Instead of the gatekeeper trick, we can precalculate the minimums from the left and maximums from the right for every index. If a valid triplet exists, then for some middle element `nums[i]`, there must be a smaller number to its left (`min_left[i-1]`) and a larger number to its right (`max_right[i+1]`).

1. Build `min_left` array where `min_left[i]` is the minimum up to index `i`.
2. Build `max_right` array where `max_right[i]` is the maximum from the end down to index `i`.
3. Iterate `1` to `n-2`: If `min_left[i-1] < nums[i] < max_right[i+1]`, return `True`.


## Follow-up / Variations

**Question:** How would you modify the algorithm to actually *return* the triplet, instead of just returning `True`/`False`?

**Solution:**
Because `first` can be overwritten by a smaller number later on (which breaks the physical pairing of your variables), we must "lock in" the first number at the exact moment `second` is assigned. We introduce a `first_for_second` variable to preserve this memory.

```python
class Solution:
    def getIncreasingTriplet(self, nums: List[int]) -> List[int]:
        first = float('inf')
        second = float('inf')
        first_for_second = None  # Locks in 'first' when 'second' is formed
        
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
                # Record what 'first' was at this exact moment
                first_for_second = first
            else:
                # Triplet found!
                return [first_for_second, second, num]
                
        return []
```

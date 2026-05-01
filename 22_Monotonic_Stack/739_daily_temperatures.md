# 739. Daily Temperatures

- **Core Pattern:** monotonic stack
- **Tricky Edge Case:** strictly increasing temperature, strictly decreasing temperature. long plateaus (duplicates), single element

## The "Aha!" Moment

We use a stack as a "waitlist" for past days when they haven't found a warmer day. The reason we use a stack is because a new warmer day will always resolve most recently seen colder days, so the stack will be monotoncially decreasing. That way we don't need to iterate the whole waitlist to resolve all the past colder days, we can keep looking at the most recent cold days since it's guaranteed to be the coldest. If we can't resolve the coldest day, there's definitely no way we can resolve warmer days.

Since we process the days out of order, we need to save the index along the temperature in the stack so we know where to write the answer.

## Complexity

- **Time:** O(N)
- **Space:** O(N)

## Alternative Approaches

Brute force approach: nested loop where for each day, you iterate through all future days one by one until you find a warmer temperature. This is O(N^2) time complexity and will cause TLE.

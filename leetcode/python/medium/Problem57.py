# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(n)
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # O(n)/O(n)
        ans = []
        i, n = 0, len(intervals)

        # Step 1: Add all intervals before `newInterval`
        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        # Step 2: Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        ans.append(newInterval)

        # Step 3: Add remaining intervals
        while i < n:
            ans.append(intervals[i])
            i += 1

        return ans

    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # O(n)/O(n)
        from bisect import bisect_left, bisect_right

        n = len(intervals)
        start, end = newInterval

        # Compare the start of newInterval with the end of existing intervals
        start_idx = bisect_left(intervals, start, key=lambda x: x[1])
        if start_idx < n and intervals[start_idx][0] < start:
            start = intervals[start_idx][0]

        # Compare the end of newInterval with the start of existing intervals
        end_idx = bisect_right(intervals, end, key=lambda x: x[0], lo=start_idx)
        if start_idx < end_idx <= n and intervals[end_idx - 1][1] > end:
            end = intervals[end_idx - 1][1]

        return intervals[:start_idx] + [[start, end]] + intervals[end_idx:]

# Problem 57
# Link: https://leetcode.com/problems/insert-interval/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
    ]
    for intervals, newInterval, expected in cases:
        assert s.insert(intervals, newInterval) == expected


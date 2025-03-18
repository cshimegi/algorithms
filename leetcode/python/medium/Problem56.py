# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(n)
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l = len(intervals)
        if l == 1:
            return intervals

        intervals.sort(key=lambda i: i[0])
        i, i_ans, ans = 0, 0, [intervals[0]]
        while i < l - 1:
            start1, end1 = ans[i_ans]
            start2, end2 = intervals[i+1]

            if start1 <= start2 <= end1 <= end2: # Case like [[1,5], [2,8]]
                ans[i_ans] = [start1, end2]
            elif start1 <= start2 and end1 >= end2: # Case like [[1,5], [1,4]]
                ans[i_ans] = [start1, end1]
            elif start2 > end1: # Other cases
                ans.append([start2, end2])
                i_ans += 1
            i += 1
        return ans

    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        # Sort intervals by their start time
        intervals.sort(key=lambda x: x[0])

        ans = []
        for start, end in intervals:
            # If the merged list is empty or the current interval does not overlap
            # with the last one, append it
            if not ans or ans[-1][1] < start:
                ans.append([start, end])
            else:
                # Overlapping intervals, merge them
                ans[-1][1] = max(ans[-1][1], end)

        return ans

# Problem 56
# Link: https://leetcode.com/problems/merge-intervals/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
    ]
    for intervals, expected in cases:
        assert s.merge(intervals) == expected

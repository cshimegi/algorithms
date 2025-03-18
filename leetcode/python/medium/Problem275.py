# Questions to ask:
# 1. What is the time complexity? O(log n)
# 2. What is the space complexity?
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        total = len(citations)
        l, r = 0, total - 1
        while l <= r:
            mid = (l+r)//2
            if citations[mid] < total - mid:
                l = mid+1
            else:
                r = mid-1
        return total - l

# Problem 275
# Link: https://leetcode.com/problems/h-index-ii/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([0, 1, 3, 5, 6], 3),
        ([1, 2, 100], 2),
        ([1], 1),
    ]
    for citations, expected in cases:
        assert s.hIndex(citations) == expected

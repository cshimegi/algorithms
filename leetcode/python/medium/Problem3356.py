# Questions to ask:
# 1. What is the time complexity? O(n*log(m))
# 2. What is the space complexity? O(n)
from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        def check(m: int) -> bool:
            diff = [0] * (n + 1)
            for i in range(m):
                start, end, val = queries[i]
                diff[start] += val
                diff[end+1] -= val
            cur = 0
            for i in range(n):
                cur += diff[i]
                if cur < nums[i]: return False
            return True

        l_q = len(queries)
        if not check(l_q): return -1

        l, r = 0, l_q
        while l <= r:
            m = (r+l) // 2
            if check(m):
                r = m - 1
            else:
                l = m + 1
        return l

# Problem 3356
# Link: https://leetcode.com/problems/zero-array-transformation-ii/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([2, 0, 2], [[0, 2, 1], [0, 2, 1], [1, 1, 3]], 2),
        ([4, 3, 2, 1], [[1, 3, 2], [0, 2, 1]], -1),
        ([5], [[0, 0, 5], [0, 0, 1], [0, 0, 3], [0, 0, 2]], 1),
    ]
    for nums, queries, expected in cases:
        assert s.minZeroArray(nums, queries) == expected

# Questions to ask:
# 1. What is the time complexity? O(n^2)
# 2. What is the space complexity? O(n^2)
from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {num: i for i, num in enumerate(arr)}
        n = len(arr)
        ans = 0
        dp = {}

        for i in range(n):
            for j in range(i+1, n):
                x, y = arr[i], arr[j]
                z = x + y
                if z in index:
                    k = index[z]
                    dp[(j, k)] = dp.get((i, j), 2) + 1
                    ans = max(ans, dp[(j, k)])

        return ans if ans >= 3 else 0

# Problem 873
# Link: https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([1,3,7,11,12,14,18], 3),
        ([1,2,3,4,5,6,7,8], 5),
        ([1,3,5], 0)
    ]
    for case, expected in cases:
        assert s.lenLongestFibSubseq(case) == expected


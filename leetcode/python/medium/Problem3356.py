# Questions to ask:
# 1. What is the time complexity? O(n*log(m))
# 2. What is the space complexity? O(n)

# PROBLEM: Zero Array Transformation II
# 
# Given array nums and queries [start, end, val], find minimum number of queries
# needed to make all elements >= nums[i] by adding val to range [start, end].
#
# Key technique: Difference Array for efficient range updates
#
# EXAMPLE: nums=[2,0,2], queries=[[0,2,1], [0,2,1], [1,1,3]]
# 
# Difference Array Technique:
# - Instead of updating each element in range, use difference array
# - diff[start] += val, diff[end+1] -= val
# - Then convert to actual values by cumulative sum
#
# STEP-BY-STEP EXAMPLE (check(2) - using first 2 queries):
# 
# Initial: diff = [0, 0, 0, 0]  (size n+1 = 4)
# 
# Query 1: [0,2,1] - add 1 to range [0,2]
# diff[0] += 1 → diff = [1, 0, 0, 0]
# diff[3] -= 1 → diff = [1, 0, 0, -1]
# 
# Query 2: [0,2,1] - add 1 to range [0,2]  
# diff[0] += 1 → diff = [2, 0, 0, -1]
# diff[3] -= 1 → diff = [2, 0, 0, -2]
# 
# Convert to actual values:
# pos 0: cur = 0 + 2 = 2, need 2 ✓
# pos 1: cur = 2 + 0 = 2, need 0 ✓  
# pos 2: cur = 2 + 0 = 2, need 2 ✓
# All satisfied → return True
from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        def check(m: int) -> bool:
            # Check if applying first m queries can make all elements >= nums[i]
            # Uses difference array technique for efficient range updates
            
            # Initialize difference array (size n+1 for range [0, n-1])
            diff = [0] * (n + 1)
            
            # Apply first m queries using difference array technique
            for i in range(m):
                start, end, val = queries[i]
                diff[start] += val      # Start of range: add val
                diff[end+1] -= val      # End of range+1: subtract val
            
            # Convert difference array to actual values
            cur = 0  # Current cumulative value
            for i in range(n):
                cur += diff[i]  # Apply difference to get actual value at position i
                if cur < nums[i]: 
                    return False  # Can't satisfy requirement at position i
            return True  # All positions can be satisfied

        l_q = len(queries)
        if not check(l_q): return -1

        l, r = 0, l_q
        while l < r:
            m = (r+l) // 2
            if check(m):
                r = m
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

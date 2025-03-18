# Questions to ask:
# 1. What is the time complexity? O(2^n)
# 2. What is the space complexity? O(2^n)
from typing import List

class Solution:
    def backtrack(self, nums: List[int], start: int, subset: List[int], ans: List[List[int]]):
        # Append the copied current subset
        ans.append(subset[:])

        for i in range(start, len(nums)):
            # Include nums[i] in the current subset
            subset.append(nums[i])
            # Recur with the next index
            self.backtrack(nums, i + 1, subset, ans)
            # Backtrack by removing the last element
            subset.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backtrack(nums, 0, [], ans)
        return ans

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        l = len(nums)

        def dfs(i):
            if i >= l:
                ans.append(subset[:])
                return
            # Add this number
            subset.append(nums[i])
            dfs(i+1)
            # Don't add this number
            subset.pop()
            dfs(i+1)

        dfs(0)
        return ans


# Problem 78
# Link: https://leetcode.com/problems/subsets/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([1,2,3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
    ]
    for nums, expected in cases:
        assert s.subsets(nums) == expected
        assert s.subsets2(nums) == expected

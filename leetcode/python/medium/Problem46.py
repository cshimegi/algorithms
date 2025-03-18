# Questions to ask:
# 1. What is the time complexity? O(n!)
# 2. What is the space complexity? O(n!)
from typing import List

class Solution:
    def backtrack(self, nums: List[int], path: List[int], res: List[List[int]]):
        if not nums:
            res.append(path)
            return

        for i in range(len(nums)):
            self.backtrack(nums[:i] + nums[i+1:], path + [nums[i]], res)

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backtrack(nums, [], ans)
        return ans


# Problem 46
# Link: https://leetcode.com/problems/permutations/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
    ]
    for nums, expected in cases:
        assert s.permute(nums) == expected

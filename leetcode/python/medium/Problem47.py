# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # O(n*n!)/O(n*n!)
        ans = []

        def backtrack(sub_nums: List[int], path: List[List[int]]):
            if not sub_nums:
                ans.append(path)
                return

            for i in range(len(sub_nums)):
                # Avoid duplicate
                if i > 0 and sub_nums[i] == sub_nums[i - 1]:
                    continue
                backtrack(sub_nums[:i] + sub_nums[i + 1:], path + [sub_nums[i]])

        nums.sort()
        backtrack(nums, [])

        return ans

    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        # O(n!)/O(n!)
        nums.sort()
        ans = []
        l = len(nums)
        used = [False] * l

        def backtrack(path: List[int]):
            if l == len(path):
                ans.append(path[:])
                return

            for i in range(l):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return ans


# Problem 47
# Link: https://leetcode.com/problems/permutations-ii/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        [1, 1, 2],
        [1, 2, 3],
        [3, 3, 0, 3],
    ]
    for case in cases:
        print(s.permuteUnique(case))


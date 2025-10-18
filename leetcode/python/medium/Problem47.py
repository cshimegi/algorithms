# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
from typing import List
from collections import Counter

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
                # Avoid duplicate
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return ans

    def permuteUnique3(self, nums: List[int]) -> List[List[int]]:
        # O(n!)/O(n!) - Most intuitive and efficient for many duplicates
        # Uses Counter to track available numbers - no complex used[] logic needed
        ans = []
        counter = Counter(nums)
        l = len(nums)

        def backtrack(path: List[int]):
            if len(path) == l:
                ans.append(path[:])
                return

            # Only iterate through unique values, not all indices!
            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    path.append(num)
                    backtrack(path)
                    path.pop()
                    counter[num] += 1

        backtrack([])
        return ans


# Problem 47
# Link: https://leetcode.com/problems/permutations-ii/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ([3, 3, 0, 3], [[0, 3, 3, 3], [3, 0, 3, 3], [3, 3, 0, 3], [3, 3, 3, 0]]),
    ]
    for nums, expected in cases:
        assert s.permuteUnique(nums) == expected
        assert s.permuteUnique2(nums) == expected
        assert s.permuteUnique3(nums) == expected

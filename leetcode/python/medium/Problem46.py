# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def backtrack(self, nums: list[int], path: list[int], res: list[list[int]]):
        if not nums:
            res.append(path)
            return

        for i in range(len(nums)):
            self.backtrack(nums[:i] + nums[i+1:], path + [nums[i]], res)

    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        self.backtrack(nums, [], ans)
        return ans


# Problem 46
# Link: https://leetcode.com/problems/permutations/description/
if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))

# Questions to ask:
# 1. What is the time complexity? O(n * 2^n)
# 2. What is the space complexity?
class Solution:
    def backtrack(self, nums: list[int], start: int, subset: list[int], ans: list[list[int]]):
        # Append the current subset
        ans.append(subset[:])  # Use subset[:] to create a copy of the current subset

        for i in range(start, len(nums)):
            # Include nums[i] in the current subset
            subset.append(nums[i])
            # Recur with the next index
            self.backtrack(nums, i + 1, subset, ans)
            # Backtrack by removing the last element
            subset.pop()

    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        self.backtrack(nums, 0, [], ans)
        return ans


    def subsets2(self, nums: list[int]) -> list[list[int]]:
        ans = []
        subset = []
        l = len(nums)

        def dfs(i):
            if i >= l:
                ans.append(subset[:])
                return

            # Add next number
            subset.append(nums[i])
            dfs(i+1)

            # Don't add next number
            subset.pop()
            dfs(i+1)

        dfs(0)
        return ans


# Problem 78
# Link: https://leetcode.com/problems/subsets/description/
if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1,2,3]))

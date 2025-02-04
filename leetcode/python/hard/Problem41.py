# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(1)
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        l = len(nums)

        for i in range(l):
            # Swap to place the number in correct position
            # https://stackoverflow.com/questions/72555438/python-swapping-values-gives-different-results-on-changing-order-of-swap
            while 1 <= nums[i] <= l and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        for i in range(l):
            if i+1 != nums[i]:
                return i+1

        return l+1

# Problem 41
# Link: https://leetcode.com/problems/first-missing-positive/description/
if __name__ == '__main__':
    s = Solution()


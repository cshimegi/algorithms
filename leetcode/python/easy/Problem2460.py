# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(1)
class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        # Move zeros to the end by swapping
        k = 0
        for j in range(n):
            if nums[j] != 0:
                nums[k], nums[j] = nums[j], nums[k]
                k += 1

        return nums


# Problem 2460
# Tips:
# Link: https://leetcode.com/problems/apply-operations-to-an-array/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        [1,2,2,1,1,3],
        [0,1],
        [2,2,2,2,2]
    ]

    for case in cases:
        print(s.applyOperations(case))


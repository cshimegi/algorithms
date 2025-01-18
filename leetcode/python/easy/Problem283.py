# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
# 3. Requirements:
#   - Could you minimize the total number of operations done?
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0 and nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]

            # Go to next zero
            while i < j and nums[i] != 0:
                i += 1


# Problem 283
# Tips:
# Link: https://leetcode.com/problems/move-zeroes/description/
if __name__ == '__main__':
    s = Solution()
    num1 = [0,1,0,3,12,0]
    s.moveZeroes(num1)
    print(num1)

    num2 = [0]
    s.moveZeroes(num2)
    print(num2)

    num3 = [1,0,0,4,5,0,7,8,0,9]
    s.moveZeroes(num3)
    print(num3)

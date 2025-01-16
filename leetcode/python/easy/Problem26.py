# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        while j < len(nums):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
            j += 1
        return i + 1


# Problem 26
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates(nums = [1,1,2]))
    print(s.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))

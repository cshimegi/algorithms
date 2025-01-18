# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
# 3. Is it guaranteed that the elements start from 1 to n?
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        freq = {}
        for n in nums:
            if not freq.get(n, False):
                freq.update({n: True})
                continue
            return True
        return False

# Problem 217
# Tips:
# Link: https://leetcode.com/problems/contains-duplicate/description/
if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate(nums = [1,2,3,1]))
    print(s.containsDuplicate(nums = [1,2,3,4]))
    print(s.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]))
    print(s.containsDuplicate(nums = [1,2,3,5]))


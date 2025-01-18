# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            ans ^= n
        return ans


# Problem 136
# Tips:
# 1.
# Link: https://leetcode.com/problems/single-number/description/
if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber(nums = [4,1,2,1,2]))

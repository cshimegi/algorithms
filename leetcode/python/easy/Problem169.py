# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(1)
# 3. The majority element is the element that appears more than ⌊n / 2⌋ times -> must be odd
# 4. How the numbers are distributed?
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Boyer-Moore Voting Algorithm
        count, majority = 1, nums[0]
        for n in nums[1:]:
            if count == 0:
                majority = n
            count += 1 if n == majority else -1
        return majority


# Problem 169
# Tips:
# 1.
# Link: https://leetcode.com/problems/majority-element/description/
if __name__ == '__main__':
    s = Solution()


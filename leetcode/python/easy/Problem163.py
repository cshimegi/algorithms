# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity?
class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        ans = []

        for num in nums:
            if num == lower:
                lower += 1
            elif num > lower:
                ans.append([lower, num-1])
                lower = num + 1
        # Add the last range
        if lower <= upper:
            ans.append([lower, upper])

        return ans


# Problem 163
# Tips:
# Link: https://leetcode.com/problems/missing-ranges/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([0,1,3,50,75], 0, 99),
        ([], 0, 100),
        ([0,1,3,99,100], 0, 100),
    ]
    for nums, lower, upper in cases:
        print(s.findMissingRanges(nums, lower, upper))


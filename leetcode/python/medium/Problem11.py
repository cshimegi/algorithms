# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(1)
class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r, ans = 0, len(height)-1, 0
        while l < r:
            ans = max(ans, (r-l)*min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans


# Problem 11
# Link: https://leetcode.com/problems/container-with-most-water/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([1,8,6,2,5,4,8,3,7], 49)
    ]
    for height, expected in cases:
        print(s.maxArea(height) == expected)

# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def trap(self, height: list[int]) -> int:
        l = len(height)
        if l == 0:
            return 0

        left, right = 0, l-1
        maxLeft, maxRight = 0, 0
        trappedWater = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= maxLeft:
                    maxLeft = height[left]
                else:
                    trappedWater += maxLeft - height[left]
                left += 1
            else:
                if height[right] >= maxRight:
                    maxRight = height[right]
                else:
                    trappedWater += maxRight - height[right]
                right -= 1

        return trappedWater

# Problem 42
# Link: https://leetcode.com/problems/trapping-rain-water/description/
if __name__ == '__main__':
    s = Solution()


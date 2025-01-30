# Questions to ask:
# 1. What is the time complexity? O(n * log(n))
# 2. What is the space complexity?
import bisect

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        sub = []  # Stores the smallest increasing subsequence

        for num in nums:
            idx = bisect.bisect_left(sub, num)  # Find insertion position
            if idx == len(sub):
                sub.append(num)  # Append if num is greater than all elements
            else:
                sub[idx] = num  # Replace to maintain the smallest increasing sequence

        return len(sub)

    def lengthOfLIS2(self, nums: list[int]) -> int:
        def binary_search(sub, num):
            left, right = 0, len(sub) - 1
            while left <= right: # need to take index=0 into account
                mid = (left + right) // 2
                if sub[mid] >= num:
                    right = mid - 1  # Move left if `num` is smaller
                else:
                    left = mid + 1  # Move right if `num` is greater
            return left  # The correct insertion position

        sub = []
        for num in nums:
            idx = binary_search(sub, num)
            if idx == len(sub):
                sub.append(num)  # Append if `num` extends LIS
            else:
                sub[idx] = num  # Replace to keep LIS minimal

        return len(sub)

    def lengthOfLIS3(self, nums: list[int]) -> int:
        # O(n^2)
        n = len(nums)
        dp = [1] * n  # Each element starts with LIS of length 1

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:  # Check increasing order
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)



# Problem 300
# Link: https://leetcode.com/problems/longest-increasing-subsequence/description/
# Tips:
if __name__ == '__main__':
    s = Solution()



# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def backtrack(self, nums: list[int], start: int, memo: dict):
        if start >= len(nums):
            return 0

        if start in memo:
            return memo[start]

        rob_this = nums[start] + self.backtrack(nums, start + 2, memo)
        skip_this = self.backtrack(nums, start+1, memo)


        memo[start] = max(rob_this, skip_this)
        return memo[start]

    def rob(self, nums: list[int]) -> int:
        return self.backtrack(nums, 0, {})

    def rob2(self, nums: list[int]) -> int:
        # DP
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        prev_rob, prev_skip = 0, 0
        for n in nums:
            curr = max(prev_skip + n, prev_rob)
            prev_skip = prev_rob
            prev_rob = curr

        return prev_rob

    def rob3(self, nums: list[int]) -> (int, list[int]):
        # Return robbed max profit and houses
        if not nums:
            return 0, []

        l = len(nums)
        if l == 1:
            return nums[0], [0]

        dp = [0]*l
        prev_selected = [-1]*l

        dp[0] = nums[0]
        prev_selected[0] = 0
        if nums[0] >= nums[1]:
            dp[1] = nums[0]
            prev_selected[1] = 0
        else:
            dp[1] = nums[1]
            prev_selected[1] = 1

        for i in range(2, l):
            if dp[i-1] > dp[i-2] + nums[i]:
                dp[i] = dp[i-1]
                prev_selected[i] = prev_selected[i-1]
            else:
                dp[i] = dp[i-2] + nums[i]
                prev_selected[i] = i

        robbed_houses = []
        i = l-1
        while i >= 0:
            if prev_selected[i] == i:
                robbed_houses.append(i)
                i -= 2
            else:
                i -= 1

        return dp[-1], robbed_houses[::-1]

# Problem 198
# Link: https://leetcode.com/problems/house-robber/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    max_profit, robbed_houses = s.rob3([7,6,8,20,1])
    print(max_profit)
    print(robbed_houses)


    max_profit2, robbed_houses2 = s.rob3([2,7,9,3,1])
    print(max_profit2)
    print(robbed_houses2)



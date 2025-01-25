# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        i, j, max_profit = 0, 1, 0
        while j < len(prices):
            # Buy at low price and sell at higher
            if prices[i] < prices[j]:
                max_profit += prices[j] - prices[i]
                i = j
            else:
                i += 1

            j += 1
        return max_profit

    def maxProfit2(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit


# Problem 122
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
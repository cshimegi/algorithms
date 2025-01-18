# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        i, j, max_profit = 0, 1, 0
        while j < len(prices):
            if prices[i] < prices[j]:
                max_profit = max(max_profit, prices[j] - prices[i])
            else:
                i = j
            j += 1
        return max_profit



# Problem 121
# Tips:
# 1.
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit(prices = [7,1,5,3,6,4]))
    print(s.maxProfit(prices = [7,1,5,3,6,4,10]))
    print(s.maxProfit(prices = [7,4,5,3,6,4,10]))

# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Change the question to the climbing stairs one
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed for amount 0

        for coin in coins:
            for i in range(coin, amount + 1):
                # Compare exchanging this coin or not min(not do, do)
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1


# Problem 322
# Link: https://leetcode.com/problems/coin-change/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([186,419,83,408],6249))


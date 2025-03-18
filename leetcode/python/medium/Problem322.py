# Questions to ask:
# 1. What is the time complexity? O(n*m)
# 2. What is the space complexity? O(m)
# Return the fewest number of coins that you need to make up that amount
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Change the question to the climbing stairs one
        dp = [float('inf')] * (amount + 1) # DP table for the number of coins to make up the amount
        dp[0] = 0  # Base case: 0 coins needed for amount 0

        for coin in coins:
            for i in range(coin, amount + 1):
                # Compare exchanging this coin or not min(not do, do)
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

    def coinChange2(self, coins: List[int], amount: int):
        # Return used coins and their counts
        # Initialize DP table
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # 0 coins needed for amount 0

        # To track which coin was used for each amount
        coin_used = [-1] * (amount + 1)
        for coin in coins:
            for i in range(coin, amount + 1):
                if dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    coin_used[i] = coin

                    # If no valid combination found, return -1
        if dp[amount] == float('inf'):
            return -1

        # Step 3: Backtrack to find coin counts
        coin_counts = {c: 0 for c in coins}
        remaining_amount = amount
        while remaining_amount > 0:
            coin = coin_used[remaining_amount]
            if coin == -1:
                return -1  # Should not happen, but extra safety
            coin_counts[coin] += 1
            remaining_amount -= coin

        return coin_counts


# Problem 322
# Link: https://leetcode.com/problems/coin-change/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([186,419,83,408], 6249, 20),
    ]
    for coins, amount, expected in cases:
        assert s.coinChange2(coins, amount) == expected

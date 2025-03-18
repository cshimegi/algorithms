# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
# Return the number of combinations that make up that amount
# Different from 322
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # O(2^n)/O(1)
        if amount == 0:
            return 1

        ans = [0]

        def backtrack(start: int, remaining: int):
            # Keep finding posible combination
            for idx, c in enumerate(coins[start:]):
                r = remaining - c

                if r == 0:
                    ans[0] += 1
                    return
                # When coin can't be changed
                if r < coins[start]:
                    return

                backtrack(idx, r)

        backtrack(0, amount)
        return ans[0]

    """
    coins = [2,1,5]
    amount=5, coin=2 => dp[2] = dp[2]+dp[0]=0+1=1
                        dp[3] = dp[3]+dp[1]=0+0=0
                        dp[4] = dp[4]+dp[2]=0+1=1
                        dp[5] = dp[5]+dp[3]=0+0=0
    amount=5, coin=1 => dp[1] = dp[1]+dp[0]=0+1=1
                        dp[2] = dp[2]+dp[1]=1+1=2
                        dp[3] = dp[3]+dp[2]=0+2=2
                        dp[4] = dp[4]+dp[3]=1+2=3
                        dp[5] = dp[5]+dp[4]=0+3=3
    amount=5, coin=5 => dp[5] = dp[5]+dp[0]=3+1=4
    
    [1,1,1,1,1]
    [1,1,1,2]
    [1,2,2]
    [5]
    """
    def change2(self, amount: int, coins: List[int]) -> int:
        # O(n^2)/O(n)
        dp = [0] * (amount + 1) # DP table for the number of ways to make up each amount
        dp[0] = 1 # Base case: amount 0 is also 1 way

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]

    def change3(self, amount: int, coins: List[int]) -> int:
        # O(n*amount)/O(amount)
        l = len(coins)
        memo = {}

        def dfs(i, remaining):
            if remaining == 0: return 1
            if remaining < 0 or i == l: return 0
            if (i, remaining) in memo:
                return memo[(i, remaining)]

            memo[(i, remaining)] = dfs(i, remaining - coins[i]) + dfs(i + 1, remaining)
            return memo[(i, remaining)]

        return dfs(0, amount)


# Problem 518
# Link: https://leetcode.com/problems/coin-change-ii/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        (5, [1, 2, 5], 4),
        (3, [2], 0),
        (10, [10], 1),
    ]
    for amount, coins, expected in cases:
        assert s.change(amount, coins) == expected

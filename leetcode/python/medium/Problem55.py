# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def backtrack(self, nums: list[int], curr: int, last: int):
        # O(2^n) ---> time limit exceeded
        if curr == last:
            return True

        isOk = False
        if curr < last:
            for step in range(1, nums[curr]+1):
                isOk |= self.backtrack(nums, curr+step, last)

        return isOk


    def canJump(self, nums: list[int]) -> bool:
        # Greedy algorithm: Only need to check how far we can reach when standing at the current index

        l, farthest = len(nums), 0
        for i in range(l):
            # If the current index is not reachable, return False
            if i > farthest:
                return False
            # Update the farthest point reachable from index `i`
            farthest = max(farthest, i + nums[i])
            # If the farthest point is past the last index, return True
            if farthest >= l - 1:
                return True
        return False



# Problem 55
# Link: https://leetcode.com/problems/jump-game/description/
if __name__ == '__main__':
    s = Solution()

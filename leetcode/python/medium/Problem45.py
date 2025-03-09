# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(1)
class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0  # Already at last index, no jumps needed

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):  # No need to check last index
            farthest = max(farthest, i + nums[i])  # Max reach from index i

            if i == current_end:  # Need to make a jump
                jumps += 1
                current_end = farthest  # Update new range

                if current_end >= n - 1:  # If we can reach or pass the last index
                    break

        return jumps


# Problem 45
# Link: https://leetcode.com/problems/jump-game-ii/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        [2,3,1,1,4],
        [2,3,0,1,4]
    ]

    for case in cases:
        print(s.pivotArray(case[0], case[1]))
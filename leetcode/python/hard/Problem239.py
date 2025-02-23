# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity?
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        from collections import deque

        idx_dq = deque()
        ans = []
        for i, num in enumerate(nums):
            # Remove elements outside the current window
            if idx_dq and idx_dq[0] < i - k + 1:
                idx_dq.popleft()

            # Remove elements smaller than the current element
            # to keep the index of max number in the current window at the front
            while idx_dq and nums[idx_dq[-1]] < num:
                idx_dq.pop()

            idx_dq.append(i)

            if i >= k-1:
                ans.append(nums[idx_dq[0]])

        return ans


# Problem 239
# Link: https://leetcode.com/problems/sliding-window-maximum/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        [[1,3,-1,-3,5,3,6,7], 3],
        [[1,3,1,2,0,5], 3],
        [[1,-1], 1]
    ]
    for nums, k in cases:
        print(s.maxSlidingWindow(nums, k))


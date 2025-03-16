# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # O(n)/O(1)
        l, r = 0, 0
        total = 0
        min_len = float('inf')
        while r < len(nums):
            total += nums[r]
            while total >= target:
                min_len = min(min_len, r-l+1)
                total -= nums[l]
                l += 1
            r += 1
        return min_len if min_len != float('inf') else 0

    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
        # O(n*log(n))/O(1)
        total = len(nums)
        def check(length: int) -> bool:
            current_sum = sum(nums[:length])
            if current_sum >= target:
                return True

            for i in range(length, total):
                current_sum += nums[i] - nums[i-length]
                if current_sum >= target:
                    return True
            return False

        l, r = 1, total # l and r mean possible lengths of subarray
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1

        if not check(l):
            return 0
        else:
            return l


# Problem 209
# Link: https://leetcode.com/problems/minimum-size-subarray-sum/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    cases = [
        (7, [2, 3, 1, 2, 4, 3]),
        (4, [1, 4, 4]),
        (11, [1, 1, 1, 1, 1, 1, 1, 1])
    ]
    for target, nums in cases:
        print(s.minSubArrayLen(target, nums))


# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(1) except for output array
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total, num_zero = 1, 0
        for n in nums:
            if n != 0:
                total *= n
            else:
                num_zero += 1

        ans = []
        for n in nums:
            if n == 0:
                if num_zero > 1:
                    ans.append(0)
                else:
                    ans.append(total)
            else:
                if num_zero > 0:
                    ans.append(0)
                else:
                    ans.append(int(total/n))
        return ans

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [1] * l

        # Compute prefix (left -> right)
        prefix = 1
        for i in range(l):
            ans[i] = prefix
            prefix *= nums[i]

        # Compute suffix (right -> left)
        suffix = 1
        for i in range(l-1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans

# Problem 238
# Link: https://leetcode.com/problems/product-of-array-except-self/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([1,2,3,4], [24,12,8,6]),
        ([-1,1,0,-3,3], [0,0,9,0,0]),
    ]
    for nums, expected in cases:
        assert s.productExceptSelf(nums) == expected
        assert s.productExceptSelf2(nums) == expected

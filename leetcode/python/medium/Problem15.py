# Questions to ask:
# 1. What is the time complexity? O(n^2)
# 2. What is the space complexity?
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        l = len(nums)
        for i in range(l):
            if nums[i] > 0:
                break

            # avoid duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j, k = i+1, l-1
            while j < k:
                res = nums[i] + nums[j] + nums[k]
                if res > 0:
                    k -= 1
                elif res < 0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1

                    # avoid duplicate
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
        return ans


# Problem 15
# Link: https://leetcode.com/problems/3sum/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([-1,0,1,2,-1,-4], [[-1,-1,2], [-1,0,1]]),
    ]
    for nums, expected in cases:
        assert s.threeSum(nums) == expected

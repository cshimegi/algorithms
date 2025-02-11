# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # Count nums[i] - i because nums[i] - i != nums[j] - j
        hm = {}
        for i, n in enumerate(nums):
            hm[i-n] = hm.get(i-n, 0) + 1
        # Count the number of good pairs
        count = 0
        for c in hm.values():
            count += c*(c-1)//2
        # The number of bad pairs = total pairs - good pairs
        l_nums = len(nums)
        return l_nums*(l_nums-1)//2 - count


# Problem 2364
# Link: https://leetcode.com/problems/count-number-of-bad-pairs/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    print(s.countBadPairs([4,1,3,3]))


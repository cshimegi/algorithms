# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(n)
class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        from collections import Counter

        cnt = Counter(nums)
        ans = 0

        for num in nums:
            if num - k in cnt:
                ans += cnt[num - k]
            if num + k in cnt:
                ans += cnt[num + k]

        return ans // 2


# Problem 2006
# Tips:
# Link: https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description/
if __name__ == '__main__':
    s = Solution()



class Solution:
    # Questions to ask:
    # 1. What is the time complexity? O(n^2)
    # 2. What is the space complexity? O(n^2)
    # 3. Are (-1,1,1,-1) and (1,1,-1,-1) same?
    from typing import List
    
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        l = len(nums1)

        remaining1 = {}
        for i in range(l):
            for j in range(l):
                r = 0 - nums1[i] - nums2[j]
                c = remaining1.get(r, 0) + 1
                remaining1.update({r: c})

        ans = 0
        for k in range(l):
            for m in range(l):
                target = nums3[k] + nums4[m]
                ans += remaining1.get(target, 0)
        return ans

    def fourSumCount2(nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        from collections import Counter
        countAB = Counter(a + b for a in nums1 for b in nums2)  # Count all sums from nums1 & nums2

        return sum(countAB[-(c + d)] for c in nums3 for d in nums4)


# Problem 454
# Link: https://leetcode.com/problems/4sum-ii/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([1,2], [-2,-1], [-1,2], [0,2], 2),
        ([-1,-1], [-1,1], [-1,1], [1,-1], 6),
    ]
    for nums1, nums2, nums3, nums4, expected in cases:
        assert s.fourSumCount(nums1, nums2, nums3, nums4) == expected

class Solution:
    # Questions to ask:
    # 1. What is the time complexity?
    # 2. What is the space complexity?
    # 3. Are (-1,1,1,-1) and (1,1,-1,-1) same?
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
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

# Problem 454
# Link: https://leetcode.com/problems/4sum-ii/description/
if __name__ == '__main__':
    s = Solution()
    print(s.fourSumCount(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]))
    print(s.fourSumCount(nums1 = [-1,-1], nums2 = [-1,1], nums3 = [-1,1], nums4 = [1,-1]))


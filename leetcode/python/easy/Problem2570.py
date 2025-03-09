# Questions to ask:
# 1. What is the time complexity? O(n+m)
# 2. What is the space complexity? O(n+m)
class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        n, m = len(nums1), len(nums2)
        nn, mm = 0, 0
        ans = []
        while nn < n and mm < m:
            temp = None
            if nums1[nn][0] < nums2[mm][0]:
                temp = nums1[nn]
                nn += 1
            elif nums1[nn][0] > nums2[mm][0]:
                temp = nums2[mm]
                mm += 1
            else:
                temp = [nums1[nn][0], nums1[nn][1] + nums2[mm][1]]
                mm += 1
                nn += 1
            ans.append(temp)

        if nn < n:
            ans.extend(nums1[nn:])
        if mm < m:
            ans.extend(nums2[mm:])

        return ans


# Problem 2460
# Tips:
# Link: https://leetcode.com/problems/apply-operations-to-an-array/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        [[[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]],
        [[[2,4],[3,6]], [[1,3],[2,3]]]
    ]

    for nums1, nums2 in cases:
        print(s.mergeArrays(nums1, nums2))


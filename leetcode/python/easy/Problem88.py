# Questions to ask:
# 1. What is the time complexity? O(m + n)
# 2. What is the space complexity?
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[i+j+1] = nums1[i]
                i -= 1
            else:
                nums1[i+j+1] = nums2[j]
                j -= 1



# Problem 88
# Tips:
# 1. Consider update num 1-by-1 from the end of num1; that's the max number of nums1 and nums2
# Link: https://leetcode.com/problems/merge-sorted-array/description/
if __name__ == '__main__':
    s = Solution()
    num11 = [1,2,3,5,0,0,0]
    s.merge(num11, 4, [2,5,6], 3)
    print(num11)
    num12 = [1,2,7,0,0,0]
    s.merge(num12, 3, [2,5,6], 3)
    print(num12)


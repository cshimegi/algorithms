# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
# Requirements:
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()
        l1, l2 = len(nums1), len(nums2)
        ans = []
        i, j = 0, 0
        while i < l1 and j < l2:
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return ans


# Problem 350
# Tips:
# Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
if __name__ == '__main__':
    s = Solution()
    print(s.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))

# Questions to ask:
# 1. What is the time complexity? O(log (m+n))
# 2. What is the space complexity?
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  # Ensure nums1 is smaller

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1

            # Get border values or use -∞ / ∞ for out-of-bounds
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]

            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]

            # Correct partition found
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 0:  # Even number of elements
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:  # Odd number of elements
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                right = partition1 - 1  # Move left
            else:
                left = partition1 + 1  # Move right



# Problem 4
# Link: https://leetcode.com/problems/median-of-two-sorted-arrays/description/
if __name__ == '__main__':
    s = Solution()


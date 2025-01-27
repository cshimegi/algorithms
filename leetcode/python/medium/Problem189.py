# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity? O(1)
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i -> i+k
        idx = []
        val = []
        l = len(nums)
        for i, num in enumerate(nums):
            idx.append((i+k)%l)
            val.append(num)

        for i in range(l):
            nums[idx[i]] = val[i]

    def rotate2(self, nums: list[int], k: int) -> None:
        n = len(nums)

        k %= n
        # Step 1: Reverse the entire array
        nums.reverse()

        # Step 2: Reverse the first k elements
        nums[:k] = reversed(nums[:k])

        # Step 3: Reverse the remaining n - k elements
        nums[k:] = reversed(nums[k:])


# Problem 189
# Link: https://leetcode.com/problems/rotate-array/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    nums1 = [1,2,3,4,5,6,7]
    s.rotate(nums1, 3)
    print(nums1) # [5,6,7,1,2,3,4]

    nums2 = [1,2,3,4,5,6,7,8]
    s.rotate(nums2, 5)
    print(nums2) # [4,5,6,7,8,1,2,3]


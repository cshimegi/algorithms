# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Time: O(n) / Space: O(n)
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
        # Time: O(n) / Space: O(1)
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
    cases = [
        ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
        ([1,2,3,4,5,6,7,8], 5, [4,5,6,7,8,1,2,3]),
    ]
    for nums, k, expected in cases:
        s.rotate(nums, k)
        assert nums == expected

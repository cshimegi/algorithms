# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Kadane's Algorithm
        ans = nums[0]
        curr = nums[0]
        for n in nums[1:]:
            curr = max(n, curr + n)
            ans = max(ans, curr)
        return ans

    def maxSubArray2(self, nums: list[int]) -> list[int]:
        # Kadane's Algorithm to return that subarray
        ans = nums[0]
        curr = nums[0]
        start, end = 0, 0
        for idx, n in enumerate(nums[1:], start=1): # Start indexing at 1
            if n > curr + n:
                curr = n
                start = idx
            else:
                curr += n

            if curr > ans:
                ans = curr
                end = idx
        return nums[start:end+1]


# Problem 53
# Link: https://leetcode.com/problems/maximum-subarray/description/
if __name__ == '__main__':
    s = Solution()
    arr1 = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray(arr1))
    print(s.maxSubArray2(arr1))

    arr2 = [1]
    print(s.maxSubArray(arr2))
    print(s.maxSubArray2(arr2))

    arr3 = [5,4,-1,7,8]
    print(s.maxSubArray(arr3))
    print(s.maxSubArray2(arr3))

    arr4 = [1, -2, 3, -1, 2, -1, 2, -5, 4]
    print(s.maxSubArray(arr4))
    print(s.maxSubArray2(arr4))

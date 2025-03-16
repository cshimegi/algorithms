# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if not nums:
            return 0

        # Initialize the maximum and minimum product up to the current position
        curr_max = nums[0]
        curr_min = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            # If the current number is negative, swap the max and min
            if nums[i] < 0:
                curr_max, curr_min = curr_min, curr_max

            # Calculate the max and min product up to the current number
            curr_max = max(nums[i], curr_max * nums[i])
            curr_min = min(nums[i], curr_min * nums[i])
            # Update the ans
            ans = max(ans, curr_max)

        return ans

    def maxProduct2(self, nums: list[int]) -> list[int]:
        """
        
        :return: subarray that produces max product 
        """
        if not nums:
            return []

        curr_max, curr_min = nums[0], nums[0]
        max_product = nums[0]
        start = end = temp_start = 0

        for i in range(1, len(nums)):
            num = nums[i]
            if num < 0:
                curr_max, curr_min = curr_min, curr_max  # Swap for negative numbers

            # Update the current max and min products
            if num > curr_max * num:
                curr_max = num
                temp_start = i  # Start a new subarray
            else:
                curr_max = curr_max * num

            curr_min = min(num, curr_min * num)

            # Update the max_product and indices
            if curr_max > max_product:
                max_product = curr_max
                start = temp_start
                end = i

        return nums[start:end + 1]

# Problem 152
# Link: https://leetcode.com/problems/maximum-product-subarray/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([-2,0,-1]))


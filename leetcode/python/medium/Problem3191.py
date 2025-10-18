# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(n)

# PROBLEM: Minimum Operations to Make Binary Array Elements Equal to One
# 
# Given a binary array, you can perform operations where you flip 3 consecutive elements.
# Goal: Make all elements equal to 1 using minimum operations, or return -1 if impossible.
#
# Key insight: We can only affect elements in groups of 3, so we need to process left to right.
#
# EXAMPLE WALKTHROUGH: [0,1,1,1,0,0]
# 
# Implementation 1 (Greedy with array modification):
# i=0: nums[0]=0 → flip [0,1,1] → [1,0,0,1,0,0], ans=1
# i=1: nums[1]=0 → flip [0,0,1] → [1,1,1,0,0,0], ans=2  
# i=2: nums[2]=1 → no flip
# i=3: nums[3]=0 → flip [0,0,0] → [1,1,1,1,1,1], ans=3
# Final: all 1s → return 3
#
# Implementation 2 (Space-optimized with tracking):
# Uses prev1, prev2 to track pending flips without modifying array
# Same logic but simulates the flips using XOR operations
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # IMPLEMENTATION 1: Greedy approach with array modification
        # Time: O(n), Space: O(1) - modifies input array
        
        ans, n = 0, len(nums)
        for i in range(n-2):  # Only process first n-2 elements
            if nums[i] == 0:  # If current element is 0, we must flip
                # Flip 3 consecutive elements starting from position i
                for j in range(i, i+3):
                    nums[j] ^= 1  # XOR with 1 flips the bit
                ans += 1  # Count this operation

        # Check if all elements are now 1
        return ans if sum(nums) == n else -1

    def minOperations2(self, nums: List[int]) -> int:
        # IMPLEMENTATION 2: Space-optimized approach without modifying input
        # Time: O(n), Space: O(1) - doesn't modify input array
        
        n = len(nums)
        prev1, prev2 = 0, 0  # Track pending flips from previous operations
        ans = 0
        
        for i in range(n-2):  # Process first n-2 elements
            # Check if current element needs flipping (considering pending flips)
            # nums[i] ^ prev1 ^ prev2 gives the effective value at position i
            if nums[i] ^ prev1 ^ prev2:  # If effective value is 1, no flip needed
                # No operation needed, just update tracking variables
                prev2 = prev1
                prev1 = 0
            else:  # If effective value is 0, we need to flip
                ans += 1
                # Update tracking: this flip affects positions i, i+1, i+2
                prev2 = prev1  # Previous flip moves to position i+1
                prev1 = 1      # Current flip affects position i+2
        
        # Check if last two elements are correctly set (considering pending flips)
        # Both should be 1 after all operations
        return ans if nums[n-1] ^ prev1 and nums[n-2] ^ prev1 ^ prev2 else -1

# Problem 3191
# Link: https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([0,1,1,1,0,0], 3),
        ([0,1,1,1], -1),
    ]
    for nums, expected in cases:
        assert s.minOperations(nums) == expected
        assert s.minOperations2(nums) == expected

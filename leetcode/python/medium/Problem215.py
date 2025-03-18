# Questions to ask:
# 1. What is the time complexity? O(n*log(k))
# 2. What is the space complexity? O(k)
from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
        return min_heap[0]

    def findKthSmallest(self, nums: List[int], k: int) -> int:
        # Kth smallest element is (len(nums)-k+1)th largest element
        min_heap = nums[:len(nums)-k+1]
        heapq.heapify(min_heap)

        for num in nums[len(nums)-k+1:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
        return min_heap[0]

# Problem 215
# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([1,4,2,8,5,2,2], 5, 2),
        ([1,4,2,8,5,2,2], 2, 5)
    ]
    for nums, k, expected in cases:
        assert s.findKthLargest(nums, k) == expected

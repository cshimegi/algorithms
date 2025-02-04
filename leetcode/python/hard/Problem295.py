# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
import heapq

class MedianFinder:
    def __init__(self):
        self.left = []  # Max heap (store as negative values)
        self.right = []  # Min heap

    def addNum(self, num: int) -> None:
        # Step 1: Add to the correct heap
        if not self.left or num <= -self.left[0]:
            heapq.heappush(self.left, -num)  # Use negative values to mimic max heap
        else:
            heapq.heappush(self.right, num)

        # Step 2: Balance heaps
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        elif len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]  # Max heap root (largest of left half)
        return (-self.left[0] + self.right[0]) / 2


# Problem 295
# Link: https://leetcode.com/problems/find-median-from-data-stream/description/
if __name__ == '__main__':
    s = Solution()


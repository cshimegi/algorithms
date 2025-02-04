# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity? < O(n^2)
class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        # Time: O(n^2)
        # Space: O(n^2)
        n = len(matrix)
        a = matrix[0]
        i = 1
        while i < n:
            temp = []
            j = 0
            for num in matrix[i]:
                while j < len(a) and a[j] <= num:
                    if a[j] <= num:
                        temp.append(a[j])
                        j += 1
                temp.append(num)
            a = temp
            i += 1
        return a[k-1]

    def kthSmallest_minHeap(self, matrix: list[list[int]], k: int) -> int:
        # Time: O(k*log(n))
        # Space: O(n)
        import heapq

        n = len(matrix)
        min_heap = [(matrix[i][0], i, 0) for i in range(n)]  # (value, row, col)
        heapq.heapify(min_heap)  # Convert into a min-heap

        for _ in range(k - 1):
            value, row, col = heapq.heappop(min_heap)  # Get smallest element
            if col + 1 < n:
                heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))  # Push next element from the same row

        return heapq.heappop(min_heap)[0]  # kth smallest element


    def kthSmallest_binarySearch(self, matrix: list[list[int]], k: int) -> int:
        # Time: O(n*log(max-min))
        # Space: O(1)
        # row-wise binary search
        n = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]

        def count_less_equal(mid):
            count, col = 0, n - 1
            for row in range(n):
                while col >= 0 and matrix[row][col] > mid:
                    col -= 1
                count += (col + 1)
            return count

        while left < right:
            mid = (left + right) // 2
            if count_less_equal(mid) < k:
                left = mid + 1
            else:
                right = mid

        return left  # kth smallest element



# Problem 378
# Link: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    print(s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))
    print(s.kthSmallest([[1,3,5],[6,7,12],[11,14,14]], 6))

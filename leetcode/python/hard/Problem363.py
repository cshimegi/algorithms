# Questions to ask:
# 1. What is the time complexity? O(m*n^2*log(n))
# 2. What is the space complexity?
from typing import List

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        import bisect

        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        max_sum = float('-inf')

        # Iterate over all row start points
        for r1 in range(m):
            # Accumulate column sums for range [r1, r2]
            col_sums = [0] * n

            for r2 in range(r1, m):  # Expand row range
                # Top to down column sum
                for c in range(n):
                    col_sums[c] += matrix[r2][c]

                # Use TreeSet (sorted list) to find max subarray sum <= k -> sum - k <= 0
                prefix_sums = [0]  # Stores sorted prefix sums
                curr_sum = 0

                # Left to right prefix column sum
                for col_sum in col_sums:
                    curr_sum += col_sum
                    # Find smallest prefix that gives sum <= k -> sum - k <= 0
                    idx = bisect.bisect_left(prefix_sums, curr_sum - k)
                    if idx < len(prefix_sums):
                        max_sum = max(max_sum, curr_sum - prefix_sums[idx])

                    # Insert current sum in sorted order
                    bisect.insort(prefix_sums, curr_sum)

        return max_sum


# Problem 363
# Link: https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([[1, 0, 1], [0, -2, 3]], 2),
        ([[2, 2, -1]], 3)
    ]
    for matrix, k in cases:
        print(s.maxSumSubmatrix(matrix, k))


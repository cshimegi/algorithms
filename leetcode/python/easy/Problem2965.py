# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(n)
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        cnt = Counter(col for row in grid for col in row)
        repeated, missing = 0, 0
        for i in range(1, n*n+1):
            if cnt[i] == 2:
                repeated = i
            if cnt[i] == 0:
                missing = i

        return [repeated, missing]

    def findMissingAndRepeatedValues2(self, grid: List[List[int]]) -> List[int]:
        # X-Y = S - actual_sum
        n = len(grid)
        total_numbers = n * n  # Total elements from 1 to n^2

        # Expected sums
        expected_sum = (total_numbers * (total_numbers + 1)) // 2

        # Compute actual sums from matrix
        actual_sum = 0
        actual_sum_squares = 0
        num_counts = {}

        for row in grid:
            for num in row:
                actual_sum += num
                actual_sum_squares += num * num
                num_counts[num] = num_counts.get(num, 0) + 1

        # Find the repeated number Y
        repeated = next(num for num, count in num_counts.items() if count > 1)

        # Use X - Y = expected_sum - actual_sum
        missing = repeated + (expected_sum - actual_sum)

        return [repeated, missing]


# Problem 2965
# Tips:
# Link: https://leetcode.com/problems/find-missing-and-repeated-values/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        [[1,3],[2,2]],
        [[9,1,7],[8,9,2],[3,4,6]],
    ]
    for case in cases:
        print(s.findMissingAndRepeatedValues(case))


# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def numSquares(self, n: int) -> int:
        from collections import deque

        squares = [i * i for i in range(1, int(n**0.5) + 1)]
        queue = deque([(n, 0)])  # (remaining sum, step count)
        visited = set()

        while queue:
            remainder, steps = queue.popleft()
            if remainder == 0:
                return steps  # Found the answer

            for sq in squares:
                next_val = remainder - sq
                if next_val < 0:
                    break
                if next_val not in visited:
                    visited.add(next_val)
                    queue.append((next_val, steps + 1))

    def numSquares2(self, n: int) -> int:
        # Lagrange’s Four Square Theorem
        while n % 4 == 0:
            n >>= 2

        if n % 8 == 7:
            return 4

        squares = [i*i for i in range(1, int(sqrt(n))+1)]
        if n in squares:
            return 1

        for square in squares:
            if n - square in squares:
                return 2

        return 3


# Problem 279
# Link: https://leetcode.com/problems/perfect-squares/description/
# Tips:
if __name__ == '__main__':
    s = Solution()


# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?

# COMPLEXITY ANALYSIS:
# 
# Both implementations use backtracking to solve the problem.
# The key difference is the order of trying numbers:
# - constructDistancedSequence: tries numbers from n down to 1 (largest first)
# - constructDistancedSequence2: tries numbers from 1 to n (smallest first)
#
# TIME COMPLEXITY: O(n! * n)
# 
# Detailed Analysis:
# 1. Problem Structure:
#    - We need to place numbers 1 to n in a sequence of length 2n-1
#    - Number 1 appears once, numbers 2 to n appear twice each
#    - For number k (k > 1), if placed at position i, it must also be at position i+k
#
# 2. Backtracking Process:
#    - At each step, we try to place a number at the current position
#    - We have n choices for which number to place
#    - Each choice may place 1 or 2 numbers in the sequence
#    - We backtrack if a choice leads to an invalid state
#
# 3. Complexity Calculation:
#    - Number of recursive calls: In worst case, we explore all valid permutations
#    - For n numbers with constraints, this is approximately O(n!)
#    - At each recursive call, we do O(n) work (checking all numbers)
#    - Total: O(n! * n)
#
# 4. Practical Performance:
#    - The actual runtime is often much better due to early pruning
#    - Invalid placements are detected quickly, reducing the search space
#    - Both implementations have the same worst-case complexity
#
# SPACE COMPLEXITY: O(n)
# - ans array: O(2n-1) = O(n)
# - used array: O(n+1) = O(n)
# - Recursion stack depth: O(n) in the worst case
# - Total: O(n)
class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        # Implementation 1: Tries largest numbers first
        # This tends to find the lexicographically LARGEST valid sequence
        # Time: O(n! * n), Space: O(n)
        ans = [0] * (n*2-1)
        used = [False] * (n+1)

        def backtrack(i: int):
            if i == n*2-1:
                return True

            if ans[i] != 0:
                return backtrack(i+1)

            for j in range(n, 0, -1):
                if used[j]:
                    continue

                if j == 1 or (i + j < n*2-1 and ans[i+j] == 0):
                    # Use the number
                    ans[i] = j
                    if j > 1:
                        ans[i+j] = j
                    used[j] = True

                    if backtrack(i+1):
                        return True
                    # Revert the used number state
                    ans[i] = 0
                    if j > 1:
                        ans[i+j] = 0
                    used[j] = False
            return False

        backtrack(0)
        return ans

    def constructDistancedSequence2(self, n: int) -> list[int]:
        # Implementation 2: Tries smallest numbers first
        # This tends to find the lexicographically SMALLEST valid sequence
        # Time: O(n! * n), Space: O(n)
        ans = [0] * (n * 2 - 1)
        used = [False] * (n + 1)

        def backtrack(i: int):
            if i == n * 2 - 1:
                return True

            if ans[i] != 0:  # Skip filled positions
                return backtrack(i + 1)

            for j in range(1, n + 1):  # Iterate from smallest to largest
                if used[j]:
                    continue

                if j == 1 or (i + j < n * 2 - 1 and ans[i + j] == 0):
                    ans[i] = j
                    if j > 1:
                        ans[i + j] = j
                    used[j] = True

                    if backtrack(i + 1):
                        return True

                    # Undo choice (Backtracking)
                    ans[i] = 0
                    if j > 1:
                        ans[i + j] = 0
                    used[j] = False

            return False

        backtrack(0)
        return ans

# Problem 1718
# Link: https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        (3, [3,1,2,3,2]),
        (5, [5,3,1,4,3,5,2,4,2]),
    ]
    for n, expected in cases:
        assert s.constructDistancedSequence(n) == expected
        assert s.constructDistancedSequence2(n) == expected

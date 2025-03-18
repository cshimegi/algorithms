# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
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
        # Return the smallest possible sequence
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

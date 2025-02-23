# Questions to ask:
# 1. What is the time complexity? O(m⋅n)
# 2. What is the space complexity?
class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        cache = [[-1]*n for _ in range(m)]

        def dfs(i: int, j: int) -> int:
            if cache[i][j] != -1:
                return cache[i][j]

            max_path = 1
            for di, dj in directions:
                new_i, new_j = i+di, j+dj
                if 0 <= new_i < m and 0 <= new_j < n and matrix[new_i][new_j] > matrix[i][j]:
                    max_path = max(max_path, dfs(new_i, new_j)+1)
            cache[i][j] = max_path
            return max_path

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))

        return ans


# Problem 329
# Link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        [
            [9,9,4],
            [6,6,8],
            [2,1,1]
        ],
        [
            [3,4,5],
            [3,2,6],
            [2,2,1]
        ],
        [[1]]
    ]
    for case in cases:
        print(s.longestIncreasingPath(case))


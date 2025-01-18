# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        ans = []
        for n in range(numRows):
            ans.append([1] * (n+1))
            for i in range(1, n):
                ans[n][i] = ans[n-1][i-1] + ans[n-1][i]
        return ans


# Problem 118
# Tips:
# 1.
# Link: https://leetcode.com/problems/pascals-triangle/description/
if __name__ == '__main__':
    s = Solution()
    print(s.generate(3))
    print(s.generate(5))


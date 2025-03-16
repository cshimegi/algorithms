# Questions to ask:
# 1. What is the time complexity? O(2^n)
# 2. What is the space complexity? O(2^n)
class Solution:
    def backtrack(self, s: str, open_count: int, close_count: int, ans: list[str]) -> None:
        if open_count == 0 and close_count == 0:
            ans.append(s)
            return

        if open_count > 0:
            self.backtrack(s + "(", open_count - 1, close_count, ans)

        if close_count > open_count:
            self.backtrack(s + ")", open_count, close_count - 1, ans)

    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        self.backtrack("", n, n, ans)
        return ans


# Problem 22
# Link: https://leetcode.com/problems/generate-parentheses/description/
if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))

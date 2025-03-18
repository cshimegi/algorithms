# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(n)
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack, ans = [], ""
        for i, c in enumerate(pattern + "I", 1):
            stack.append(str(i))
            if c == "I":
                while stack:
                    ans += stack.pop()
        return ans

# Problem 2375
# Link: https://leetcode.com/problems/construct-smallest-number-from-di-string/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ("IIIDIDDD", "123549876"),
        ("DDD", "4321"),
    ]
    for pattern, expected in cases:
        assert s.smallestNumber(pattern) == expected

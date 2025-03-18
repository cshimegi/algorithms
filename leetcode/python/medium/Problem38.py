# Questions to ask:
# 1. What is the time complexity? O(n*m) where m is the length of the string
# 2. What is the space complexity? O(1)
class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        for _ in range(1, n):
            temp = ""
            count = 1
            curr = ans[0]
            for j in ans[1:]:
                if j == curr:
                    count += 1
                else:
                    temp += str(count) + curr
                    curr = j
                    count = 1
            temp += str(count) + curr
            ans = temp
        return ans

# Problem 38
# Link: https://leetcode.com/problems/count-and-say/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        (1, "1"),
        (4, "1211"),
        (7, "13112221"),
        (10, "13211311123113112211")
    ]
    for n, expected in cases:
        assert s.countAndSay(n) == expected

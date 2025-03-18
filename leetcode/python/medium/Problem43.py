# Questions to ask:
# 1. What is the time complexity? O(m*n)
# 2. What is the space complexity? O(m+n)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        # Multipy numbers without using built-in functions
        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                """
                0 0 0 0 0 0 0  0    0
                          <-- pos1 pos2
                """
                mul = int(num1[i]) * int(num2[j])
                pos1, pos2 = i + j + 1, i + j

                # Add to current position in result array
                total = mul + result[pos1]
                result[pos1] = total % 10  # Store number at right position
                result[pos2] += total // 10  # Carry to next right position

        return "".join(map(str, result)).lstrip("0")


# Problem 43
# Link: https://leetcode.com/problems/multiply-strings/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ("2", "3", "6"),
        ("123", "456", "56088"),
    ]

    for num1, num2, expected in cases:
        assert s.multiply(num1, num2) == expected

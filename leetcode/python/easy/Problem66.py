# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        ans = [0] * (l + 1)

        carry = 1
        for i in range(l-1, -1, -1):
            ans[i+1] = (digits[i] + carry) % 10
            carry = (digits[i] + carry) // 10

        if carry > 0:
            ans[0] = carry
            return ans
        else:
            return ans[1:]

# Problem 66
# Tips:
# 1. Be careful of the cases which carry is greater than 0 when it comes to most significant digit
# Link: https://leetcode.com/problems/plus-one/description/
if __name__ == '__main__':
    s = Solution()

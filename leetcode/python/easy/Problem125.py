# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


# Problem 125
# Tips:
# 1.
# Link: https://leetcode.com/problems/valid-palindrome/description/
if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(s = "A man, a plan, a canal: Panama"))

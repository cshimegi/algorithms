# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        ans = s[0]
        max_len = 1
        for i in range(l-1):
            for j in range(i+1, l):
                if j-i+1 > max_len and s[i:j+1] == s[i:j+1][::-1]:
                    ans = s[i:j+1]
                    max_len = j-i+1
        return ans

    # Manacher's Algorithm
    def longestPalindrome2(self, s: str) -> str:
        l = len(s)
        if l <= 1:
            return s
        # Ensure the length of string is always odd
        hashed_s = "#" + "#".join(s) + "#"
        l_hashed_s = 2*l+1
        max_len = 0
        ans = ""
        for i in range(l_hashed_s):
            r = 0
            while i+r < l_hashed_s and i-r >= 0 and hashed_s[i-r] == hashed_s[i+r]:
                r += 1

            # r must be reduced by 1 because hashed_s[i-r] != hashed_s[i+r] when r
            if 2*(r-1)+1 > max_len:
                max_len = 2*(r-1)+1
                ans = hashed_s[i-r+1:i+r]
        return ans.replace("#", "")

# Problem 5
# Link: https://leetcode.com/problems/longest-palindromic-substring/description/
if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome2("babad"))
    print(s.longestPalindrome2("cbbd"))
    print(s.longestPalindrome2("aaaaaaaaa"))

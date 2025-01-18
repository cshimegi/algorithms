# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
# 3. A -> 65, Z -> 90
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for c in columnTitle:
            ans = ans * 26 + ord(c) - ord('A') + 1
        return ans

# Problem 171
# Tips:
# 1. 
# Link: https://leetcode.com/problems/excel-sheet-column-number/description/
if __name__ == '__main__':
    s = Solution()
    print(s.titleToNumber(columnTitle = "A"))
    print(s.titleToNumber(columnTitle = "FXSHRXW"))

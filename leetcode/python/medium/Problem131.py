# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def isPalindrome(self, sub_str: str) -> bool:
        return sub_str == sub_str[::-1]

    def partition(self, s: str) -> list[list[str]]:
        ans = []
        l = len(s)

        def backtrack(start: int, path: list[str]):
            # If we have reached the end of the string, add the current partition to the result
            if start == l:
                ans.append(path[:])
                return
            # Explore all possible substrings starting from `start`
            for end in range(start, l):
                if self.isPalindrome(s[start:end+1]):
                    # Choose: Add the current substring to the path
                    path.append(s[start:end+1])
                    # Explore further partitions
                    backtrack(end+1, path)
                    # Undo the choice
                    path.pop()

        backtrack(0, [])
        return ans


# Problem 131
# Link: https://leetcode.com/problems/palindrome-partitioning/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
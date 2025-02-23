class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        # Cantor’s Diagonalization
        return ''.join('1' if num[i] == '0' else '0' for i, num in enumerate(nums))


# Problem 1980
# Link: https://leetcode.com/problems/find-unique-binary-string/description/
if __name__ == '__main__':
    s = Solution()


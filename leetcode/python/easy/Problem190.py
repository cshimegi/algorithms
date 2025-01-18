# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def reverseBits(self, n: int) -> int:
        bin_str = bin(n)[2:]
        ans = ""
        for i in range(len(bin_str)-1, -1, -1):
            ans += bin_str[i]
        return int(ans.ljust(32, '0'), 2)

    def reverseBits2(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)

# Problem 190
# Tips:
# 1. 
# Link: https://leetcode.com/problems/reverse-bits/description/
if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(0b00000010100101000001111010011100))

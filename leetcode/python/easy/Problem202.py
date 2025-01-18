# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def isHappy(self, n: int) -> bool:
        repeated = {}
        while repeated.get(n, 0) == 0:
            repeated[n] = 1
            temp = 0
            while n > 0:
                temp += (n%10)**2
                n = n//10
            if temp == 1:
                return True
            n = temp
        return False

# Problem 202
# Tips:
# 1. Need to ensure it won't run endlessly
# 2. If not happy number, it must be repeated somewhere
# For example,
# (1) 19 -> 82 -> 68 -> 100 -> 1 => happy
# (2) 12 -> 5 -> 25 -> 29 -> 85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89 => not happy
# Link: https://leetcode.com/problems/happy-number/description/
if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(19))
    print(s.isHappy(2147483647))

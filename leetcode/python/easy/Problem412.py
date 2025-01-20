# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        return ['Fizz' * (n % 3 == 0) + 'Buzz' * (n % 5 == 0) or str(n) for n in range(1, n+1)]

# Problem 412
# Tips:
# Link: https://leetcode.com/problems/fizz-buzz/description/
if __name__ == '__main__':
    s = Solution()
    print(s.fizzBuzz(15))


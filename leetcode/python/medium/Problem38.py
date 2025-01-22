# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        for _ in range(1, n):
            temp = ""
            count = 1
            curr = ans[0]
            for j in ans[1:]:
                if j == curr:
                    count += 1
                else:
                    temp += str(count) + curr
                    curr = j
                    count = 1
            temp += str(count) + curr
            ans = temp
        return ans

# Problem 38
# Link: https://leetcode.com/problems/count-and-say/description/
if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(1))  # "1"
    print(s.countAndSay(4))  # "1211"
    print(s.countAndSay(7))  # "13112221"
    print(s.countAndSay(10)) # "13211311123113112211"

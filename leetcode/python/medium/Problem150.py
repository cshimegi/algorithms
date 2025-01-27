# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for t in tokens:
            if t in ("+", "-", "*", "/"):
                second_num = stack.pop()
                first_num = stack.pop()
                if t == "+":
                    stack.append(first_num + second_num)
                elif t == "-":
                    stack.append(first_num - second_num)
                elif t == "*":
                    stack.append(first_num * second_num)
                else:
                    stack.append(int(first_num / second_num))
            else:
                stack.append(int(t))
        return stack[0]



# Problem 150
# Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    print(s.evalRPN(["4","13","5","/","+"]))

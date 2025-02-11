# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")  # Remove spaces
        stack = []
        num = 0
        sign = "+" # Default sign for the first number

        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c) # Construct multi-digit numbers
            if c in "+-*/" or i == len(s) - 1: # Process when it's at the end
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(int(stack.pop() / num))

                num = 0  # Reset num for the next number
                sign = c  # Store the current operator
        return sum(stack)


    def calculate2(self, s: str) -> int:
        # Advanced: for s including nested parentheses
        def evaluate(index: int) -> (int, int):
            stack = []
            num = 0
            sign = "+"

            while index < len(s):
                char = s[index]

                if char.isdigit():
                    num = num * 10 + int(char)  # Handle multi-digit numbers
                if char == "(":
                    num, index = evaluate(index + 1)  # Recursively evaluate inner expression
                # Process it reaches the end or sign is found
                if char in "+-*/)" or index == len(s) - 1:
                    if sign == "+":
                        stack.append(num)
                    elif sign == "-":
                        stack.append(-num)
                    elif sign == "*":
                        stack.append(stack.pop() * num)
                    elif sign == "/":
                        stack.append(int(stack.pop() / num))  # Integer division towards zero

                    num = 0  # Reset for next number
                    sign = char  # Store current operator

                    if char == ")":  # End of subexpression
                        return sum(stack), index
                index += 1  # Move to next character

            return sum(stack), index  # Return final sum and index

        return evaluate(0)[0]  # Start from index 0 and return result


# Problem 227
# Link: https://leetcode.com/problems/basic-calculator-ii/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    print(s.calculate2("2*(3+4)-5"))
    print(s.calculate2("2*(3+4*(2+9))-5"))

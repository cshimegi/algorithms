class Solution:
    # Questions to ask:
    # 1. Is the string: ([)] valid?
    # 2. Is the string: ([{}]) valid?
    # 3. Is the string s guaranteed to be non-empty?
    # 4. What is the maximum length of s?
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '[':']', '{':'}'}
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    # Check last element in stack
                    last_element = stack.pop()
                    if brackets[last_element] != c:
                        return False
        return len(stack) == 0


# Problem 20
# Link: https://leetcode.com/problems/valid-parentheses/description/
if __name__ == '__main__':
    s = Solution()
    print(s.isValid(s = "()"))
    print(s.isValid(s = "()[]{}"))
    print(s.isValid(s = "((()))"))
    print(s.isValid(s = "((())"))
    print(s.isValid(s = "([)]"))
    print(s.isValid(s = "([])"))
    print(s.isValid(s = "([{}])"))
    print(s.isValid(s = "))))"))

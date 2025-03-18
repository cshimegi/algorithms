# Questions to ask:
# 1. What is the time complexity? O(3^x*4^y)
# 2. What is the space complexity? O(3^x*4^y)
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        dl = {
            "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
            "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]
        }

        l = len(digits)
        if l == 0:
            return []
        elif l == 1:
            return dl[digits]

        ans = dl[digits[0]]
        for d in digits[1:]:
            temp, letters = [], dl[d]
            for c in ans:
                for letter in letters:
                    temp.append(c+letter)
            ans = temp
        return ans


    def backtrack(self, combination: str, next_digit: str | None, ans: list[str], dl: dict):
        if next_digit == "":
            ans.append(combination)
            return

        for l in dl[next_digit[0]]:
            self.backtrack(combination + l, next_digit[1:], ans, dl)


    def letterCombinations2(self, digits: str) -> list[str]:
        dl = {
            "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
            "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]
        }
        l = len(digits)
        if l == 0:
            return []
        elif l == 1:
            return dl[digits]

        ans = []
        self.backtrack("", digits, ans, dl)
        return ans



# Problem 17
# Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    ]
    for digits, expected in cases:
        assert s.letterCombinations(digits) == expected
        assert s.letterCombinations2(digits) == expected

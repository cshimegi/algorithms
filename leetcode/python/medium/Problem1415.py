class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        combinations = []

        def backtrack(curr: str):
            if len(curr) == n:
                combinations.append(curr)
                return
    
            for c in "abc":
                if not curr or curr[-1] != c:
                    backtrack(curr + c)
    
        backtrack("")
    
        return combinations[k - 1] if k <= len(combinations) else ""

# Problem 1415
# Link: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        (1, 3, "c"),
        (1, 4, ""),
        (3, 9, "cab"),
    ]
    for n, k, expected in cases:
        assert s.getHappyString(n, k) == expected

# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Problem 100
# Tips:
# Link: https://leetcode.com/problems/same-tree/description/
if __name__ == '__main__':
    s = Solution()
    cases = []
    for case in cases:
        print(s.isSameTree(case[0], case[1]))

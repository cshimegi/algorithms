# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right



# Problem 236
# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
# Tips:
if __name__ == '__main__':
    s = Solution()


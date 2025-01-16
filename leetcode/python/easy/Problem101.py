# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def compare(self, leftNode: TreeNode | None, rightNode: TreeNode | None) -> bool:
        if leftNode is None and rightNode is None:
            return True

        if leftNode is None or rightNode is None:
            return False

        if leftNode.val != rightNode.val:
            return False

        return self.compare(leftNode.left, rightNode.right) and self.compare(leftNode.right, rightNode.left)

    def isSymmetric(self, root: TreeNode | None) -> bool:
        return self.compare(root.left, root.right)


# Problem 101
# Tips:
# 1.
# Link: https://leetcode.com/problems/symmetric-tree/description/
if __name__ == '__main__':
    s = Solution()



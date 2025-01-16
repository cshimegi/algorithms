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
    def measureDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        # 1 is for counting itself
        return 1 + max(self.measureDepth(root.left), self.measureDepth(root.right))

    def maxDepth(self, root: TreeNode | None) -> int:
        return self.measureDepth(root)


# Problem 104
# Tips:
# 1.
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
if __name__ == '__main__':
    s = Solution()
    print(s.maxDepth(TreeNode(1, TreeNode(2), TreeNode(3))))


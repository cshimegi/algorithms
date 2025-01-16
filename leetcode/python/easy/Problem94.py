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
    def traversal(self, root: TreeNode | None, ans: list[int]) -> list[int]:
        if root is None:
            return ans

        self.traversal(root.left, ans)
        ans.append(root.val)
        self.traversal(root.right, ans)

        return ans

    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        return self.traversal(root, [])


# Problem 94
# Tips:
# 1.
# Link: https://leetcode.com/problems/binary-tree-inorder-traversal/description/
if __name__ == '__main__':
    s = Solution()
    print(s.inorderTraversal(TreeNode(1, TreeNode(2), TreeNode(3))))


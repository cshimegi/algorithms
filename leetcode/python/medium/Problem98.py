# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_valid(self, node: TreeNode | None, lower: float, upper: float) -> bool:
        if node is None:
            return True

        # Validate current node value
        if not (lower < node.val < upper):
            return False

        # Recursively validate left and right subtrees
        return self.is_valid(node.left, lower, node.val) and self.is_valid(node.right, node.val, upper)

    def isValidBST(self, root: TreeNode | None) -> bool:
        # Initialize with the full range of valid values
        return self.is_valid(root, float('-inf'), float('inf'))


# Problem 98
# Link: https://leetcode.com/problems/validate-binary-search-tree/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    print(s.isValidBST(TreeNode(1, TreeNode(2), TreeNode(3))))

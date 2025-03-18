# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(n)
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode | None:
        post_idx = {val: i for i, val in enumerate(postorder)}  # Map for quick lookup
        pre_idx = 0

        def build(left: int, right: int) -> TreeNode | None:
            nonlocal pre_idx
            if left > right:
                return None

            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1

            if left == right:
                return root  # Leaf node

            left_root_val = preorder[pre_idx]
            left_subtree_end = post_idx[left_root_val]

            root.left = build(left, left_subtree_end)
            root.right = build(left_subtree_end + 1, right - 1)

            return root

        return build(0, len(postorder) - 1)
        

# Problem 889
# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/
if __name__ == '__main__':
    s = Solution()

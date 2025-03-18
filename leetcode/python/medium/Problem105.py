# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(n)
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Pre-order: root -> left -> right
# In-order: left -> root -> right
# Post-order: left -> right -> root
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode | None:
        if not preorder or not inorder:
            return None

        # Precompute indices of inorder values
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}

        def build(preorder: List[int], inorder_start: int, inorder_end: int) -> TreeNode | None:
            if inorder_start > inorder_end:
                return None

            # The first element of preorder is the root
            root_val = preorder.pop(0)
            root = TreeNode(root_val)

            # Get the index of the root in inorder traversal
            inorder_index = inorder_index_map[root_val]

            # Recursively build the left and right subtrees
            root.left = build(preorder, inorder_start, inorder_index - 1)
            root.right = build(preorder, inorder_index + 1, inorder_end)

            return root

        return build(preorder, 0, len(inorder) - 1)


    # Further practice for building a tree from postorder and inorder
    def buildTree2(self, postorder: List[int], inorder: List[int]) -> TreeNode | None:
        if not postorder or not inorder:
            return None

        # Precompute indices of inorder values
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}

        def build(postorder: List[int], inorder_start: int, inorder_end: int) -> TreeNode | None:
            if inorder_start > inorder_end:
                return None

            # The last element of postorder is the root
            root_val = postorder.pop()
            root = TreeNode(root_val)

            # Get the index of the root in inorder traversal
            inorder_index = inorder_index_map[root_val]

            # Recursively build the right and left subtrees
            root.left = build(postorder, inorder_start, inorder_index - 1)
            root.right = build(postorder, inorder_index + 1, inorder_end)

            return root

        return build(postorder, 0, len(inorder) - 1)



# Problem 105
# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
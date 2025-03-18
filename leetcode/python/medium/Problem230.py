# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        # O(n) Time | O(1) Space
        count = 0
        ans = None

        def inorder(node: TreeNode | None):
            nonlocal count, ans
            if not node or ans is not None:
                return

            # Visit left subtree
            inorder(node.left)

            # Process the current node
            count += 1
            if count == k:
                ans = node.val
                return  # Stop further traversal

            # Visit right subtree
            inorder(node.right)

        inorder(root)
        return ans

    def kthSmallest2(self, root: TreeNode | None, k: int) -> int:
        # O(n) Time | O(n) Space
        stack = []
        curr = root
        count = 0

        while stack or curr:
            # Go left as far as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            # Process the smallest element
            curr = stack.pop()
            count += 1
            if count == k:
                return curr.val

            # Move to the right subtree
            curr = curr.right

# Problem 230
# Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# Tips:
if __name__ == '__main__':
    s = Solution()


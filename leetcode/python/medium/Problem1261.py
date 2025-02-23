# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    def __init__(self, root: TreeNode | None):
        self.values = set()

        def recover(node: TreeNode | None):
            if not node:
                return

            if node.left:
                node.left.val = 2 * node.val + 1
                self.values.add(node.left.val)
                recover(node.left)
            if node.right:
                node.right.val = 2 * node.val + 2
                self.values.add(node.right.val)
                recover(node.right)

        root.val = 0
        self.values.add(root.val)
        recover(root)

    def find(self, target: int) -> bool:
        return target in self.values

# Problem 1261
# Link: https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/description/
if __name__ == '__main__':
    s = Solution()

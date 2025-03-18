# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bfs(self, node: TreeNode | None, level: int, res: List[List[int]]):
        if node is None:
            return

        if level >= len(res):
            res.append([])
        res[level] += [node.val]

        if node.left:
            self.bfs(node.left, level+1, res)
        if node.right:
            self.bfs(node.right, level+1, res)

    def levelOrder(self, root: TreeNode | None) -> List[List[int]]:
        ans = []
        self.bfs(root, 0, ans)
        return ans

    def levelOrder2(self, root: TreeNode | None) -> List[List[int]]:
        if not root:
            return []

        from collections import deque
        ans = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level)
        return ans


# Problem 102
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bfs(self, node: TreeNode | None, level: int, direction: int, res: list[list[int]]):
        if node is None:
            return

        if level >= len(res):
            res.append([])

        # For direction: 0 is from left to right and 1 is from right to left
        if direction == 0:
            res[level] = res[level] + [node.val]
        else:
            res[level] = [node.val] + res[level]

        direction ^= 1 # Change direction
        if node.left:
            self.bfs(node.left, level+1, direction, res)
        if node.right:
            self.bfs(node.right, level+1, direction, res)

    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        ans = []
        self.bfs(root, 0, 0, ans)
        return ans

    def zigzagLevelOrder2(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        from collections import deque
        ans = []
        queue = deque([root])
        direction = 0
        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                if direction == 0:
                    level = level + [node.val]
                else:
                    level = [node.val] + level

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level)
            direction ^= 1
        return ans


# Problem 103
# Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
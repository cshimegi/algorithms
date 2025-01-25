# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        from collections import deque

        curr = root
        queue = deque([curr])
        while queue:
            level_size = len(queue)
            prev_node = None
            for _ in range(level_size):
                curr_node = queue.popleft()
                if prev_node:
                    prev_node.next = curr_node
                prev_node = curr_node

                if curr_node and curr_node.left:
                    queue.append(curr_node.left)
                if curr_node and curr_node.right:
                    queue.append(curr_node.right)
        return root


    def connect2(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(node: 'Optional[Node]'):
            if not node or not node.left:
                return

            node.left.next = node.right
            if node.next:
                node.right.next = node.next.left

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return root

    def connect3(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        left_node = root
        while left_node.left:
            head = left_node
            # BFS
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next # --> move to next node at the same level
            left_node = left_node.left
        return root


# Problem 116
# Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
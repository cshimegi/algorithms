# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from typing import Optional
class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        # Time: O(n)/Space: O(n)
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


    def connect2(self, root: Optional[Node]) -> Optional[Node]:
        # Time: O(n)/Space: O(log(n)): due to recursive call stack
        def dfs(node: Optional[Node]):
            if not node or not node.left:
                return

            node.left.next = node.right
            if node.next:
                node.right.next = node.next.left

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return root

    def connect3(self, root: Optional[Node]) -> Optional[Node]:
        """
        How It Works:
        Outer loop: Iterates through each level using leftmost_node
        Inner loop: Traverses horizontally across the current level using current
        Key insight: Uses the already-connected next pointers to traverse 
            horizontally, achieving O(1) space complexity without a queue
            The code is now much easier to understand while maintaining the 
            same O(n) time and O(1) space
        """
        # Time: O(n) / Space: O(1)
        # Uses the tree structure itself to traverse levels without a queue
        if not root:
            return root

        # Start from the root and process level by level
        leftmost_node = root
        
        # Continue until we reach the last level (no more children)
        while leftmost_node.left:
            # Traverse the current level horizontally
            current = leftmost_node
            
            while current:
                # Connect left child to right child
                current.left.next = current.right
                
                # Connect right child to the next node's left child (if exists)
                if current.next:
                    current.right.next = current.next.left
                
                # Move to the next node in the same level
                current = current.next
            
            # Move down to the next level (go to leftmost node)
            leftmost_node = leftmost_node.left
        
        return root


# Problem 116
# Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
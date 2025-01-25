# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Copy nodes and prepare mapping for random pointers
        dummy = Node(0)
        records, curr, copy = {}, head, dummy
        while curr:
            copy.next = Node(curr.val, curr.next)
            records[curr] = copy.next
            curr, copy = curr.next, copy.next

        # Step 2: set up random pointers
        curr, copy = head, dummy.next
        while curr:
            copy.random = records[curr.random] if curr.random else None
            curr, copy = curr.next, copy.next

        return dummy.next

# Problem 138
# Link: https://leetcode.com/problems/copy-list-with-random-pointer/description/
# Tips:
if __name__ == '__main__':
    s = Solution()


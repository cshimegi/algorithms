# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        visited = {}
        while head is not None:
            if visited.get(head, 0) == 1:
                return True
            visited[head] = 1
            head = head.next
        return False

    def hasCycle2(self, head: ListNode | None) -> bool:
        if head is None:
            return False

        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True



# Problem 141
# Tips:
# 1.
# Link: https://leetcode.com/problems/linked-list-cycle/description/
if __name__ == '__main__':
    s = Solution()
    # Create nodes
    node3 = ListNode(3)
    node2 = ListNode(2)
    node0 = ListNode(0)
    node4 = ListNode(4)

    # Link nodes to form the list 3 -> 2 -> 0 -> 4
    node3.next = node2
    node2.next = node0
    node0.next = node4

    # Create the cycle: 0 -> 2
    node4.next = node2

    s = Solution()
    # Test hasCycle and hasCycle2
    print(s.hasCycle(node3))  # Expected: True
    print(s.hasCycle2(node3))  # Expected: True

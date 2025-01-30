# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:  # Edge case: empty list or one node
            return head

        odd = head  # Points to the first node (odd)
        even = head.next  # Points to the second node (even)
        even_head = even  # Store the head of even list

        while even and even.next:
            odd.next = even.next  # Link current odd node to next odd node
            odd = odd.next  # Move odd pointer forward

            even.next = odd.next  # Link current even node to next even node
            even = even.next  # Move even pointer forward

        odd.next = even_head  # Merge odd list with even list

        return head


# Problem 328
# Link: https://leetcode.com/problems/odd-even-linked-list/description/
# Tips:
if __name__ == '__main__':
    s = Solution()


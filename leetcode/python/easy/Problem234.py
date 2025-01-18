# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            # 1 step
            slow = slow.next
            # 2 steps
            fast = fast.next.next

        # Revers the slow because it includes the nodes from the middle to the end
        rslow = None
        while slow is not None:
            next = slow.next
            slow.next = rslow
            rslow = slow
            slow = next

        # Compare
        while head is not None:
            if rslow.val != head.val:
                return False
            rslow = rslow.next
            head = head.next
        return True

# Problem 234
# Tips:
# Link: https://leetcode.com/problems/palindrome-linked-list/description/
if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))
    print(s.isPalindrome(head = ListNode(1, ListNode(2))))

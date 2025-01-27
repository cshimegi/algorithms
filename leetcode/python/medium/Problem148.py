# Questions to ask:
# 1. What is the time complexity? O(n*log(n))
# 2. What is the space complexity? O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge(self, list1: ListNode | None, list2: ListNode | None):
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return dummy.next

    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None # Split it into 2 parts

        left = self.sortList(head) # first to slow
        right = self.sortList(mid) # slow.next to tail

        return self.merge(left, right)


# Problem 148
# Link: https://leetcode.com/problems/sort-list/description/
# Tips:
if __name__ == '__main__':
    s = Solution()

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
# 3. Are list1 and list2 sorted?
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        ans = ListNode()
        # Need head to always point to the last node of ans
        head = ans
        # Point the head to correct node
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        # Append the remaining list
        if list1 is not None:
            head.next = list1
        if list2 is not None:
            head.next = list2
        return ans.next


# Problem 21
# Link: https://leetcode.com/problems/merge-two-sorted-lists/description/
if __name__ == '__main__':
    s = Solution()
    print(s.mergeTwoLists(
        list1 = ListNode(1, ListNode(2, ListNode(4))),
        list2 = ListNode(1, ListNode(3, ListNode(4)))
    ))
    print(s.mergeTwoLists(
        list1 = None,
        list2 = ListNode(0)
    ))

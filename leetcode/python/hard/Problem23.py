# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        # Need head to always point to the last node of dummy
        head = dummy
        # Point the head to correct node
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        # Append the remaining list
        head.next = list1 or list2
        return dummy.next

    def mergeKlists(self, lists: list[ListNode | None]) -> ListNode | None:
        # O(n * k)
        l = len(lists)
        if l == 0:
            return None
        if l == 1:
            return lists[0]

        while len(lists) >= 2:
            list1 = lists.pop(0)
            list2 = lists.pop(0)
            lists.append(self.merge(list1, list2))

        return lists[0]


    def mergeKLists2(self, lists: list[ListNode | None]) -> ListNode | None:
        # O(n * log(k))
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        left = self.mergeKLists2(lists[:mid])
        right = self.mergeKLists2(lists[mid:])

        return self.merge(left, right)


# Problem 23
# Link: https://leetcode.com/problems/merge-k-sorted-lists/description/
if __name__ == '__main__':
    s = Solution()


# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

# Problem 206
# Tips:
# 1. Reverse the link between adjacent nodes
#    For example, 1 -> 2 -> 3 will be reversed to 1 <- 2 <- 3
# Link: https://leetcode.com/problems/reverse-linked-list/description/
if __name__ == '__main__':
    s = Solution()
    print(s.reverseList(head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))


# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        ans = ListNode()
        curr = ans
        carry = 0
        while l1 is not None or l2 is not None:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            s = x + y + carry
            carry = s // 10
            curr.next = ListNode(s % 10)
            curr = curr.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        if carry != 0:
            curr.next = ListNode(carry)

        return ans.next

# Problem 2
# Link: https://leetcode.com/problems/add-two-numbers/description/
if __name__ == '__main__':
    s = Solution()
    print(s.addTwoNumbers(
        l1 = ListNode(2, ListNode(4, ListNode(3))),
        l2 = ListNode(5, ListNode(6, ListNode(4))),
    ))
    

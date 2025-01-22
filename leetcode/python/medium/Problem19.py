# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # Create a dummy node to handle edge cases like removing the first node
        ans = ListNode(0, head)
        slow = ans
        fast = ans

        # Move the `fast` pointer n+1 steps ahead
        # This is mathematically provable
        for _ in range(n + 1):
            fast = fast.next

        # Move both `slow` and `fast` pointers until `fast` reaches the end
        while fast is not None:
            slow = slow.next
            fast = fast.next

        # Remove the nth node from the end
        slow.next = slow.next.next

        # Return the modified list
        return ans.next



# Problem 19
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
if __name__ == '__main__':
    s = Solution()
    print(s.removeNthFromEnd(
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
        2,
    ))


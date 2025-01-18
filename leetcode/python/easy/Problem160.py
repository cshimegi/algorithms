# Questions to ask:
# 1. What is the time complexity? O(m + n)
# 2. What is the space complexity? O(1)
# 3. Requirement:
#  (1) the linked lists must retain their original structure after the function returns
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        tempA, tempB = headA, headB
        while tempA != tempB:
            tempA = tempA.next if tempA else headB
            tempB = tempB.next if tempB else headA
        return tempA


# Problem 160
# Tips:
# 1.
# Link: https://leetcode.com/problems/intersection-of-two-linked-lists/description/
if __name__ == '__main__':
    s = Solution()

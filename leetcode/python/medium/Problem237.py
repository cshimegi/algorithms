# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next



# Problem 237
# Link: https://leetcode.com/problems/delete-node-in-a-linked-list/description/
# Tips:
if __name__ == '__main__':
    s = Solution()


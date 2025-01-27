# Questions to ask:
# 1. What is the time complexity? O(1) for each operation
# 2. What is the space complexity?
class Node:
    def __init__(self, value: int, min_val: int):
        self.val = value
        self.min_val = min_val
        self.prev = None
        self.next = None

class MinStack:
    def __init__(self):
        self.head = Node(0, float("inf"))
        self.tail = Node(0, float("inf"))
        self.head.next = self.tail
        self.tail.prev = self.head

    def push(self, val: int) -> None:
        pre_top = self.head.next
        min_val = min(val, pre_top.min_val)
        node = Node(val, min_val)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def pop(self) -> None:
        prev_top = self.head.next
        if prev_top != self.tail:
            self.head.next.next.prev = self.head
            self.head.next = self.head.next.next

    def top(self) -> int:
        top_node = self.head.next
        return top_node.val

    def getMin(self) -> int:
        top_node = self.head.next
        return top_node.min_val

# Without using additional Node
# Reference: https://leetcode.com/problems/min-stack/solutions/3176175/solution
class MinStack2:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val = min(self.minStack[-1],val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# Problem 155
# Link: https://leetcode.com/problems/min-stack/description/
# Tips:
if __name__ == '__main__':
    s = Solution()



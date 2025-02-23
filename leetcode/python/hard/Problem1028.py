# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode | None:
        stack = []  # Stack maintains path from root to current node
        l_traversal, i = len(traversal), 0
        while i < l_traversal:
            depth = 0
            while i < l_traversal and traversal[i] == '-':  # Count depth
                depth += 1
                i += 1

            start = i  # Extract node value (multiple digits)
            while i < l_traversal and traversal[i].isdigit():
                i += 1
            node = TreeNode(int(traversal[start:i]))

            # Maintain correct depth in stack when subtree is completed
            while len(stack) > depth:
                stack.pop()

            if stack:
                # Attach child to parent based on preorder traversal: root -> left -> right
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            stack.append(node)  # Push current node to stack

        return stack[0]

# Problem 1028
# Link: https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        "1-2--3--4-5--6--7",
        "1-2--3---4-5--6---7",
        "1-401--349---90--88"
    ]
    for case in cases:
        print(s.recoverFromPreorder(case))


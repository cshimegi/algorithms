# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string using BFS."""
        if not root:
            return ""

        queue = deque([root])
        res = []

        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('null')

        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree using BFS."""
        if not data:
            return None

        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        i = 1

        while queue:
            node = queue.popleft()

            # Process left child
            if nodes[i] != 'null':
                node.left = TreeNode(int(nodes[i]))
                queue.append(node.left)
            i += 1

            # Process right child
            if nodes[i] != 'null':
                node.right = TreeNode(int(nodes[i]))
                queue.append(node.right)
            i += 1

        return root


# Problem 297
# Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        [1,2,3,null,null,4,5]
    ]



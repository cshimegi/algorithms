# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        ans = [root.val]

        def dfs(node: TreeNode | None):
            if not node:
                return 0

            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)

            # compute max path sum with split
            ans[0] = max(ans[0], node.val + leftMax + rightMax)

            return node.val + max(leftMax, rightMax)

        dfs(root)
        return ans[0]



# Problem 124
# Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
if __name__ == '__main__':
    s = Solution()

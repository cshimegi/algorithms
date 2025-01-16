# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        if not nums:
            return None
        # Since it's sorted, we can set the middle as the root for BST
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


# Problem 108
# Tips:
# 1.
# Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
if __name__ == '__main__':
    s = Solution()


